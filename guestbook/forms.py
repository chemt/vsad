from django.forms import ModelForm
from math_captcha.forms import MathCaptchaModelForm
from models import GuestBook


class GuestbookForm(MathCaptchaModelForm):
    class Meta:
        model = GuestBook
