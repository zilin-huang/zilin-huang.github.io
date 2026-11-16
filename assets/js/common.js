$(document).ready(function() {
    $('a.abstract').click(function() {
        $(this).parent().parent().find(".abstract.hidden").toggleClass('open');
        $(this).parent().parent().find(".bibtex.hidden.open").toggleClass('open');
    });
    $('a.bibtex').click(function() {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
        $(this).parent().parent().find(".abstract.hidden.open").toggleClass('open');
    });
    $('a').removeClass('waves-effect waves-light');
    
    // Image loading optimization
    $('img[loading="lazy"]').on('load', function() {
        $(this).addClass('loaded');
    });
    
    // Preload critical images (above the fold)
    $('img:not([loading="lazy"])').each(function() {
        if (this.complete) {
            $(this).addClass('loaded');
        } else {
            $(this).on('load', function() {
                $(this).addClass('loaded');
            });
        }
    });
});
