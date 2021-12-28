//mainPage

var index = 0;
change();

function change() {
    var x = document.getElementsByClassName('sildes');
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    index++;

    if (index > x.length) {
        index = 1;
    }
    x[index - 1].style.display = "block";

    //set loop to change image every 3000 milliseconds (3 seconds)
    setTimeout(change, 3000);
}
