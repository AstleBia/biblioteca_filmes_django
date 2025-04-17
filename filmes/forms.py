from django.forms import ModelForm
from .models import Filme

class FormFilme(ModelForm):
    class Meta:
        model = Filme
        fields = ["titulo","nota","review"]
