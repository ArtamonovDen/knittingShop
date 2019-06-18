from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Item
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
import  django.contrib.auth as auth
from django.contrib.auth.decorators import login_required

from django.urls import reverse


def index(request):
    last_items_list = Item.objects.order_by('-pub_date')[:3]
    return render(request, 'knittingshop/index.html', {'last_items': last_items_list})


def detail(request, question_id):
    # item = get_object_or_404(Item, pk=question_id)
    # return render(request, 'knittingshop/detail.html', {'item': item})
    return HttpResponse('item\'s details')


def gallery(request):
    all_items_list = Item.objects.all()
    return render(request, 'knittingshop/gallery.html', {'all_items_list': all_items_list})


def contacts(request):
    return render(request, 'knittingshop/contacts.html')


def testindex(request):
    return render(request, 'knittingshop/testindex.html', {'object': Item.objects.all()[0]})


def login(request):
    return render(request, 'knittingshop/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('knittingshop:index'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('knittingshop:index'))
        else:
            return HttpResponse('wrong input')  # TODO
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'knittingshop/reg_form.html', args)


def view_profile(request):
    if request.user.is_authenticated:
        args = {'user': request.user}
        return render(request, 'knittingshop/profile.html', args)
    else:
        return redirect('/login')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('knittingshop:view_profile'))
        else:
            return redirect(reverse('knittingshop:edit_profile'))  # TODO add error message

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'knittingshop/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)
            return redirect(reverse('knittingshop:profile'))
        else:
            return redirect(reverse('knittingshop:change_password'))  # TODO add error message

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'knittingshop/change_password.html', args)


# TODO
'''
{% if user.is_authenticated() %}
{% else %}
{% end if %}


@login_required
'''
