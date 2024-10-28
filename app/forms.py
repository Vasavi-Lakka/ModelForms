from django import forms

from app.models import *

class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields="__all__"

class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        # fields=['topic_name', 'name']
        #exclude=['url']
        help_texts={'topic_name':'shouldnot be num'}
        labels={'topic_name':'TN'}
        widgets={'url':forms.PasswordInput}
# class AccessModelForm(forms.ModelForm):
#     class Meta:
#         model=AccessRecord
#         fields="__all__"
