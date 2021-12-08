
function validateForm(formType) {
    var x = document.forms["myForm"]["fname"].value;
    var y = document.forms["myForm"]["lname"].value;
    var z = document.forms["myForm"]["phone"].value;
    var k = document.forms["myForm"]["email"].value;
    if (x == "" || y == "") {
        alert("Full name must be filled out");
        fname.focus();
        lname.focus();
        return false;
    }
    var phoneFormat = /^\d{10}$/;
    if (!z.match(phoneFormat)) {
        alert("You have entered an invalid phone number!");
        phone.focus();
        return false;
    }
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!k.match(mailformat)){
        alert("You have entered an invalid email address!");
        email.focus();
        return false;
    }
    if (formType == "tour") {
        const inpObj = document.getElementById("numOfTickets");
        if (!inpObj.checkValidity()) {
            alert("number of tickects must have between 0 to 10");
            return false;
        }
    }
    return true;
}





