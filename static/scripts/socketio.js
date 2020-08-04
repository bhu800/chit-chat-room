$(document).ready(function(){
    // make socket object
    var socket = io();

    let room = 'lounge';
    joinRoom(room);

    // send info that socketio has been connected
    // socket.on('connect', function(){
    //     socket.send(data = "I am Connected!!")
    // });

    // show message on receiving message in 'message' event bucket
    socket.on('message',function(data){

        if (data.username) {
            printUserMsg(data);
        }
        else {
            printSysMsg(data.msg);
        }
    });

    // send message on pressing submit button
    $('#send_message').click(function(){
        // console.log($('#user_message').val())
        // console.log(room);
        socket.send({'msg': $('#user_message').val(), 'username': username, 'room': room});
        // Clear the input area
        $('#user_message').val("");
    });

    // send message on pressing 'enter'
    $('#user_message').keypress(function(e){
        if(e.keyCode==13){
            // console.log($('#user_message').val())
            // console.log(room);
            socket.send({'msg': $('#user_message').val(), 'username': username, 'room': room});
            // Clear the input area
            $('#user_message').val("");
        }
    });

    $('.select-room').each(function(){
        $( this ).click(function(e){              // Important NOTE: don't forget to keep space in $() with 'this' keyword, otherwise it will give unexpected behaviour
            let newRoom = this.innerHTML.toLowerCase();
            // console.log(newRoom);
            // console.log(this);
            console.log(newRoom, room);
            if (newRoom == room) {
                msg = `You already in ${room} room.`;
                printSysMsg(msg);
            }
            else {
                leaveRoom(room);
                joinRoom(newRoom);
                msg = `You entered in ${room} room.`;
                room = newRoom;
                printSysMsg(msg);
            }
        })
    });

    // Leave Room function
    function leaveRoom(room) {
        console.log(room)
        socket.emit('leave', {'username': username, 'room': room});
    };

    // Join Room function
    function joinRoom(room) {
        console.log(room)
        socket.emit('join', {'username': username, 'room': room});
        // Clear message area
        $('#display-chat-section').empty();
        // Autofocus to input area whenever user joins a room
        $('#user_message').focus();
    };

    // Print system messages
    function printSysMsg(msg) {
        var sys_msg = $('<p></p>').text(msg);
        $('#display-chat-section').append(sys_msg);
    }

    function printUserMsg(msg) {
        var message = $("<p></p>").text(msg.msg)
        var username_span = $("<span></span>").text(msg.username)
        var timestamp_span = $("<p></p>").text(msg.timestamp)
        $('#display-chat-section').append(username_span, ": ", message, timestamp_span, "<br>")
    }
})