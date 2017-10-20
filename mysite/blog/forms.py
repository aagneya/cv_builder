from django import forms

from .models import Resume

class Resumeform(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('name','address1','address2','obj','image','school','UG','PG','skills','cell','email','expone','expfrom','expto','exptwo',)
