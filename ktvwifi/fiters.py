import django_filters
from django.contrib.auth.models import Group , User
from .models import *

class InternetPlansFilter(django_filters.FilterSet):
    class Meta:
        model = InternetPlans
        fields = ['speed','price','validity']

class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['name','phone','email']

class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = '__all__'

class ComplaintFilter(django_filters.FilterSet):
    class Meta:
        model = Complaint
        fields = ['user']

class FaqFilter(django_filters.FilterSet):
    class Meta:
        model = Faq
        fields = ['title','solution']

