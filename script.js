$(document).ready(function() {
    $('#send_btn').click(function() {
        var userInput = $('#user_input').val();
        $('#chatlog').append('<div>User: ' + userInput + '</div>');
        $('#user_input').val('');

        $.post('/get', { user_input: userInput }, function(data) {
            $('#chatlog').append('<div>Bot: ' + data.response + '</div>');
            $('#chatlog').scrollTop($('#chatlog')[0].scrollHeight);
        });
    });

    $('#user_input').keypress(function(e) {
        if (e.which === 13) {
            $('#send_btn').click();
        }
    });
});
