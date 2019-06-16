from django.urls import path
from . import views
from django.conf import  settings
from django.conf.urls.static import static

app_name = 'knittingshop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('test/', views.testindex, name='testindex')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
