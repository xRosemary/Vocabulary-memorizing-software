let word_str = document.getElementById("word_str");
let phon_str = document.getElementById("phon_str");
let Candidate_0 = document.getElementById("Candidate_0");
let Candidate_1 = document.getElementById("Candidate_1");
let Candidate_2 = document.getElementById("Candidate_2");
let Candidate_3 = document.getElementById("Candidate_3");

const right_audio = new Audio("/static/audio/right.mp3")
const wrong_audio = new Audio("/static/audio/wrong.mp3")

let ajax = {};
let id_list = []
let score_list = []

let currentScore = 0

let currentWordNum = 0
let totalNum = 0

$(document).ready(function () {
    ajax.getWordList();
})
ajax.getWordList = function () {
    $.ajax({
        type: "post",
        url: "/req/getWordList",
        success: function (d) {
            console.log(d)
            let wordlist = JSON.stringify(d["result"])
            sessionStorage.setItem("wordlist", wordlist)
            totalNum = JSON.stringify(d["total"])

            getNextWord()
        },
        error: function () {
            alert("error");
        }
    })
}
ajax.summitSocre = function () {
    console.log(JSON.stringify(id_list))
    console.log(JSON.stringify(score_list))
    $.ajax({
        type: "post",
        url: "/req/summitScore",
        data: {"id_list": JSON.stringify(id_list), "score_list": JSON.stringify(score_list)},
        success: function () {
            alert("本次学习完成");
            location.href = "index"

        },
        error: function () {
            alert("error");
        }
    })
}

function getNextWord() {
    // 恢复默认样式
    $("#Candidate_0").removeClass("btn-danger");
    $("#Candidate_0").addClass("btn-primary");
    $("#Candidate_1").removeClass("btn-danger");
    $("#Candidate_1").addClass("btn-primary");
    $("#Candidate_2").removeClass("btn-danger");
    $("#Candidate_2").addClass("btn-primary");
    $("#Candidate_3").removeClass("btn-danger");
    $("#Candidate_3").addClass("btn-primary");

    let wordlist = JSON.parse(sessionStorage.getItem("wordlist"))
    let audio = new Audio(wordlist[currentWordNum]["PHONETIC"])

    audio.play()


    word_str.innerText = wordlist[currentWordNum]["WORD"]
    phon_str.innerText = wordlist[currentWordNum]["PRONOUNCE"]
    Candidate_0.innerText = wordlist[currentWordNum]["Candidate"][0]["str"]
    Candidate_0.setAttribute("value", wordlist[currentWordNum]["Candidate"][0]["id"])
    Candidate_1.innerText = wordlist[currentWordNum]["Candidate"][1]["str"]
    Candidate_1.setAttribute("value", wordlist[currentWordNum]["Candidate"][1]["id"])
    Candidate_2.innerText = wordlist[currentWordNum]["Candidate"][2]["str"]
    Candidate_2.setAttribute("value", wordlist[currentWordNum]["Candidate"][2]["id"])
    Candidate_3.innerText = wordlist[currentWordNum]["Candidate"][3]["str"]
    Candidate_3.setAttribute("value", wordlist[currentWordNum]["Candidate"][3]["id"])


}

$(".candidate_btn").click(function () {
    let wordlist = JSON.parse(sessionStorage.getItem("wordlist"))
    let currentAnswer = wordlist[currentWordNum]["ID"]
    console.log(this.value, currentAnswer)

    if (parseInt(this.value) === currentAnswer) {
        if (currentWordNum === parseInt(totalNum) - 1) {
            ajax.summitSocre();
            return
        }
        id_list.push(currentAnswer)
        score_list.push(currentScore)
        currentScore = 0
        right_audio.play()
        console.log("right")

        currentWordNum += 1;
        getNextWord();
    } else {
        $(this).removeClass("btn-primary");
        $(this).addClass("btn-danger")
        currentScore -= 1
        wrong_audio.currentTime = 0;
        wrong_audio.play()
        console.log("wrong")
        console.log(this.value);
        console.log(currentScore);
    }

})

