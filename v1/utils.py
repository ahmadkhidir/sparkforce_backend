from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


def hash_words(word):
    return make_password(word).replace('/','')[21:-1]

def courses_image_path(instance, filename: str):
    *name, ext = filename.replace(' ', '').split('.')
    name = ''.join(name)
    return f"images/courses/{hash_words(name)}.{ext}"

def opportunities_image_path(instance, filename: str):
    *name, ext = filename.replace(' ', '').split('.')
    name = ''.join(name)
    return f"images/opportunities/{hash_words(name)}.{ext}"

def validate_rate(value):
        if (value > 5):
            raise ValidationError('Rate cannot be greater than 5')