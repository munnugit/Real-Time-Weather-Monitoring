// static/js/scripts.js

$(document).ready(function() {
    $('#alert-form').on('submit', function(event) {
        event.preventDefault();
        const temperatureThreshold = $('input[name="temperature"]').val();
        const condition = $('input[name="condition"]').val();

        $.ajax({
            type: 'POST',
            url: '/set_threshold',
            data: { temperature: temperatureThreshold, condition: condition },
            success: function(response) {
                alert('Threshold set successfully!');
                $('input[name="temperature"]').val('');  // Clear input
                $('input[name="condition"]').val('');  // Clear input
            }
        });
    });
});
