from django import template

register = template.Library()


def add_class(field, css):
    try:
        return field.as_widget(attrs={"class": css})
    except AttributeError:
        return field
