from django import forms
from django_jsonform.widgets import JSONFormWidget
from .models import *

class AddScenarioForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ('name', 'status', 'test_body', 'last_update_user')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'test_body': JSONFormWidget(schema=TestCase.SCENARIO_SCHEMA_JSON, validate_on_submit=True),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=SCENARIO_STATUS)
        }


class AddFeatureForm(forms.ModelForm):
    class Meta:
        model = FeatureTest
        fields = ('level', 'name', 'slug')
        widgets = {
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']






