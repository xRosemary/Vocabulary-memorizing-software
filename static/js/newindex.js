let word_list = ["aaa"]


$("#start").click(function (e) {
    word_list = $("#input_area").val();

    location.href = "learn"
})
