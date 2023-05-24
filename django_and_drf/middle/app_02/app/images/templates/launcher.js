(function() {
    if(!window.mark) {
        mark_js = document.body.appendChild(document.
            createElement('script'));
            mark_js.src = '//127.0.0.1:8000/static/js/mark.js?r=' + Math.
            floor(Math.random() * 9999999999999999);
            window.mark = true;
    }
    else {
        markLaunc();
    }
})();