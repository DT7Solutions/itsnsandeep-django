from django.contrib import messages
from django.shortcuts import render
from .models import Blogs,Contact,Banner
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail

# Create your views here.



def index(request):
    oBlogs = Blogs.objects.all()[:3]
    oBanner = Banner.objects.first()

    #Contact 
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        message = request.POST.get('message',"")
        
        oContactinfo = Contact(Name=name,Email=email,Message=message)
        oContactinfo.save()
    
        sucess =f'hi {name} sucessfully Sending email'
        subject = ''
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplayitsnsandeep@gmail.com',recipient_list=['admin@itsnsandeep.com']) 
            messages.success(request,sucess)
            print(messages)
        except:
            messages.error(request,'your emails sending fail')
    return render(request, 'uifiles/index.html',{'oBlogs':oBlogs,'oBanner':oBanner})


def blogs(request):
    blog_items =Blogs.objects.all()
    paginator = Paginator( blog_items, 3) 

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post = paginator.page(paginator.num_pages)
    
    return render(request,'uifiles/blogs.html',{'blog_items':blog_items,'page':page})

def blog_details(request,slug):
    blog_posts = Blogs.objects.get(Sluglink=slug)
    return render(request,'uifiles/blog-single.html',{'blog_posts':blog_posts})

def ceo_and_business_personal_branding(request):
    return render(request, 'uifiles/ceo-and-business-owner-personal-branding.html')

def celebprenenur_transformation(request):
    return render(request, 'uifiles/celebprenenur-transformation.html')

def educational_institutions(request):
    return render(request, 'uifiles/educational-institutions.html')

def corporate_solutions_personal_branding(request):
    return render(request, 'uifiles/corporate-solutions-personal-branding-mastery-workshops-for-corporate-success.html')
