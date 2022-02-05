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





function submitFormTours() {
         if (document.getElementById('tour_dt').value.length==0 ||
             document.getElementById('emailaddress').value.length==0 ||
             document.getElementById('numOfTickets').value.length==0)  {
              alert("לא ניתן לשלוח את הטופס מכיוון שלא כל השדות מולאו באופן תקין");
             }
         else {
               // alert("שמחים שבחרת להגיע לסיור שלנו! הרשמתך נקלטה במערכת");
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





