from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Item, UserProfile, Purchase
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from .forms import RegistrationForm, EditProfileForm, EditUserForm
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required, user_passes_test

from django.urls import reverse


def index(request):
    last_items_list = Item.objects.order_by('-item_pub_date')[:3]
    print(last_items_list)
    return render(request, 'knittingshop/index.html', {'last_items_list': last_items_list})


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'knittingshop/detail.html', {'item': item})


def gallery(request):
    all_items_list = Item.objects.all()
    return render(request, 'knittingshop/gallery.html', {'all_items_list': all_items_list})


def contacts(request):
    return render(request, 'knittingshop/contacts.html')


def login(request):
    return render(request, 'knittingshop/login.html')


@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect(reverse('knittingshop:index'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # request.user.basket_set.create()
            return redirect(reverse('knittingshop:index'))
        else:
            return HttpResponse('wrong input')  # TODO
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'knittingshop/reg_form.html', args)


@login_required(login_url='/login/')
def buy(request, item_id):
    profile = UserProfile.objects.get(user=request.user)  # TODO check profile existence
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=True)
            chosen_item = item
            # user = UserProfile.objects.get(user=request.user)
            purchase = profile.purchase_set.create(chosen_item=chosen_item)
            return redirect(reverse('knittingshop:thanks_for_buying'))
        else:
            return redirect(reverse('knittingshop:{}/buy'.format(item_id)))  # TODO add error message
    else:
        profile = UserProfile.objects.get(user=request.user)
        args = {
            'formProfile': EditProfileForm(instance=profile),
            'item': item
        }
        print(args['formProfile'])
        return render(request, 'knittingshop/buy.html', args)
    print(request.user)
    # args = {
    #     'item': Item.objects.get(id=item_id),
    #     'user': UserProfile.objects.get(user=request.user)
    # }
    #
    # return render(request, 'knittingshop/buy.html', args)


def confirm_purchase(request):
    return render(request, 'knittingshop/thanks_for_buying.html')


def view_profile(request):
    if request.user.is_authenticated:
        print(request.user)
        profile = UserProfile.objects.get(user=request.user)
        args = {'user': profile}
        return render(request, 'knittingshop/profile.html', args)
    else:
        return redirect('/login')


@login_required(login_url='/login/')
def add_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('knittingshop:add_profile'))
        else:
            return redirect(reverse('knittingshop:add_profile'))  # TODO add error message
    else:
        profile = UserProfile.objects.get(user=request.user)
        args = {
            'formUser': EditProfileForm(instance=profile)
        }
        return render(request, 'knittingshop/add_profile.html', args)


@login_required(login_url='/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('knittingshop:view_profile'))
        else:
            return redirect(reverse('knittingshop:edit_profile'))  # TODO add error message
    else:
        args = {
            'formUser': EditUserForm(instance=request.user)
        }
        return render(request, 'knittingshop/edit_profile.html', args)


# profile = UserProfile.objects.get(user=request.user)
# form = EditProfileForm(request.POST, instance=profile)
# if form.is_valid():
#     form.save()
#     return redirect(reverse('knittingshop:view_profile'))
# else:
@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            auth.update_session_auth_hash(request, user)
            return render(request, 'knittingshop/password_change_done.html')
        else:
            return render(request, 'knittingshop/change_password.html', {'form': form})

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
# {% if latest_question_list %}
#     <ul>
#     {% for question in latest_question_list %}
#         <li><a href="{% url 'knittingshop::detail' question.id %}">{{ question.question_text }}</a></li>
#     {% endfor %}
#     </ul>
# {% else %}
#     <p>No polls are available.</p>
# {% endif %}
