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