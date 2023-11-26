from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            "name": "Имя:",
            "mail": "Эл.почта:",
            "phone_number": "Телефон:",
            "message": "Добавьте сообщение:",
        }
        error_messages = {
            "name": {
                "max_length": "Слишком много символов",
                "required": "Укажите хотя бы один символ",
            },
            "mail": {
                "required": "Укажите почту",
            },
            "phone_number": {
                "max_length": "Слишком много символов",
                "min_length": "Слишком мало символов",
                "required": "Укажите номер телефона",
            },
        }
