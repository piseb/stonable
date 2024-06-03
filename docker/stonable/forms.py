from django.forms import ModelForm
from .models import Entite


class EntiteForm(ModelForm):
    class Meta:
        model = Entite
        localized_fields = ["date_naissance"]
        fields = [
            "nom",
            "prenom",
            "adresse",
            "code_postal",
            "ville",
            "telephone_fixe",
            "telephone_portable",
            "email",
            "date_naissance",
            "note",
        ]
