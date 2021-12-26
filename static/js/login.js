let tips_DOM = $("#login_tip")

function loginFn() {
    console.log({
        username: $('#username').val(),
        password: $('#password').val()
    })

    $.ajax({
        url: '/login',
        method: 'POST',
        data: {
            "username": $('#username').val(),
            "password": $('#password').val()
        },
        success: function (res) {
            // 成功
            if (res["state"] < 0) {
                console.log("denglu shibai")
                alert("用户名或密码错误")
            } else {
                alert("登录成功")
                window.location.replace("/index")
            }
            console.log(res)
        },
        error: function (err) {

            console.log(err)
        }
    })
}