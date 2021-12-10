
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// check sign-in
function validateFormlogIn() {
          var x = document.forms["logInForm"]["Email_Login"].value;
          var y = document.forms["logInForm"]["psw"].value;
          var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
          if (!x.match(mailformat)) {
              alert("You have entered an invalid email address!");
              Email_Login.focus();
              return false;
          }
          if (y.length < 6) {
              alert("Password must include at least 6 chars!");
              psw.focus();
              return false;
          }
          alert("Login successfully (:");
          return true;
}

// check sign-up
function validateFormSignUp() {
          var x = document.forms["signUpForm"]["emailSignUp"].value;
          var y = document.forms["signUpForm"]["psw1"].value;
          var z = document.forms["signUpForm"]["psw-repeat1"].value;
          var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
          if (!x.match(mailformat)) {
              alert("You have entered an invalid email address!");
              emailSignUp.focus();
              return false;
          }
          if (y.length < 6) {
              alert("Password must include at least 6 chars!");
              psw.focus();
              return false;
          }
          if (z!=y){
              alert("Passwords are not the same");
              psw1.focus();
              psw-repeat1.focus();
              return false;
          }
          alert("Sign up successfully (:");
          return true;
}

