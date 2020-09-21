function startLoad() {
    document.addEventListener('DOMContentLoaded', function () {
        document.getElementById("loader").classList.add("done");
        addFadeOut();

        document.getElementById("sideNav").addEventListener("click", function(){
            document.getElementById("sideNav").classList.toggle("show");
        })
    })

    window.addEventListener('pageshow', function (event) {
        if (!event.persisted) {
            return;
        }
        var fader = document.getElementById('fader');
        fader.classList.remove('fade-in');
    });
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
            }, 1010)
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