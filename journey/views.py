from django.shortcuts import render,redirect
from .models import Memory
from .form import MemForm
#from django.http import HttpResponse

def index_view(request,*args,**kwargs):
    mem=Memory.objects.all()
    cont={
        "obj":mem
    }
    
    return render(request,'index.html',cont)
    #return redirect('home/')
def home_view(request):
    return render(request,'index.html')
def add_view(request):
    mem=Memory()
    #new_city=form.cleaned_data['title']
    #print("Vail",form)
    if request.method=='POST':
        mem.title= request.POST.get('name')
        mem.place= request.POST.get('subject')
        mem.desc= request.POST.get('message')
       
        form=MemForm(request.POST ,request.FILES)
        

        if form.is_valid():
            mem.image=form.cleaned_data["image"]
        mem.save()
        
  
    form=MemForm(request.POST,request.FILES)
    context={
        'form':form
    }
    
    print(request.POST,request.FILES)
    return render(request,'contact.html',{})



def desc_view(request,id):
    m=Memory.objects.get(id=id)
    cont={
        "obj":m
    }
    return render(request,'work-single.html',cont)
   
    

