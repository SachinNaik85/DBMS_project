function details() {
    var user_information = document.getElementsByClassName('user_information');
    for (var i = 0; i < user_information.length; i++) {
        user_information[i].style = "visibility : visible";
    }
}

function is_valid_search() {
    var from = document.getElementById("from").value;
    var to = document.getElementById("to").value;
    var from_regx = /^[a-zA-Z' ']+$/
    var to_regx = /^[a-zA-Z' ']+$/
    var valid_search = true
    if (!from_regx.test(from)) {
        valid_search = false;
    }

    if (!to_regx.test(to)) {
        valid_search = false;
    }
    return valid_search
}

function close_usinfo() {
    var modalpopup = document.getElementsByClassName('user_information');
    for (var i = 0; i < modalpopup.length; i++) {
        modalpopup[i].style = "visibility: hidden ; filter : blur(0px)";
    }
}

function close_booking_modal() {
    var modal = document.getElementsByClassName("booking_confirmed")
    for (var i = 0; i < modal.length; i++) {
        modal[i].style = "visibility : hidden";
    }
};