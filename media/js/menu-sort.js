
/*
jQuery(function($) {
    $('div.inline-group').sortable({
        items: 'div.inline-related',
        handle: 'h3:first'
    });
    $('div.inline-related h3').css('cursor', 'move');
    $('div.inline-related').find('input[id$=ordering]').parent('div').hide();
    $('#menucategory_form').submit(function() {
        $('div.inline-group > div.inline-related').each(function(i) {
            if ($(this).find('input[id$=name]').val()) {
                $(this).find('input[id$=ordering]').val(i+1);
            }
        });
    });
});
*/


    jQuery(function($) {
        $('div.inline-group').sortable({
            items: '.inline-related tbody tr',
            handle: 'td',
            update: function() {
                $(this).find('.inline-related tbody tr').each(function(i) {
                	if($(this).find('input[name$=name]').val()){
                    	$(this).find('input[name$=ordering]').val(i+1);
                	}
                    $(this).removeClass('row1').removeClass('row2');
                    $(this).addClass('row'+((i%2)+1));
                });
            }
        });
        $('tr.has_original').css('cursor', 'move');
    });
    
    jQuery(function($) {
        $('td[class^=col] > input.vTextField').width('10em');
    });    