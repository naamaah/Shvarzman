function openForm(id) {
    var containerID='gridContainer'+id
    var buttonID='btnGridContainer'+id
    console.log(containerID)
    console.log(buttonID)
    var x = document.getElementById(containerID);
    if (x.style.display == "none") {
        x.style.display = "block";
        if (id=='1'){
            document.getElementById(buttonID).innerText = 'סגור הרשמה לסיור';
        }
        else{
            document.getElementById(buttonID).innerText = 'סגור עדכון לסיור';
        }
    } else {
        x.style.display = "none";
                if (id=='1'){
            document.getElementById(buttonID).innerText = 'פתיחת טופס הרשמה לסיור';
        }
        else{
            document.getElementById(buttonID).innerText = 'פתיחת טופס עדכון סיור קיים';
        }
    }
}

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

function submitFormTours(id_1, id_2) {
    if (document.getElementById(id_1).value.length == 0 ||
        document.getElementById(id_2).value.length == 0) {
        alert("לא ניתן לשלוח את הטופס מכיוון שלא הוזנה כמות הכרטיסים הרצויה");
        event.preventDefault();
        return false;
    }
}

function checkNumOfTickets(id) {
    var numOfTickets = document.getElementById(id).value;
    if (numOfTickets <= 0 || numOfTickets > 10) {
        alert("ניתן לרכוש באתר בין 1-10 כרטיסים, במידה ואתם קבוצה גדולה יותר צרו איתנו קשר");
        document.getElementById(id).value = "";
    }
}
