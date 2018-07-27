

from django import forms
from polls.models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, PrependedAppendedText, InlineRadios, FormActions
from bootstrap_datepicker_plus import DatePickerInput



class PForm(forms.ModelForm):

    to_do = 'To-Do'
    in_progress = 'In Progress'
    blocked = 'Blocked'
    done = 'Done'
    dismissed = 'Dismissed'
    STATUSES = (
        (to_do, 'To Do'),
        (in_progress, 'In Progress'),
        (blocked, 'Blocked'),
        (done, 'Done'),
        (dismissed, 'Dismissed')
     )


    project = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form control',
        'placeholder':'Give your project a name'
        }
    ))

    # description = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #     attrs={
    #     'class': 'form control',
    #     'placeholder':'Please add a detailed description for your project',
    #
    #     }
    # ))
    # resolution = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #     attrs={
    #     'class': 'form control',
    #     'placeholder':'If you have a preferred resolution for your project please detail it here.'
    #     }
    # ))
    # startdate = forms.DateField(
    #     widget=DatePickerInput(format='%m/%d/%Y')
    # )




    status = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=STATUSES,)
    # startdate = forms.DateField(
    #     required=False,
    #     widget=forms.DateInput(
    #     attrs={
    #     'placeholder' : 'please format start date like this 12/1/2018'
    #     }
    # ))

    # deadline = forms.DateField(
    #     required=False,
    #     widget=forms.DateInput(
    #     attrs={
    #     'placeholder' : 'please format deadline date like this 12/1/2018'
    #     }
    # ))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create Project'))
        #self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-default'))
        self.helper.form_tag = False
        self.helper.layout = Layout(
     HTML("""
    <p>Please answer a few questions to  <strong>get started</strong></p>
"""),

            Field('project'),
        #      HTML("""
        #     <p>Please add a name for your project <strong>make if unique</strong></p>
        # """),
            Field('description', placeholder ='Please add a detailed description for your project'),
            #      HTML("""
            #     <p>Please add a detailed description for your project</p>
            # """),
            Field('resolution', placeholder='If you have a preferred resolution for your project please detail it here.'),
            #      HTML("""
            #     <p>If you have a preferred resolution for your project please detail it here.</p>
            # """),
            Field('startdate',placeholder='please format startdate date like this 12/1/2018'),
            Field('deadline', placeholder="please format deadline date like this 12/1/2018"),

            PrependedAppendedText('budget', '$', '.00',  css_class='input-sm'),
            InlineRadios('status'),
            #Submit('Submit', 'Submit', css_class="btn-success"),
        )


    class Meta:
        model = Project
        fields = ('project','description','resolution','startdate','deadline', 'budget', 'status')
        widgets = {
            'startdate': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'deadline': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }
