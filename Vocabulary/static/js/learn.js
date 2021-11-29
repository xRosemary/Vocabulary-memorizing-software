let word_str = document.getElementById("word_str");
let Candidate_0 = document.getElementById("Candidate_0");
let Candidate_1 = document.getElementById("Candidate_1");
let Candidate_2 = document.getElementById("Candidate_2");
let Candidate_3 = document.getElementById("Candidate_3");

//假定不为空

$(document).ready(function () {
    word_str.innerText = "abandon"
    Candidate_0.innerText = "aaa"
    Candidate_1.innerText = "bbb"
    Candidate_2.innerText = "ccc"
    Candidate_3.innerText = "ddd"
})

$(".candidate_btn").click(function (e) {
    $.ajax({
        type: "post",
        url: "/req/getNextWord",
        // data: {"name": "test"},
        success: function (d) {
            word_str.innerText = d['WORD']
            Candidate_0.innerText = d['Candidate'][0]
            Candidate_1.innerText = d['Candidate'][1]
            Candidate_2.innerText = d['Candidate'][2]
            Candidate_3.innerText = d['Candidate'][3]
        },
        error: function () {
            alert("error");
        }
    })
})

