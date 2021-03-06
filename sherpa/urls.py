"""sherpa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application 
from django.conf.urls import include
from django.urls import path
from portal import views
from portal.views import signup, home

urlpatterns += [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('portal/', include('portal.urls')),
    path('demofirst/', views.demofirst, name='demofirst'),
    path('livedemo/', views.users, name='livedemo'), 
    path('student/', views.gwoo, name='student'), 
    path('circle/', views.circle, name='circle'), 
    path('feedback/', views.feedback, name='feedback'), 
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
#urlpatterns += [
#    path('', RedirectView.as_view(url='/login/')),
#]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)