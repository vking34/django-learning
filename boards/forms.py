from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': "What is on your mind?"}
        ),
        max_length=3500,
        help_text='The max length of the text is 3500'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
