from django.urls import path, re_path
from . import views as auth_views
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(), name="user_logout"),
    path('register/', views.register, name='register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         {"post_change_redirect": "registration/password-change-done"}, name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         {"template_name": "registration/password_reset_subject.txt",
          "post_reset_redirect": "/registration/password_reset_done.html"}, name="password_reset"),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(),
         {"template_name": "registration/password_reset_done.html"}, name="password_reset_done"),
    re_path('password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/',
         auth_views.PasswordResetConfirmView.as_view(), {"template_name": " registration/password_reset_confirm.html",
                                                         "post_reset_redirect": "/registration/password_reset_complete"
                                                                                ".html"},
         name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(),
         {"template_name": "registration/password_reset_complete.html"}, name="password_reset_complete"),
]
