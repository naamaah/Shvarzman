
function increase(e) {
  const group = e.currentTarget.parentElement;
  const quantity = group.querySelector('.quantity-field');
  const nextValue = Number((quantity.value || 0)) + 1;
  quantity.value = nextValue;
  updateTotalPrice();
}

function decrease(e) {
  const group = e.currentTarget.parentElement;
  const quantity = group.querySelector('.quantity-field');
  const nextValue = Number((quantity.value) || 0) - 1;
  if (nextValue >= 0) {
    quantity.value = nextValue;
    updateTotalPrice();
  }
}


document.addEventListener('DOMContentLoaded', function () {
  const plusButtons = document.querySelectorAll('.button-plus');
  for (let i = 0; i < plusButtons.length; i++) {
    const plusButton = plusButtons[i];
    plusButton.addEventListener('click', increase);
  };

  const minusButtons = document.querySelectorAll('.button-minus');
  for (let i = 0; i < plusButtons.length; i++) {
    const minusButton = minusButtons[i];
    minusButton.addEventListener('click', decrease);
  };

  // const quantities = document.querySelectorAll('.quantity-field');
  // for (let i = 0; i < quantities.length; i++) {
  //   quantities[i].addEventListener('change', updateTotalPrice);
  // }
  //
  // const deleteButtons = document.querySelectorAll('.deleteButton');
  // for (let i = 0; i < deleteButtons.length; i++) {
  //   deleteButtons[i].addEventListener('click', deleteItem);
  // }
});

// function updateTotalPrice() {
//   const quantities = document.querySelectorAll('.quantity-field');
//   let sum = 0;
//   for (let j = 0; j < quantities.length; j++) {
//     const quantity = quantities[j];
//     let priceInfo = quantity.parentElement.querySelector('.price');
//     if (priceInfo === null) {
//       priceInfo = quantity.parentElement.parentElement.querySelector('.price');
//     }
//     const price = Number(priceInfo.textContent);
//     sum += (price * Number(quantity.value));
//   }
//   console.log(sum)
//   document.getElementById('totalPriceText').innerText = "₪ " + sum ;
//   // document.querySelector('#totalPrice').value =sum;
//   // document.querySelector('#totalPriceText').textContent ="₪ " + sum +  " סך הכל לתשלום ";
// }

function submitCart() {
const quantities = document.querySelectorAll('.quantity-field');
let isItem = false;
 for (let j = 0; j < quantities.length; j++) {
    if (quantities[j].value!=0) {
        isItem = true;
    }
}

if (isItem == false)  {
      alert("לא ניתן לעבור לתשלום מכיוון שאין פריטים בסל קניות");
}
else {
  window.location="/payment"
}
}

function openOrderTab(id, date) {
  var idOrder='productsOrder'+id
  var btn='openOrder'+id
  // console.log(date)
  var x = document.getElementById(idOrder);
  if (x.style.display == "none") {
    x.style.display = "block";
    document.getElementById(btn).style.backgroundColor= "#354f52";
    if (id=='00'){
            document.getElementById(btn).innerText = 'סגור הזמנות קודמות';
    }
    else{
            document.getElementById(btn).innerText = "סגור הזמנה מהתאריך " +date;

    }
  } else {
    x.style.display = "none";
    document.getElementById(btn).style.backgroundColor= "#52796f";
            if (id=='00'){
            document.getElementById(btn).innerText = 'צפייה בהזמנות קודמות';
        }
            else{
                document.getElementById(btn).innerText = "הזמנה מהתאריך " +date;

            }

  }
}


