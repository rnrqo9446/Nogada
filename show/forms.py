from django import forms
from .models import Musical_Comment, Exhibition_Comment, Concert_Comment, Classic_Comment

class Musical_CommentForm(forms.ModelForm):
    class Meta:
        model = Musical_Comment
        fields = {'nickname', 'text'}

class Exhibition_CommentForm(forms.ModelForm):
    class Meta:
        model = Exhibition_Comment
        fields = {'nickname', 'text'}


class Concert_CommentForm(forms.ModelForm):
    class Meta:
        model = Concert_Comment
        fields = {'nickname', 'text'}

class Classic_CommentForm(forms.ModelForm):
    class Meta:
        model = Classic_Comment
        fields = {'nickname', 'text'}

