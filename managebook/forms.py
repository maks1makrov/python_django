from django.forms import ModelForm, TextInput

from managebook.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            'text': TextInput(attrs={'class': "form-control"})
        }
