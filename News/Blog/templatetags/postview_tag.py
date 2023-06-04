from django import template

from Blog.models import *

register = template.Library()
@register.simple_tag()
def get_posts():
    return Post.objects.all()
@register.simple_tag()
def get_profile(num):
    return Profile.objects.get(user__pk=num).pk
@register.simple_tag()
def get_first_post():
    return Post.objects.first()
@register.simple_tag()
def get_last_post():
    return Post.objects.last()
@register.simple_tag()
def get_category():
    return Category.objects.all()

@register.simple_tag()
def get_social():
    return Social.objects.all()
@register.simple_tag()
def strong_text(text, words):
    words = words.split()
    for word in words:
        text = text.lower().replace(word.lower(), f"<strong>{word.lower()}</strong>")
    return text

