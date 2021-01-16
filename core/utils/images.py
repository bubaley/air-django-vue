import secrets
import base64

from django.core.files.base import ContentFile
from rest_framework.exceptions import ValidationError


def str_is_base64(image_str):
    return ';base64' in image_str


def base64_to_file(image):
    try:
        format, imgstr = image.split(';base64,')
        ext = format.split('/')[-1]
        file = ContentFile(base64.b64decode(imgstr), name=secrets.token_urlsafe(16) + '.' + ext)
        return file
    except ValueError:
        raise ValidationError('Incorrect base64.')
