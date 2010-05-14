from django.forms import ModelForm
from math_captcha.forms import MathCaptchaModelForm

from models import Zayavka, ZayavkaHotel


class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka

class ZayavkaHotelForm(MathCaptchaModelForm):
    class Meta:
        model = ZayavkaHotel