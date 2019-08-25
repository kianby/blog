// --------------------------------------------------------------------------
//  Common functions
// --------------------------------------------------------------------------

function show_hide(panel_id, button_id){
    if (document.getElementById(panel_id).style.display == 'none'){
        document.getElementById(panel_id).style.display = '';
        document.getElementById(button_id).style.display = 'none';
    } else {
        document.getElementById(panel_id).style.display = 'none';
    }
}

// --------------------------------------------------------------------------
//  Markdown preview
// --------------------------------------------------------------------------

function preview_markdown() {
    if (document.getElementById('preview-container').style.display == 'none'){
        document.getElementById('preview-container').style.display = '';
    }
    var $ = function (id) { return document.getElementById(id); };
    new Editor($("message"), $("preview"));
}

function Editor(input, preview) {
    this.update = function () {
        preview.innerHTML = markdown.toHTML(input.value);
    };
    input.editor = this;
    this.update();
}
