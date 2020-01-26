from django import template

register = template.Library()


@register.filter()
def limit_4(obj):
    return obj[:4]

@register.filter()
def limit_2(obj):
    return obj[:2]