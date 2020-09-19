from django import template

register = template.Library()


@register.filter(name='stars')
def stars(number):
    starList = ["star"] * int(number)
    if number > int(number):
        starList.append("star_half")
    starList += ["star_outline"] * (5 - len(starList))
    return starList

