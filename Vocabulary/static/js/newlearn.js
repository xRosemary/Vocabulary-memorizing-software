let word_str = document.getElementById("word_str");
let Candidate_0 = document.getElementById("Candidate_0");
let Candidate_1 = document.getElementById("Candidate_1");
let Candidate_2 = document.getElementById("Candidate_2");
let Candidate_3 = document.getElementById("Candidate_3");

let currentAnswer = 0;
let ajax = {};
ajax.getNextWord = function () {
    $("#Candidate_0").removeClass("btn-danger");
    $("#Candidate_0").addClass("btn-primary");
    $("#Candidate_1").removeClass("btn-danger");
    $("#Candidate_1").addClass("btn-primary");
    $("#Candidate_2").removeClass("btn-danger");
    $("#Candidate_2").addClass("btn-primary");
    $("#Candidate_3").removeClass("btn-danger");
    $("#Candidate_3").addClass("btn-primary");

    $.ajax({
        type: "post",
        url: "/req/getNextWord",
        success: function (d) {
            word_str.innerText = d['WORD']

            Candidate_0.innerText = d['Candidate'][0]["CN"]
            Candidate_0.setAttribute("value", d['Candidate'][0]["ID"])
            Candidate_1.innerText = d['Candidate'][1]["CN"]
            Candidate_1.setAttribute("value", d['Candidate'][1]["ID"])
            Candidate_2.innerText = d['Candidate'][2]["CN"]
            Candidate_2.setAttribute("value", d['Candidate'][2]["ID"])
            Candidate_3.innerText = d['Candidate'][3]["CN"]
            Candidate_3.setAttribute("value", d['Candidate'][3]["ID"])
            console.log(d)
            currentAnswer = d['WORD_ID']

        },
        error: function () {
            alert("error");
        }
    })
}
$(document).ready(function () {
    ajax.getNextWord();
})

$(".candidate_btn").click(function () {
    console.log(this.value, currentAnswer)

    if (parseInt(this.value) === currentAnswer) {
        ajax.getNextWord();
    } else {
        $(this).removeClass("btn-primary");
        $(this).addClass("btn-danger")
        console.log("wrong")
        console.log(this.value);
    }

})

