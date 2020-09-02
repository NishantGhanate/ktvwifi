from django.contrib import admin

# Register your models here.
from .models import InternetPlans , Contact , Customer , Complaint , Faq

admin.site.register(InternetPlans)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Complaint)
admin.site.register(Faq)