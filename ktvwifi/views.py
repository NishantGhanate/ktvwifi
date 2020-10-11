from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import Group , User

from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core import serializers

from .decoraters  import unauthenticatedUser ,  allowed_user , admin_only
from .models import *
from .forms import *
from .fiters import *

# Create your views here.
def homePage(request):
    if request.user.is_authenticated :
        complaintsCount = Complaint.objects.filter(user=request.user).count()
        rechargesCount = 1
        context = {'complaintsCount':complaintsCount , 'rechargesCount':rechargesCount}
        return render(request,'ktvwifi/userDashboard/userHome.html',context )
    return render(request,'ktvwifi/home.html' )

def features(request):
    context = {}
    return render(request, 'ktvwifi/features.html' , context)

def pricing(request):
    # context : rtype - dict
    plans =  InternetPlans.objects.all()
    paginator = Paginator(plans, 12)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # filter = InternetPlansFilter(request.GET,queryset=plans)
    # posts = filter.qs
   
    return render(request, 'ktvwifi/plans.html', {'page':page,'plans':posts ,'filter':filter})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def contactus(request):
    form = ContactForm()
    ip = get_client_ip(request)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('homePage')
        return render(request,'ktvwifi/contactus.html' , {'form': form , 'ip' : ip} ) 
    elif request.method == 'POST':
        updated_data = request.POST.copy()
        updated_data.update({'ip': ip}) 
        form = ContactForm(data=updated_data) 
        if form.is_valid():
            form.save()
            msg = 'Thank you for contacting us. We will email you at ' +  form.cleaned_data['email']
            context = {'thanks': msg}
            return render(request,'ktvwifi/thanks.html' , context )
            
        else:
            return render(request, 'ktvwifi/contactus.html', {'form': form})

def faq(request):
    faqList =  Faq.objects.all()
    paginator = Paginator(faqList, 10)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # filter = InternetPlansFilter(request.GET,queryset=plans)
    # posts = filter.qs
    return render(request, 'ktvwifi/faq.html', {'page':page,'posts':posts})

   
@unauthenticatedUser
def signupPage(request):
    form = CreateUserForm()
    context = {'form' : form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            userSigned = form.save(commit=True)
            group = Group.objects.get(name='customer')
            username = form.cleaned_data['username']
            userSigned.groups.add(group)
            customer = Customer()
            customer.user = userSigned
            customer.phone = ''
            customer.address = ''
            customer.save()

            # userSigned.is_active =False
            # userSigned.save()
            # emailSubject = 'Activate Your acount'
            # emailBody = 'Email Body '
            # userEmail = form.cleaned_data['email']
            # email = EmailMessage(
            # emailSubject,
            # emailBody,
            # 'noreply@ktvwifi.com',
            # [userEmail],
            # )
            # email.send(fail_silently=False)
            messages.success(request,'Account created for ' + username)
            return redirect('loginPage')
        else:
            messages.error(request,form.errors)
            return render(request,'ktvwifi/signup.html' , context )

    return render(request,'ktvwifi/signup.html' , context )

@unauthenticatedUser
def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=username, password=pwd)
        if user is not None :
            login(request,user)
            if request.user.is_authenticated:
                usergroup = request.user.groups.values_list('name', flat=True).first()
                if usergroup == "customer":
                   return redirect('homePage')
                elif usergroup == "admin":
                    return redirect('dashboard')
        elif username is not None and pwd is not None:
            # messages.error(request,'Username or password incorrect')
            context = {'errorMessages' : 'Username or password incorrect'}
            return render(request,'ktvwifi/login.html' , context )
    elif request.method == 'GET':
        return render(request,'ktvwifi/login.html' , context )

def logoutUser(request):
    logout(request)
    return redirect('home')

# User panel 
@login_required(login_url='loginPage')
def userComplaints(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-date_created')
    paginator = Paginator(complaints, 9)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    form = ComplaintForm()
    context = {'page':page,'complaints':posts ,'form':form}
    if request.method == 'POST':
        updated_data = request.POST.copy()
        updated_data.update({'status': ('p')}) 
        form = ComplaintForm(data=updated_data)     
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('userComplaints')
        else:
            context = {'page':page,'complaints':posts ,'form':form}
            render(request,'ktvwifi/userDashboard/userComplaints.html' , context  ) 
        
    return render(request,'ktvwifi/userDashboard/userComplaints.html' , context) 


@login_required(login_url='loginPage')
def userSettings(request):
    try :
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('/')
    context = {'user': request.user , 'customer' : customer}
    if request.is_ajax and request.method == "POST":
        # get the form data
        cform = CustomerForm(request.POST)
        # save the data and after fetch the object in instance
        if cform.is_valid():
            instance = cform.save(commit=False)
            customer = Customer.objects.filter(user=request.user).update(
            phone = cform.cleaned_data['phone'] , 
            address = cform.cleaned_data['address']
            )
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance})
            
        else:
            ## some form errors occured.
            return JsonResponse({"error": cform.errors} )
    return render(request,'ktvwifi/userDashboard/userSettings.html' , context )


# Admin/Staff panel 
@login_required(login_url='loginPage')
@admin_only
def adminHome(request):
    context = {}
    return render(request,'ktvwifi/staffDashboard/home.html' , context )
      
@login_required(login_url='loginPage')
@admin_only
def adminCustomers(request):
    users_all = User.objects.filter(groups__name='customer')
    paginator = Paginator(users_all, 10)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
 
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    myfilter = UsersFilter(request.GET , queryset=users_all)
    users = myfilter.qs
    comtext =  {'page':page,'users':users , 'myfilter':myfilter} 
    return render(request,'ktvwifi/staffDashboard/customers.html' , comtext)

@login_required(login_url='loginPage')
@admin_only
def adminComplaints(request):
    if request.method == 'POST':
        # complaint id , status , solution 
        c = Complaint.objects.get(complaint_id=request.POST['complaint_id'])
        c.status = request.POST['status']  
        c.solution = request.POST['solution'] 
        c.save() 
        return redirect('complaints')

    complaints_all = Complaint.objects.all().order_by('-date_created')
    myfilter = ComplaintFilter(request.GET , queryset=complaints_all)
    paginator = Paginator( myfilter.qs, 7)
    page = request.GET.get('page', 1)
    try:
        complaints = paginator.page(page)
    except PageNotAnInteger:
        complaints = paginator.page(1)
 
    except EmptyPage:
        complaints = paginator.page(paginator.num_pages)
   

    # for status dropdown menu
    form= ComplaintForm()
    comtext = {'page':page,'complaints':complaints ,'form':form , 'myfilter':myfilter}
    return render(request,'ktvwifi/staffDashboard/complaints.html' , comtext)

@login_required(login_url='loginPage')
@admin_only
def adminContact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        response = request.POST.get('response')
        contact = Contact.objects.get(pk=contact_id)
        contact.response = response
        contact.status = ('c')
        contact.save()
        sendEmail(contact.email , contact.title , response)
        return redirect('contacts')

    contacts_all = Contact.objects.all().order_by('-date_created')
    myfilter = ContactFilter(request.GET , queryset=contacts_all)
    paginator = Paginator(myfilter.qs, 9)
    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    context = {'contacts' : contacts , 'myfilter':myfilter}
    return render(request,'ktvwifi/staffDashboard/contact.html' , context)

def sendEmail(userEmail,emailSubject,emailBody):
    email = EmailMessage(
            emailSubject,
            emailBody,
            'noreply@ktvwifi.com',
            [userEmail],
            )
    email.send(fail_silently=False)
    

@login_required(login_url='loginPage')
@admin_only
def adminPlans(request): 
    plans_all =  InternetPlans.objects.all().order_by('-date_created')
    myfilter = InternetPlansFilter(request.GET , queryset=plans_all)
    paginator  = Paginator( myfilter.qs, 7)
    page = request.GET.get('page', 1)
    try:
        plans = paginator.page(page)
    except PageNotAnInteger:
        plans = paginator.page(1)
    except EmptyPage:
        plans = paginator.page(paginator.num_pages)
    context = {'plans':plans ,'page':page}
    if request.method == 'POST':
        form = InternetPlansForm(request.POST,files=request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            if not request.POST['id']:
                p.save()
            else:
                plans = InternetPlans.objects.get(id=request.POST['id'])
                if p.image:
                    plans.image = p.image
                plans.speed = p.speed
                plans.price = p.price
                plans.validity = p.validity
                plans.message = p.message
                plans.save()
            return redirect('plans')
        else:
            ## some form errors occured.
            context = {'plans':plans , 'error': form.errors , 'page':page}
            render(request,'ktvwifi/staffDashboard/internetplans.html' , context)

    return render(request,'ktvwifi/staffDashboard/internetplans.html' , context)

@login_required(login_url='loginPage')
@admin_only
def adminPlansDelete(request):
    if request.method == 'POST':
        result = InternetPlans.objects.get(id = request.POST.get('id'))
        if result:
            result.delete()
            return redirect('plans')
        else:
            return redirect('plans')

@login_required(login_url='loginPage')
@admin_only
def adminFaq(request):
    faqList =  Faq.objects.all().order_by('-date_created')
    myfilter = InternetPlansFilter(request.GET,queryset=faqList)
    paginator = Paginator(myfilter.qs, 9)
    page = request.GET.get('page', 1)
    try:
        faq = paginator.page(page)
    except PageNotAnInteger:
        faq = paginator.page(1)
 
    except EmptyPage:
        faq = paginator.page(paginator.num_pages)
    
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            if not request.POST['id']:
                p.save()
            else:
                f = Faq.objects.get(id=request.POST.get('id'))
                f.title = p.title
                f.solution = p.solution
                f.save()
            return redirect('faq')
        else:
            ## some form errors occured.
            context = {'faq':faq , 'error': form.errors , 'page':page}
            render(request,'ktvwifi/staffDashboard/faq.html' , context)

    return render(request, 'ktvwifi/staffDashboard/faq.html', {'page':page,'faq':faq})

@login_required(login_url='loginPage')
@admin_only
def adminFaqDelete(request):
    if request.method == 'POST':
        result = Faq.objects.get(id = request.POST.get('id'))
        if result:
            result.delete()
            return redirect('faq')
        else:
            return redirect('faq')