from django.forms import ModelForm
from models import GuestBook

class GuestbookForm(ModelForm):
    class Meta:
        model = GuestBook
