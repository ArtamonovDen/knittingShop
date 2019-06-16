from django.urls import path
from . import views


app_name = 'knittingshop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('test/', views.testindex, name='testindex')
]
