"""
URL configuration for AssociAction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from general_views import views as gv
from authentication import views as authv
from association import views as assoviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gv.home, name='home'),
    #Authentication urls
    path('register/', authv.RegisterView.as_view(), name='register'),
    path('login/', authv.LoginPageView.as_view(), name='login'),
    path('logout/', authv.logout_view, name='logout'),
    #Profile urls
    path('profile/', authv.profile_view, name='profile'),
    path('profile_update/', authv.update_profile_view, name='update_profile'),
    #Association urls
    path('association/<int:association_id>/', assoviews.association_detail, name='association_detail'),
    path('association_create/', assoviews.create_association, name='create_association'),
    path('association_address/<int:association_id>/', assoviews.association_address, name="association_address")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)