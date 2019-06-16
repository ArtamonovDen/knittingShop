from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Item
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):

    return render(request, 'knittingshop/index.html', {'object': Item.objects.all()[0]})


def detail(request, question_id):
    # item = get_object_or_404(Item, pk=question_id)
    # return render(request, 'knittingshop/detail.html', {'item': item})
    return HttpResponse('item\'s details')

def gallery(request):
    return HttpResponse(' gallery')

def testindex(request):

    return render(request, 'knittingshop/testindex.html', {'object': Item.objects.all()[0]})
