from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from . models import ClassModel, ContactModel
from django.views.generic import CreateView, ListView,View,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

   
class ProductCreateView(CreateView):
    model = ClassModel
    fields = ["firstname", "lastname","phonenumber", "email", "messages"]
    template_name = 'julyapp/index.html'
    success_url = '/view/'
          
       
class ProductContactView(ListView):
    model = ContactModel
    fields = ["firstname", "lastname","phonenumber", "email", "messages"]
    template_name = 'julyapp/contact.html'
    success_url = '/contact/'
       

class ProductView(View):
       model = ContactModel
       template_name = 'classapp/table.html'
       context_object_name = 'data'
       
    
def contact(request):
    return render(request, "julyapp/contact.html") 


class ProductUpdateView(UpdateView):
       model = ClassModel
       fields = ["fullname","phonenumber", "email", "messages"]
       template_name = 'classapp/update.html'
       success_url = '/table/'
       
class ProductDeleteView(DeleteView):
       model = ClassModel
       template_name = 'classapp/delete.html'
       success_url = reverse_lazy("table")
       

def company(request):
    return render(request, "julyapp/company.html")

def services(request):
    return render(request, "julyapp/services.html")

