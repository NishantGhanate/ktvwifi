from django import template
from django.template.defaultfilters import linebreaksbr, urlize
from ..models import Complaint , Contact

register = template.Library()

@register.simple_tag
def number_of_complaints(request):
    count = Complaint.objects.filter(status='p').count()
    return count

@register.simple_tag
def number_of_contacts(request):
    count = Contact.objects.filter(status='p').count()
    return count