from django.urls import path, include, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView

app_name = 'knittingshop'
urlpatterns = [
                  path('', views.index, name='index'),
                  path('<int:question_id>/details', views.detail, name='detail'),
                  path('gallery/', views.gallery, name='gallery'),
                  path('contacts/', views.contacts, name='contacts'),
                  path('test/', views.testindex, name='testindex'),
                  path('login/', LoginView.as_view(template_name='knittingshop/login.html'), name='login'),
                  path('logout/', views.logout, name='logout'),
                  path('register/', views.register, name='register'),
                  path('profile/', views.view_profile, name='view_profile'),
                  path('profile/edit/', views.edit_profile, name='edit_profile'),
                  path('change-password/', views.change_password, name='change_password')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
