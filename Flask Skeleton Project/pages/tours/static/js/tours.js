function openForm() {
    var x = document.getElementById('gridContainer');
    if (x.style.display == "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
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
