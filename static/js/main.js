let word_list = []


$("#input_box .btn").click(function (e) {
    word_list = $("#input_area").val();

    $.ajax({
        type: "post",
        url: "/req/setWordList",
        data: {"wordlist": word_list},
        success: function (d) {
            // alert("success");
        },
        error: function () {
            alert("error");
        }
    })

    location.href = "learn"
})
