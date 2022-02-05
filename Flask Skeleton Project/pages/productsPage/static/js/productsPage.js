
function increase(e) {
  const group = e.currentTarget.parentElement;
  const quantity = group.querySelector('.quantity-field');
  const nextValue = Number((quantity.value || 0)) + 1;
  quantity.value = nextValue;
}

function decrease(e) {
  const group = e.currentTarget.parentElement;
  const quantity = group.querySelector('.quantity-field');
  const nextValue = Number((quantity.value) || 0) - 1;
  if (nextValue >= 0) {
    quantity.value = nextValue;
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

});

function submitProduct(btnQuantity) {
  var id = 'btnquantity'+btnQuantity
  console.log(id);
  const quantity = document.getElementById(id)
  if (quantity.value==0) {
        alert("לא ניתן להוסיף לסל פריט עם כמות 0");
    }
}




