from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.views.generic import DetailView


class Post_Detail(DetailView):
    model = Contact
    template_name = 'contact/post.html'
    context_object_name = 'article'


def detail(request):
    show_all_detail = Contact.objects.all()
    return render(request, 'contact/detail.html', {'show_all': show_all_detail})


def main_full(request):
    hello_world = 'Hello World'
    return render(request, 'contact/base.html', {'hi': hello_world})



def create(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Error'
    form = ContactForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'contact/create.html', data)

