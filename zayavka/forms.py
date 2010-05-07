from django.forms import ModelForm
from models import Zayavka

class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
