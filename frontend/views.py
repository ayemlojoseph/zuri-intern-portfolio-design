from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("The form is valid")
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            country = form.cleaned_data.get('country')
            contact = Contact(email=email, message=message, country=country)
            contact.save()
            messages.info(request, "Message Sent, You will be contacted shortly...")
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})



def formSuccess(request):
    return render (request, 'form-success.html' )
    