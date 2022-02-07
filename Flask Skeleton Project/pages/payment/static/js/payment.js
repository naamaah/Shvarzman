function submitPayment() {
  if (checkallInput()){
    alert("התשלום בוצע בהצלחה, אישור התשלום נשלח למייל. הינך מועבר/ת לעמוד הבית");
    // window.location="/"
  }
  else{
    alert("לא ניתן לבצע תשלום מכיוון שלא כל השדות מולאו באופן תקין");
  }
}

function checkallInput(){
  // if(document.getElementById('visa').checked || document.getElementById('mastercard').checked){
  //   if (document.getElementById('creditCardNum').value.length==0 || document.getElementById('creditCardCVVInput').value.length==0){
  //     return false;
  //   }
  // }
  // else if (!document.getElementById('cash').checked){
  //   return false;
  // }
  if (document.getElementById('firstName').value.length==0 ||
      document.getElementById('lastName').value.length==0 ||
      document.getElementById('id').value.length==0 ||
      document.getElementById('creditCardNum').value.length==0 ||
      document.getElementById('creditCardCVVInput').value.length==0 )
        return false;
  return true;
}