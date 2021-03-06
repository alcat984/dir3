from django.contrib import admin
from django.urls import path, include

from mysite.core import views
import dashboard.views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret', views.secret_page, name='secret'),
    path('secret2', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('company-reg', views.company_reg, name='company_reg'),
    path('admin/', admin.site.urls),
    path('dashboard', dashboard.views.dashboard, name='dashboard'),
]
