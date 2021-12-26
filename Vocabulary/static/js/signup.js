function SignUpFn() {
    console.log({
        username: $('#username').val(),
        password: $('#password').val()
    })
    let username = $('#username').val()
    let password = $('#password').val()
    let repassword = $('#re_password').val()
    if (!username || !password) {
        alert("用户名或密码为空");
        return 0;
    }

    if (password !== repassword) {
        alert("两次密码不一致");
        return 0;
    }


    $.ajax({
        url: '/login/signup',
        method: 'POST',
        data: {
            "username": $('#username').val(),
            "password": $('#password').val()
        },
        success: function (res) {
            // 成功
            if (res["state"] > 0) {
                alert("注册成功")
                window.location.replace("/")
            } else {
                alert("注册失败，用户名已存在")
            }
            console.log(res)
        },
        error: function (err) {
            console.log(err)
        }
    })
}