from django.forms import ModelForm
from .models import *
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
       