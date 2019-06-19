from django.urls import path, include, reverse_lazy
import re
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeDoneView

app_name = 'knittingshop'
urlpatterns = [
                  path('', views.index, name='index'),
                  path('<int:item_id>/detail/', views.detail, name='detail'),
                  path('gallery/', views.gallery, name='gallery'),
                  path('<int:item_id>/buy/', views.buy, name='buy'),
                  path('thanks_for_buying/', views.confirm_purchase, name='thanks_for_buying'),
                  path('contacts/', views.contacts, name='contacts'),
                  path('login/', LoginView.as_view(template_name='knittingshop/login.html'), name='login'),
                  path('logout/', views.logout, name='logout'),
                  path('register/', views.register, name='register'),
                  path('profile/edit/', views.edit_profile, name='edit_profile'),
                  path('change-password/', views.change_password, name='change_password')


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
