from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
        )

    class Meta:
        model = User
        fields = ['name']


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            Field('resolution'),
            Field('startdate'),
            Field('deadline'),
            Field('user'),
            Field('state'),
            Field('priority'),
            Field('created_by'),
            Field('created_at'),
            Field('last_modified'),
            Field('pub_date'),
            Submit('update', 'Update', css_class="btn-success"),
        )

    class Meta:
        model = models.Project
        fields = ['title','description','resolution','startdate','deadline','user','state', 'priority','pub_date']
