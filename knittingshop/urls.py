from django.urls import path, include, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView

app_name = 'knittingshop'
urlpatterns = [
                  path('', views.index, name='index'),
                  path('<int:question_id>/details', views.detail, name='detail'),
                  path('gallery/', views.gallery, name='gallery'),
                  path('contacts/', views.contacts, name='contacts'),
                  path('basket/', views.basket, name='basket'),
                  path('login/', LoginView.as_view(template_name='knittingshop/login.html'), name='login'),
                  path('logout/', views.logout, name='logout'),
                  path('register/', views.register, name='register'),
                  path('profile/', views.view_profile, name='view_profile'),
                  path('profile/edit/', views.edit_profile, name='edit_profile'),
                  path('change-password/', views.change_password, name='change_password'),
                  # path('reset-password/',
                  #      auth_views.PasswordResetView.as_view(template_name='knittingshop/password_reset_form.html'),
                  #      name='reset_password'),
                  # path('reset-password/done',
                  #      auth_views.PasswordResetDoneView.as_view(template_name='knittingshop/reset_password_done.html'),
                  #      name='reset_password_done'),
                  # path('reset-password/confirm',
                  #      auth_views.PasswordResetConfirmView.as_view(template_name='knittingshop/password_reset_confirm.html'),
                  #      name='password_reset_confirm'),
                  # # path('reset-password/confirm',
                  # #      auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
                  # path('reset-password/complete',
                  #      auth_views.PasswordResetCompleteView.as_view(template_name='knittingshop/password_reset_complete.html'),
                  #      name='password_reset_complete'),

                  # path('accounts/', include('django.contrib.auth.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
