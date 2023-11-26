from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contacts/contacts.html"
    success_url = "/contacts/success"


class SuccessView(TemplateView):
    template_name = "contacts/success.html"
