function startLoad() {
    document.getElementById("loader").classList.add("done");
    addFadeOut();

    document.getElementById("sideNav").addEventListener("click", function () {
        document.getElementById("sideNav").classList.toggle("show");
    })

    console.log("hello1");
    swipeEvent(document.getElementById("sideNav"),
        {
            "left": function () {
                document.getElementById("sideNav").classList.remove("show");
            }, "right": function () {
                document.getElementById("sideNav").classList.add("show");
            }
        }
    )
}

function swipeEvent(gesuredZone, callbacks) {
    console.log("hello2");
    var touchstartX = 0;
    var touchstartY = 0;
    var touchendX = 0;
    var touchendY = 0;

    gesuredZone.addEventListener('touchstart', function (event) {
        touchstartX = event.changedTouches[0].screenX;
        touchstartY = event.changedTouches[0].screenY;
    }, false);

    gesuredZone.addEventListener('touchend', function (event) {
        touchendX = event.changedTouches[0].screenX;
        touchendY = event.changedTouches[0].screenY;
        handleGesure();
    }, false);

    function handleGesure() {
        console.log("hello3");
        if (touchendX < touchstartX) {
            callbacks["left"]();
        }
        if (touchendX > touchstartX) {
            callbacks["right"]();
        }
        if (touchendY < touchstartY) {
            callbacks["down"]();
        }
        if (touchendY > touchstartY) {
            callbacks["up"]();
        }
        if (touchendY == touchstartY) {
            callbacks["tap"]();
        }
    }
}

function addFadeOut() {
    if (!window.AnimationEvent) { return }

    var anchors = document.getElementsByTagName('a');

    for (var idx = 0; idx < anchors.length; idx += 1) {

        if (anchors[idx].hostname !== window.location.hostname) {
            continue;
        }

        anchors[idx].addEventListener('click', function (event) {

            var fader = document.getElementById('loader'),
                anchor = event.currentTarget;

            event.preventDefault();
            fader.classList.remove('done');

            setTimeout(function () {
                window.location = anchor.href;
            }, 1050)
        });
    }

}

function toggleColorMode() {
    document.body.classList.toggle('light_mode');

    if (document.body.classList.contains('light_mode')) {
        document.cookie = "colorMode=1"
    } else {
        document.cookie = "colorMode=0"
    }
}

function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
            end = dc.length;
        }
    }
    // because unescape has been deprecated, replaced with decodeURI
    //return unescape(dc.substring(begin + prefix.length, end));
    return decodeURI(dc.substring(begin + prefix.length, end));
} 