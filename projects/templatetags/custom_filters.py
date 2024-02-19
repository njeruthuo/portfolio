# your_app/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter
def truncate_sentence(value, max_length):
    words = value.split(' ')
    truncated_words = ' '.join(words[:max_length])
    return truncated_words + ('...' if len(words) > max_length else '')
