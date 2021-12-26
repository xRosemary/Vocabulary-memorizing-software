var stars = document.getElementById('stars')

// js随机生成流星
for (var j = 0; j < 100; j++) {
    var newStar = document.createElement("div")
    newStar.className = "star"
    newStar.style.top = randomDistance(-100, -1000) + 'px'
    newStar.style.left = randomDistance(1980, 100) + 'px'
    stars.appendChild(newStar)
}

// 封装随机数方法
function randomDistance(max, min) {
    var distance = Math.floor(Math.random() * (max - min + 1) + min)
    return distance
}

var star = document.getElementsByClassName('star')

// 给流星添加动画延时
for (var i = 0, len = star.length; i < len; i++) {
    star[i].style.animationDelay = i % 6 == 0 ? '0s' : i * 0.8 + 's'
}