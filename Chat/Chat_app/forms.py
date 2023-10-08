from django import forms

from Chat_app.models import Message


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'size': '40'}),  # Устанавливает ширину поля
        }