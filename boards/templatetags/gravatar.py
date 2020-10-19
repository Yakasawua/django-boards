import hashlib
from urllib.parse import urlencode
from django.utils.safestring import mark_safe

from django import template
from django.conf import settings

register = template.Library()

@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default='https://pm1.narvii.com/6323/b68234d2b49aeb2cbf1f9b7c6ab86018f02dfee7_hq.jpg'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url