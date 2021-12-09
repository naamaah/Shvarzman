// checking form js
function validateForm() {
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


function validateFormSignUp() {
    var x = document.forms["myForm"]["Email_Login"].value;
    var y = document.forms["myForm"]["psw"].value;
    var z = document.forms["myForm"]["psw-repeat"].value;
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!x.match(mailformat)){
        alert("You have entered an invalid email address!");
        Email_Login.focus();
        return false;
    }
     if (y.length<6) {
         alert("Password must contain at least 6 chars!");
         psw.focus();
         return false;
     }
     if (z!=null){
         if (z != y) {
          alert("Passwords are not the same");
          psw-repeat.focus();
          return false;
         }
     }
    return true;
}



// login js
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Approved form
function formApproved () {
    window.location.href = "formApproval.html";
}




