#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2018 Sunaina Pai
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Modifed by Yax

"""Make static website/blog with Python."""

import sys
import os
import shutil
import re
import glob
import json
import datetime
import time
from email import utils
from pathlib import Path
import unicodedata
import locale
import requests
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

# set user locale
locale.setlocale(locale.LC_ALL, "")

# initialize markdown


class HighlightRenderer(mistune.Renderer):

    options = {"escape": False, "hard_wrap": True}

    def block_code(self, code, lang):
        if not lang:
            return "\n<pre><code>%s</code></pre>\n" % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


def fread(filename):
    """Read file and close the file."""
    with open(filename, "r") as f:
        return f.read()


def fwrite(filename, text):
    """Write content to file and close the file."""
    basedir = os.path.dirname(filename)
    if not os.path.isdir(basedir):
        os.makedirs(basedir)

    with open(filename, "w") as f:
        f.write(text)


def log(msg, *args):
    """Log message with specified arguments."""
    sys.stderr.write(msg.format(*args) + "\n")


def truncate(text, words=25):
    """Remove tags and truncate text to the specified number of words."""
    return " ".join(re.sub("(?s)<.*?>", " ", text).split()[:words])


def read_headers(text):
    """Parse headers in text and yield (key, value, end-index) tuples."""
    for match in re.finditer(r"\s*<!--\s*(.+?)\s*:\s*(.+?)\s*-->\s*|.+", text):
        if not match.group(1):
            break
        yield match.group(1), match.group(2), match.end()


def rfc_2822_format(date_str):
    """Convert yyyy-mm-dd date string to RFC 2822 format date string."""
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    dtuple = d.timetuple()
    dtimestamp = time.mktime(dtuple)
    return utils.formatdate(dtimestamp)


def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub("[^\w\s-]", "", value).strip().lower()
    return re.sub("[-\s]+", "-", value)


def read_content(filename):
    """Read content and metadata from file into a dictionary."""
    # Read file content.
    text = fread(filename)

    # Read metadata and save it in a dictionary.
    date_slug = os.path.basename(filename).split(".")[0]
    match = re.search(r"^(?:(\d\d\d\d-\d\d-\d\d)-)?(.+)$", date_slug)
    content = {"date": match.group(1) or "1970-01-01", "slug": match.group(2)}

    # Read headers.
    end = 0
    for key, val, end in read_headers(text):
        content[key] = val

    # slugify post title
    content["slug"] = slugify(content["title"])

    # Separate content from headers.
    text = text[end:]

    # Convert Markdown content to HTML.
    if filename.endswith((".md", ".mkd", ".mkdn", ".mdown", ".markdown")):
        summary_index = text.find("<!-- more")
        if summary_index > 0:
            summary = markdown(clean_html_tag(text[:summary_index]))
        else:
            summary = truncate(markdown(clean_html_tag(text)))
        clean_text = text.replace("<!-- more -->", "")
        text = markdown(clean_text)
    else:
        summary = truncate(text)

    # Update the dictionary with content and RFC 2822 date.
    content.update(
        {
            "content": text,
            "rfc_2822_date": rfc_2822_format(content["date"]),
            "summary": summary,
        }
    )

    return content


def clean_html_tag(text):
    """Remove HTML tags."""
    while True:
        original_text = text
        text = re.sub("<\w+.*?>", "", text)
        text = re.sub("<\/\w+>", "", text)
        if original_text == text:
            break
    return text


def render(template, **params):
    """Replace placeholders in template with values from params."""
    return re.sub(
        r"{{\s*([^}\s]+)\s*}}",
        lambda match: str(params.get(match.group(1), match.group(0))),
        template,
    )


def get_header_list_value(header_name, page_params):
    l = []
    if header_name in page_params:
        for s in page_params[header_name].split(" "):
            if s.strip():
                l.append(s.strip())
    return l


def get_friendly_date(date_str):
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%d %b %Y")


def make_posts(
    src, src_pattern, dst, layout, category_layout, comment_layout, comment_detail_layout, **params
):
    """Generate posts from posts directory."""
    items = []

    for posix_path in Path(src).glob(src_pattern):
        src_path = str(posix_path)
        content = read_content(src_path)

        # render text / summary for basic fields
        content["content"] = render(content["content"], **params)
        content["summary"] = render(content["summary"], **params)

        page_params = dict(params, **content)
        page_params["header"] = ""
        page_params["footer"] = ""
        page_params["date_path"] = page_params["date"].replace("-", "/")
        page_params["friendly_date"] = get_friendly_date(page_params["date"])
        page_params["year"] = page_params["date"].split("-")[0]
        page_params["post_url"] = page_params["year"] + "/" + page_params["slug"] + "/"

        # categories
        categories = get_header_list_value("category", page_params)
        out_cats = []
        for category in categories:
            out_cat = render(category_layout, category=category, url=slugify(category))
            out_cats.append(out_cat.strip())
        page_params["categories"] = categories
        page_params["category_label"] = "".join(out_cats)

        # tags
        tags = get_header_list_value("tag", page_params)
        page_params["tags"] = tags

        #  comments
        page_comment = page_params.get("comment", "yes")
        if page_comment == "no":
            is_page_comment_enabled = False
        else:
            is_page_comment_enabled = True

        page_params["comment_count"] = 0
        page_params["comments"] = ""
        page_params["comment"] = ""

        if params["stacosys_url"] and is_page_comment_enabled:
            req_url = params["stacosys_url"] + "/comments"
            query_params = dict(
                token=params["stacosys_token"], url="/" + page_params["post_url"] 
            )
            resp = requests.get(url=req_url, params=query_params)
            comments = resp.json()["data"]
            out_comments = []
            for comment in comments:
                site=comment.get("site", "")
                if site:
                    site_start = '<a href="' + site + '">'
                    site_end = '</a>'
                else:
                    site_start = ''
                    site_end = ''
                out_comment = render(
                    comment_detail_layout,
                    author=comment["author"],
                    avatar=comment.get("avatar", ""),
                    site_start=site_start,
                    site_end=site_end,
                    date=comment["date"],
                    content=markdown(comment["content"]),
                )
                out_comments.append(out_comment)
            page_params["comments"] = "".join(out_comments)
            page_params["comment_count"] = len(comments)
            page_params["comment"] = render(comment_layout, **page_params)

        content["year"] = page_params["year"]
        content["post_url"] = page_params["post_url"]
        content["categories"] = page_params["categories"]
        content["category_label"] = page_params["category_label"]
        content["tags"] = page_params["tags"]
        content["friendly_date"] = page_params["friendly_date"]
        content["comment_count"] = page_params["comment_count"]
        items.append(content)

        dst_path = render(dst, **page_params)
        output = render(layout, **page_params)

        log("Rendering {} => {} ...", src_path, dst_path)
        fwrite(dst_path, output)

    return sorted(items, key=lambda x: x["date"], reverse=True)


def make_list(
    posts, dst, list_layout, item_layout, header_layout, footer_layout, **params
):
    """Generate list page for a blog."""

    # header
    if header_layout is None:
        params["header"] = ""
    else:
        header = render(header_layout, **params)
        params["header"] = header

    # footer
    if footer_layout is None:
        params["footer"] = ""
    else:
        footer = render(footer_layout, **params)
        params["footer"] = footer

    # content
    items = []
    for post in posts:
        item_params = dict(params, **post)
        if "comment_count" in item_params and item_params["comment_count"]:
            if item_params["comment_count"] == 1:
                item_params["comment_label"] = "1 commentaire"
            else:
                item_params["comment_label"] = (
                    str(item_params["comment_count"]) + " commentaires"
                )
        else:
            item_params["comment_label"] = ""
        item = render(item_layout, **item_params)
        items.append(item)
    params["content"] = "".join(items)
    dst_path = render(dst, **params)
    output = render(list_layout, **params)

    log("Rendering list => {} ...", dst_path)
    fwrite(dst_path, output)


def main():
    # Create a new _site directory from scratch.
    if os.path.isdir("_site"):
        shutil.rmtree("_site")
    shutil.copytree("static", "_site")

    # Default parameters.
    params = {
        "title": "Blog",
        "subtitle": "Lorem Ipsum",
        "author": "Admin",
        "site_url": "http://localhost:8000",
        "current_year": datetime.datetime.now().year,
        "stacosys_token": "",
        "stacosys_url": "",
    }

    # If params.json exists, load it.
    if os.path.isfile("params.json"):
        params.update(json.loads(fread("params.json")))

    # Load layouts.
    banner_layout = fread("layout/banner.html")
    paging_layout = fread("layout/paging.html")
    archive_title_layout = fread("layout/archives.html")
    page_layout = fread("layout/page.html")
    post_layout = fread("layout/post.html")
    list_layout = fread("layout/list.html")
    item_layout = fread("layout/item.html")
    item_nosummary_layout = fread("layout/item_nosummary.html")
    category_title_layout = fread("layout/category_title.html")
    category_layout = fread("layout/category.html")
    comment_layout = fread("layout/comment.html")
    comment_detail_layout = fread("layout/comment-detail.html")
    rss_xml = fread("layout/rss.xml")
    rss_item_xml = fread("layout/rss_item.xml")
    sitemap_xml = fread("layout/sitemap.xml")
    sitemap_item_xml = fread("layout/sitemap_item.xml")

    # Combine layouts to form final layouts.
    post_layout = render(page_layout, content=post_layout)
    list_layout = render(page_layout, content=list_layout)

    # Create blogs.
    blog_posts = make_posts(
        "posts",
        "**/*.md",
        "_site/{{ post_url }}/index.html",
        post_layout,
        category_layout,
        comment_layout,
        comment_detail_layout,
        **params
    )

    # Create blog list pages.
    page_size = 10
    chunk_posts = [
        blog_posts[i : i + page_size] for i in range(0, len(blog_posts), page_size)
    ]
    page = 1
    last_page = len(chunk_posts)
    for chunk in chunk_posts:
        params["page"] = page
        if page == last_page:
            params["next_page"] = ""
        else:
            params["next_page"] = "/page" + str(page + 1) + "/"
        if page == 1:
            params["previous_page"] = ""
            make_list(
                chunk,
                "_site/index.html",
                list_layout,
                item_layout,
                banner_layout,
                paging_layout,
                **params
            )
        else:
            params["previous_page"] = "/page" + str(page - 1) + "/"
        make_list(
            chunk,
            "_site/page" + str(page) + "/index.html",
            list_layout,
            item_layout,
            banner_layout,
            paging_layout,
            **params
        )
        page = page + 1

    # Create category pages
    catpost = {}
    for post in blog_posts:
        for cat in post["categories"]:
            if cat in catpost:
                catpost[cat].append(post)
            else:
                catpost[cat] = [post]
    for cat in catpost.keys():
        params["category"] = cat
        make_list(
            catpost[cat],
            "_site/" + slugify(cat) + "/index.html",
            list_layout,
            item_nosummary_layout,
            category_title_layout,
            None,
            **params
        )

    # Create archive page
    make_list(
        blog_posts,
        "_site/archives/index.html",
        list_layout,
        item_nosummary_layout,
        archive_title_layout,
        None,
        **params
    )

    # Create main RSS feed for 10 last entries
    nb_items = min(10, len(blog_posts))
    make_list(
        blog_posts[:nb_items],
        "_site/rss.xml",
        rss_xml,
        rss_item_xml,
        None,
        None,
        **params
    )

    # Create RSS feed by tag
    tagpost = {}
    for post in blog_posts:
        for tag in post["tags"]:
            if tag in tagpost:
                tagpost[tag].append(post)
            else:
                tagpost[tag] = [post]
    for tag in tagpost.keys():
        params["tag"] = tag
        make_list(
            tagpost[tag],
            "_site/rss." + slugify(tag) + ".xml",
            rss_xml,
            rss_item_xml,
            None,
            None,
            **params
        )

    # Create sitemap
    make_list(
        blog_posts,
        "_site/sitemap.xml",
        sitemap_xml,
        sitemap_item_xml,
        None,
        None,
        **params
    )


# Test parameter to be set temporarily by unit tests.
_test = None


if __name__ == "__main__":
    main()
