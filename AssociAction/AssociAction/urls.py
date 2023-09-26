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
from events import views as eviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #General urls
    path('admin/', admin.site.urls),
    path('', gv.home, name='home'),
    path('help_center/', gv.help_center, name='help'),
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
    path('association_address/<int:association_id>/', assoviews.association_address, name="association_address"),
    path('association_list/', assoviews.association_list, name='association_list'),
    #Association rights url
    path('association_dir_rights/', assoviews.request_dir_rights_view, name='request_dir_rights'),
    #path('association_rights/', assoviews.request_rights_view, name='request_rights'),
    #Events urls
    path('association/<int:association_id>/create_event/', eviews.create_event, name='create_event'),#1
    path('association/<int:association_id>/association_events/', eviews.association_events, name='all_asso_event'),#2
    path('association/<int:association_id>/association_events/<int:event_id>', eviews.event_detail, name='event_detail'),#3
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)