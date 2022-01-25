console.log('pleassssssssssssssss');

function addToCart(name) {
  window.location='/shopPage'
}

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

function deleteItem(e) {
  const row = e.currentTarget.parentElement.parentElement;
  let index = 0;
  let previousSibling = row.previousElementSibling;
  while (previousSibling !== null) {
    previousSibling = previousSibling.previousElementSibling;
    index++;
  }
  row.parentElement.deleteRow(index);
  updateTotalPrice();
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

  const navToggles = document.querySelectorAll('.navToggle');
  for (let i = 0; i < navToggles.length; i++) {
    const navButton = navToggles[i];
    navButton.addEventListener('click', toggleNav);
  };

  const quantities = document.querySelectorAll('.quantity-field');
  for (let i = 0; i < quantities.length; i++) {
    quantities[i].addEventListener('change', updateTotalPrice);
  }

  const deleteButtons = document.querySelectorAll('.deleteButton');
  for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener('click', deleteItem);
  }
});

function updateTotalPrice() {
  const quantities = document.querySelectorAll('.quantity-field');
  let sum = 0;
  for (let j = 0; j < quantities.length; j++) {
    const quantity = quantities[j];
    let priceInfo = quantity.parentElement.querySelector('.price');
    if (priceInfo === null) {
      priceInfo = quantity.parentElement.parentElement.querySelector('.price');
    }
    const price = Number(priceInfo.textContent);
    sum += (price * Number(quantity.value));
  }
  document.querySelector('#totalPrice').value =sum;
  document.querySelector('#totalPriceText').textContent ="₪ " + sum +  " סך הכל לתשלום ";
}
