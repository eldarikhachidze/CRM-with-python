from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Custom template filter to retrieve a value from a dictionary by key."""
    return dictionary.get(key, None)