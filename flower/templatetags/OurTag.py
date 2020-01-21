from django import template

register = template.Library()


@register.filter()
def limit_4(obj):
    return obj[:4]
