from django.shortcuts import render

from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    # latest_question_list = Item.objects.order_by('-pub_date')[:5]
    # context = {
    #     'latest_question_list': []
    # }
    # return render(request, 'knittingshop/index.html', context)
    return HttpResponse('main page')


def detail(request, question_id):
    # item = get_object_or_404(Item, pk=question_id)
    # return render(request, 'knittingshop/detail.html', {'item': item})
    return HttpResponse('item\'s details')

def gallery(request):
    return HttpResponse(' gallery')
