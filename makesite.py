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


"""Make static website/blog with Python."""


import os
import shutil
import re
import glob
import sys
import json
import datetime
from pathlib import Path
import unicodedata

def fread(filename):
    """Read file and close the file."""
    with open(filename, 'r') as f:
        return f.read()


def fwrite(filename, text):
    """Write content to file and close the file."""
    basedir = os.path.dirname(filename)
    if not os.path.isdir(basedir):
        os.makedirs(basedir)

    with open(filename, 'w') as f:
        f.write(text)


def log(msg, *args):
    """Log message with specified arguments."""
    sys.stderr.write(msg.format(*args) + '\n')


def truncate(text, words=25):
    """Remove tags and truncate text to the specified number of words."""
    return ' '.join(re.sub('(?s)<.*?>', ' ', text).split()[:words])


def read_headers(text):
    """Parse headers in text and yield (key, value, end-index) tuples."""
    for match in re.finditer(r'\s*<!--\s*(.+?)\s*:\s*(.+?)\s*-->\s*|.+', text):
        if not match.group(1):
            break
        yield match.group(1), match.group(2), match.end()


def rfc_2822_format(date_str):
    """Convert yyyy-mm-dd date string to RFC 2822 format date string."""
    d = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return d.strftime('%a, %d %b %Y %H:%M:%S +0000')


def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

def read_content(filename):
    """Read content and metadata from file into a dictionary."""
    # Read file content.
    text = fread(filename)

    # Read metadata and save it in a dictionary.
    date_slug = os.path.basename(filename).split('.')[0]
    match = re.search(r'^(?:(\d\d\d\d-\d\d-\d\d)-)?(.+)$', date_slug)
    content = {
        'date': match.group(1) or '1970-01-01',
        'slug': match.group(2),
    }

    # Read headers.
    end = 0
    for key, val, end in read_headers(text):
        content[key] = val

    # Separate content from headers.
    text = text[end:]

    # Convert Markdown content to HTML.
    if filename.endswith(('.md', '.mkd', '.mkdn', '.mdown', '.markdown')):
        try:
            if _test == 'ImportError':
                raise ImportError('Error forced by test')
            import commonmark
            text = commonmark.commonmark(text)
        except ImportError as e:
            log('WARNING: Cannot render Markdown in {}: {}', filename, str(e))

    # Update the dictionary with content and RFC 2822 date.
    content.update({
        'content': text,
        'rfc_2822_date': rfc_2822_format(content['date'])
    })

    return content


def render(template, **params):
    """Replace placeholders in template with values from params."""
    return re.sub(r'{{\s*([^}\s]+)\s*}}',
                  lambda match: str(params.get(match.group(1), match.group(0))),
                  template)


def get_categories(page_params):
    cat = []
    if 'category' in page_params:
        cat.append(str(page_params['category']).strip())
    elif 'categories' in page_params:
        for s in page_params['categories'].split(' '):
            if s.strip():
                cat.append(s.strip())
    return cat


def make_pages(src, dst, layout, **params):
    """Generate pages from page content."""
    items = []

    for src_path in glob.glob(src):
        content = read_content(src_path)

        page_params = dict(params, **content)

        # Populate placeholders in content if content-rendering is enabled.
        # if page_params.get('render') == 'yes':
        #     rendered_content = render(page_params['content'], **page_params)
        #     page_params['content'] = rendered_content
        #     content['content'] = rendered_content

        items.append(content)

        dst_path = render(dst, **page_params)
        output = render(layout, **page_params)

        log('Rendering {} => {} ...', src_path, dst_path)
        fwrite(dst_path, output)

    return sorted(items, key=lambda x: x['date'], reverse=True)


def make_posts(src, src_pattern, dst, layout, category_layout, **params):
    """Generate posts from posts directory."""
    items = []

    for posix_path in Path(src).glob(src_pattern):
        src_path = str(posix_path)
        content = read_content(src_path)

        page_params = dict(params, **content)
        page_params['banner'] =' '
        page_params['date_path'] = page_params['date'].replace('-', '/')
        page_params['year'] = page_params['date'].split('-')[0]

        # categories
        categories = get_categories(page_params)
        out_cats = []
        for category in categories:
            out_cat = render(category_layout, category=category, url=slugify(category))
            out_cats.append(out_cat.strip())
        page_params['category_label'] = ''.join(out_cats)

    
        # Populate placeholders in content if content-rendering is enabled.
        # if page_params.get('render') == 'yes':
        #      rendered_content = render(page_params['content'], **page_params)
        #      page_params['content'] = rendered_content
        #      content['content'] = rendered_content

        summary_index = page_params['content'].find('<!-- more')
        if summary_index > 0:
            content['summary'] = render(page_params['content'][:summary_index], **page_params)

        content['year'] = page_params['year']
        content['category_label'] = page_params['category_label']

        items.append(content)

        # TODO DEBUG
        #print(page_params) 
        #print(content)  
        #break

        dst_path = render(dst, **page_params)
        output = render(layout, **page_params)

        log('Rendering {} => {} ...', src_path, dst_path)
        fwrite(dst_path, output)

    return sorted(items, key=lambda x: x['date'], reverse=True)


def make_list(posts, dst, list_layout, item_layout, banner_layout, **params):
    """Generate list page for a blog."""
    items = []
    for post in posts:
        item_params = dict(params, **post)
        if 'summary' not in item_params:
            item_params['summary'] = truncate(post['content'])
        item = render(item_layout, **item_params)
        items.append(item)

    banner = render(banner_layout, **params)
    params['banner'] = banner

    params['content'] = ''.join(items)
    dst_path = render(dst, **params)
    output = render(list_layout, **params)

    log('Rendering list => {} ...', dst_path)
    fwrite(dst_path, output)


def main():
    # Create a new _site directory from scratch.
    if os.path.isdir('_site'):
        shutil.rmtree('_site')
    shutil.copytree('static', '_site')

    # Default parameters.
    params = {
        'base_path': '',
        'title': 'Blog',
        'subtitle': 'Lorem Ipsum',
        'author': 'Admin',
        'site_url': 'http://localhost:8000',
        'current_year': datetime.datetime.now().year
    }

    # If params.json exists, load it.
    if os.path.isfile('params.json'):
        params.update(json.loads(fread('params.json')))

    # Load layouts.
    page_layout = fread('layout/page.html')
    post_layout = fread('layout/post.html')
    list_layout = fread('layout/list.html')
    item_layout = fread('layout/item.html')
    banner_layout = fread('layout/banner.html')
    category_layout = fread('layout/category.html')
    feed_xml = fread('layout/feed.xml')
    item_xml = fread('layout/item.xml')

    # Combine layouts to form final layouts.
    post_layout = render(page_layout, content=post_layout)
    list_layout = render(page_layout, content=list_layout)

    # Create site pages.
    make_pages('content/index.html', '_site/index.html',
               page_layout, **params)
    #make_pages('content/[!_]*.html', '_site/{{ slug }}/index.html',
    #           page_layout, **params)

    # Create blogs.
    blog_posts = make_posts('posts', '**/*.md',
                            '_site/{{ year }}/{{ slug }}.html',
                            post_layout, category_layout, **params)

    # Create blog list pages.
    make_list(blog_posts, '_site/index.html',
              list_layout, item_layout, banner_layout, **params)

    # Create RSS feeds.
    #make_list(blog_posts, '_site/blog/rss.xml',
    #          feed_xml, item_xml, banner_layout, **params)


# Test parameter to be set temporarily by unit tests.
_test = None


if __name__ == '__main__':
    main()
