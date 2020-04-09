from django.forms import ModelForm
from shows.models import Type

# Create the form class.
class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'