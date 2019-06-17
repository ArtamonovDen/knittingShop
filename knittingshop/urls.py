from django.urls import path
from . import views
from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

app_name = 'knittingshop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('test/', views.testindex, name='testindex'),
    path('login/', auth_view.LoginView.as_view(template_name='knittingshop/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='knittingshop/logout.html'), name='logout'),
    path('register/', views.register, name='register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)