//mainPage
 function moveAndClick(){
    window.location='Recipes.html';
    setTimeout(function(){
    document.getElementById("defaultOpen").click();
}, 2000);


}

// check forms inputs
function checkName(id){
  var name=document.getElementById(id).value;
  if (name.length<=1){
    alert("שם חייב להכיל לפחות 2 אותיות");
    document.getElementById(id).value="";
  }
}

function checkID (id){
  var idNumber=document.getElementById(id).value;
  var checkIdNumber=onlyNumbers(idNumber);
  if (checkIdNumber.length!=9) {
    alert("תעודת זהות צריכה להכיל בדיוק 9 ספרות");
    document.getElementById(id).value="";
  }
  else{
    document.getElementById(id).value=checkIdNumber;
  }
}

function checkCreditNum(id){
  var creditNum=document.getElementById(id).value;
  var checkCreditNum=onlyNumbers(creditNum);
  if (checkCreditNum.length<9 || checkCreditNum.length>16){
    alert("מספר הספרות של כרטיס האשראי נדרש להיות בין 9-16 ספרות");
    document.getElementById(id).value="";
  }
  else{
    document.getElementById(id).value=checkCreditNum;
  }
}

function checkCVV (id){
  var cvv=document.getElementById(id).value;
  var checkCvv=onlyNumbers(cvv);
  if (checkCvv.length!=3){
    alert("נדרש להכיל 3 ספרות בדיוק");
    document.getElementById(id).value="";
  }
  else{
    document.getElementById(id).value=checkCvv;
  }
}

function checkEmail (id){
  var email=document.getElementById(id).value;
  var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
  if (!email.match(mailformat)){
        alert("כתובת דואר אלקטרוני שהוזנה לא תקינה");
        document.getElementById(id).value="";
  }
}

function checkPhone (id){
  var phone=document.getElementById(id).value;
  var checkPhone=onlyNumbers(phone);
  var phoneFormat = /^\d{10}$/;
    if (!checkPhone.match(phoneFormat)) {
         alert("מספר הטלפון שהוזן אינו תקין");
    document.getElementById(id).value="";
  }
  else{
    document.getElementById(id).value=checkPhone;
  }
}

function checkNumOfTickets(id){
  var numOfTickets=document.getElementById(id).value;
  if (numOfTickets<=0 || numOfTickets>10){
    alert("ניתן לרכוש באתר בין 1-10 כרטיסים, במידה ואתם קבוצה גדולה יותר צרו איתנו קשר");
    document.getElementById(id).value="";
  }
}

function checkPassword(id){
  var password=document.getElementById(id).value;
  if (password.length<6){
    alert("סיסמא צריכה לכלול לפחות 6 תווים");
    document.getElementById(id).value="";
  }
}

function onlyNumbers(num){
  var ans="";
  var i;
  for (i = 0; i < num.length; i++) {
    var digit = num[i];
    if (digit=='0' || digit=='1' || digit=='2' || digit=='3' || digit=='4' || digit=='5' || digit=='6' || digit=='7' || digit=='8' || digit=='9'){
      ans += num[i];
    }
  }
  return ans;
}


function submitPayment() {
  if (checkallInput()){
    alert("התשלום בוצע בהצלחה, אישור התשלום נשלח למייל. הינך מועבר/ת לעמוד הבית");
    window.location="mainPage.html";
  }
  else{
    alert("לא ניתן לבצע תשלום מכיוון שלא כל השדות מולאו באופן תקין");
  }
}

function checkallInput(){
  if(document.getElementById('visa').checked || document.getElementById('mastercard').checked){
    if (document.getElementById('creditCardNum').value.length==0 || document.getElementById('creditCardCVVInput').value.length==0){
      return false;
    }
  }
  else if (!document.getElementById('cash').checked){
    return false;
  }
  if (document.getElementById('firstName').value.length==0 ||
      document.getElementById('lastName').value.length==0 ||
      document.getElementById('id').value.length==0) {
        return false;
      }
  return true;
}


function submitForm() {
         if (document.getElementById('firstname').value.length==0 ||
             document.getElementById('lastname').value.length==0 ||
             document.getElementById('phonenumer').value.length==0 ||
             document.getElementById('emailaddress').value.length==0 ||
             document.getElementById('numOfTickets').value.length==0)  {
              alert("לא ניתן לשלוח את הטופס מכיוון שלא כל השדות מולאו באופן תקין");
             }
         else {
              alert("הטופס נשלח בהצלחה. הינך מועבר/ת לעמוד הבית");
              window.location="mainPage.html";
           }
}


function submitFormContact() {
         if (document.getElementById('firstname').value.length==0 ||
             document.getElementById('lastname').value.length==0 ||
             document.getElementById('phonenumer').value.length==0 ||
             document.getElementById('emailaddress').value.length==0){
              alert("לא ניתן לשלוח את הטופס מכיוון שלא כל השדות מולאו באופן תקין");
               }
         else {
                 alert("הטופס נשלח בהצלחה. הינך מועבר/ת לעמוד הבית");
                 window.location="mainPage.html";
          }
}


function submitlogIn(){
     if (document.getElementById('Email_Login').value.length==0 ||
      document.getElementById('psw').value.length==0){
       alert("לא ניתן לשלוח את הטופס מכיוון שלא כל השדות מולאו באופן תקין");
      }
     else {
         alert("כניסתך למערכת בוצעה בהצלחה. הינך מועבר/ת לעמוד הבית");
         window.location="mainPage.html";
     }
}

function submitSignUp(){
     if (document.getElementById('emailSignUp').value.length==0 ||
      document.getElementById('psw1').value.length==0 ||
          document.getElementById('psw-repeat1').value.length==0){
       alert("לא ניתן לשלוח את הטופס מכיוון שלא כל השדות מולאו באופן תקין");
      }
     else if (document.getElementById('psw1').value != document.getElementById('psw-repeat1').value) {
        alert("הסיסמאות שהוזנו אינן זהות זו לזו");
     }
     else {
         alert("נרשמת בהצלחה למערכת. הינך מועבר/ת לעמוד הבית");
         window.location="mainPage.html";
     }
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

// recipes

  $(document).ready(function(){
   $(".more.btn").on('click', function(){
    $(this).parent().parent().find(".more-text").toggleClass("active");
   });
  });