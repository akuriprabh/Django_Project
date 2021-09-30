from django.shortcuts import render,get_object_or_404
from garments.models import FormalShirt
from garments.models import CasualShirt
from garments.models import TShirt
from garments.models import TrousersBottomWear
from garments.models import JeansBottomWear
from garments.models import CargoBottomWear
from django.db.models import Q
from django.contrib import messages
from garments.forms import ContactForm
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail



# Create your views here.
def index (request):
    return render(request,'index.html')

def aboutus (request):
    return render(request,'aboutus.html')

def contactus (request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        content = request.POST.get('content')
        subject = 'Hello from mygarmentsshop.com'
        from_email = settings.EMAIL_HOST_USER
        user_email = email
        to_list = [user_email,from_email]
        send_mail(subject,content,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request,'contactus.html',{'form':form})

def formalshirts (request):
    lst=FormalShirt.objects.all()
    return render(request,'formalshirts.html',{'lst':lst})

def casualshirts (request):
    lst=CasualShirt.objects.all()
    return render(request,'casualshirts.html',{'lst':lst})

def tshirts (request):
    lst=TShirt.objects.all()
    return render(request,'tshirts.html',{'lst':lst})

def trousers (request):
    lst=TrousersBottomWear.objects.all()
    return render(request,'trousers.html',{'lst':lst})

def jeans (request):
    lst=JeansBottomWear.objects.all()
    return render(request,'jeans.html',{'lst':lst})

def cargo (request):
    lst=CargoBottomWear.objects.all()
    return render(request,'cargo.html',{'lst':lst})

def search_list(request):
    q=request.GET.get('query')
    if q:
        match1=FormalShirt.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))
        if match1:
            return render(request,'search_list.html',{'match1':match1})
        else:
            messages.error(request,'No result found')
            return render(request,'search_list1.html')
    return render(request,'search_list.html')

def thankyou (request):
    return render(request,'thankyou.html')



lst=[]
price=[]
def cart(request, x):
    #item=FormalShirt.objects.get(id=x)
    item=get_object_or_404(FormalShirt,id=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'price':price,'no_items':len(lst),'tot_price':sum(price)})

lst=[]
price=[]
def cart(request, x):
    #item=CasualShirt.objects.get(id=x)
    item=get_object_or_404(FormalShirt,id=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'price':price,'no_items':len(lst),'tot_price':sum(price)})








