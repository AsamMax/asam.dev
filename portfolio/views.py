from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.


def portfolio(request):
    return render(request, 'about_me.html', {})


def cv(request):
    context = {
        "experience": [{
            "name": "Ausbildung zum Fachinformatiker (Anwendungsentwicklung)",
            "place": "SEWOBE AG",
            "placeLink": "https://sewobe.de",
            "time": "August 2017 - Juli 2020",
            "bullets": ["Anpassung und Erweiterung von modularer Cloud-Software",
                        "Verwaltung relationeler Datenbanken",
                        "Entwurf und Umsetzung inovativer Kundenwebseiten (Wordpress)",
                        "Einarbeitung neuer Entwickler",
                        "Individuelle Beratung und Betreuung von Klienten",
                        "Agile Softwareentwicklung",
                        ]
        }, {
            "name": "Praktikum Elektro- und Metaltechnik",
            "place": "IHK Akademie Schwaben",
            "time": "Semptember 2015 - Juli 2016",
            "placeLink": "https://www.ihk-akademie-schwaben.de/",
            "bullets": [
                "Umgang mit CNC-Fräsen und -Drehmaschienen",
                "Aufbau zweckgebundener Platinen",
                "Optimierung von Schaltplänen für Microcontroller",
            ]
        }, {
            "name": "Praktikum Fachinformatiker",
            "place": "XITASO GmbH",
            "time": "März 2013",
            "placeLink": "https://xitaso.com/",
            "bullets": [
                "Erste Grundlagen und Kentnisse im Bereich der angewandten Informatik",
                "Konfiguration von Netzwerkdiensten",
            ]
        }],
        "education": [{
            "name": "Ausbildung zum Anwendungsentwicker",
            "place": "Berufsschule 7 Augsburg",
            "time": "August 2017 - Juli 2020",
            "at": "an der",
            "bullets": [
                "Abschlussprüfungsschnitt: 94 von 100 Punkten (entspricht ca. 1,2)",
            ]
        }, {
            "name": "Fachabitur (Technik)",
            "place": "Fachoberschule Augsburg",
            "time": "Semptember 2015 - Juli 2017",
            "at": "an der"
        }, {
            "name": "Bertolt-Brecht-Realschule",
            "place": "Augsburg",
            "time": "Januar 2014 - Juli 2015",
            "at": "in"
        }, {
            "name": "Jakob-Fugger-Gymnasium",
            "place": "Augsburg",
            "time": "Semptember 2008 - Januar 2014",
            "at": "in"
        }],
        "skills": [
            {"name": "HTML", "stars": 5, },
            {"name": "CSS", "stars": 5, },
            {"name": "JavaScript", "stars": 5, },
            {"name": "TypeScript", "stars": 3, },
            {"name": "PHP", "stars": 5, },
            {"name": "Python", "stars": 3.5, },
            {"name": "SASS/SCSS", "stars": 3.5, },
            {"name": "Java", "stars": 2.5, },
            {"name": "C++", "stars": 2, },
            {"name": "SQL", "stars": 5, }
        ],
        "frameworks": [
            {"name": "Bootstrap", "stars": 4, },
            {"name": "JQuery", "stars": 4.5, },
            {"name": "Angular", "stars": 2.5, },
            {"name": "React", "stars": 2, },
            {"name": "Electron", "stars": 1.5, },
        ],
        "languages": [
            {"name": "Deutsch", "stars": 5, },
            {"name": "Englisch", "stars": 4.5, },
        ],
        "personal": {
            "Stärken": ["Analytisches Denkvermögen", "Teamfähigkeit", "Kompromissbereitschaft", "Flexibilität",
                        "Konfliktfähigkeit", "Kommunikationsfähigkeit", "Empathie",
                        "Qualitätsbewusstsein",  "Ergebnisorientierung"],
            #            "Interessen": ["Programmieren", "Sport"]
        }
    }
    return render(request, 'cv.html', context)

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.Post)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = ['max@asam.dev']

            send_mail("von " + name + " via asam.dev: " +
                      subject, message, sender, recipients)
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
