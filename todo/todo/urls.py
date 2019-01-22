from django.contrib import admin
from django.urls import path, include
from task.views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
