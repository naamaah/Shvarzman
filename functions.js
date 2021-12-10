
// check tour and contact us forms
function validateForm() {
    var x = document.forms["myForm"]["firstname"].value;
    var y = document.forms["myForm"]["lastname"].value;
    var z = document.forms["myForm"]["phonenumer"].value;
    var k = document.forms["myForm"]["emailaddress"].value;
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
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (!k.match(mailformat)){
        alert("You have entered an invalid email address!");
        email.focus();
        return false;
    }
    alert("The form was successfully received");
    return true;
}


// check sign-in form
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

// check sign-up form
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

// log in page
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


// tour
/*var imgs = ["pictures/pumpkin.jpg","pictures/sweetPotato.jpg"];
var i=0;
function stopMotion () {
    setTimeOut(()=>{
                document.getElementById("img").src= imgs[i];
                i++;
                if (i < imgs.length) {
                    stopMotion ();
                }
                else {
                    i=0;
                }
},500);
}

if (formType == "tour") {
        const inpObj = document.getElementById("numOfTickets");
        if (!inpObj.checkValidity()) {
            alert("number of tickects must have between 0 to 10");
            return false;
        }

*/

// QA
function openQuestion(name) {
  var x = document.getElementById(name);
  if (x.style.display == "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function openQASub(evt, type) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace("active", "");
  }
  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(type).style.display = "block";
  evt.currentTarget.className += " active";

}

//tour
function openForm() {
  var x = document.getElementById('gridContainer');
  if (x.style.display == "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


// photo gallery
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}
