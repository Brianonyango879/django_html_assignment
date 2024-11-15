from django.shortcuts import render,redirect
from .models import Contacts
from .forms import ContactsForm
# Create your views here.
#create index view
def index(request):
    return render(request,'index.html')

def contact_list(request):
    contacts = Contacts.objects.all()
    return render(request, 'portfolio/contact_list.html', {'contacts':contacts})
#create contact view
def contact_create(request):
    if request.method == 'POST or None':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')

    else:
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        return render(request,'portfolio/contacts_form.html',{'form':form})
def contact_success_view(request):
    return render(request, 'portfolio/contact_success.html')
