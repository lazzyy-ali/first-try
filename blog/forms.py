from django import forms
from blog.models import Comments
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['name', 'email', 'subject', 'message']