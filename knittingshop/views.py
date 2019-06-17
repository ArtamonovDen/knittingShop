from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Item
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def index(request):
    return render(request, 'knittingshop/index.html', {'object': Item.objects.all()[0]})


def detail(request, question_id):
    # item = get_object_or_404(Item, pk=question_id)
    # return render(request, 'knittingshop/detail.html', {'item': item})
    return HttpResponse('item\'s details')


def gallery(request):
    return render(request, 'knittingshop/gallery.html')


def testindex(request):
    return render(request, 'knittingshop/testindex.html', {'object': Item.objects.all()[0]})


def login(request):
    return render(request, 'knittingshop/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('wrong input')  #TODO
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'knittingshop/reg_form.html', args)
