// recipes
function openRec(id) {
  var x='content'+id
  var y='btnRes'+id
  console.log(x);
  console.log(y);
  var text = document.getElementById(x);

  if (text.style.display == "none") {
    text.style.display = "block";
    document.getElementById(y).innerText = 'קרא פחות';
  } else {
    text.style.display = "none";
    document.getElementById(y).innerText = 'קרא עוד';
  }
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