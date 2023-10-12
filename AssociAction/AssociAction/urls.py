from django.contrib import admin
from django.urls import path
from general_views import views as gv
from authentication import views as authv
from association import views as assoviews
from events import views as eviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # General urls
    path('admin/', admin.site.urls),
    path('', gv.home, name='home'),
    path('help_center/', gv.help_center, name='help'),
    path('contact/', gv.contact, name='contact'),
    path('legals/', gv.legals, name='legals'),
    # Authentication urls
    path('register/', authv.RegisterView.as_view(), name='register'),
    path('login/', authv.LoginPageView.as_view(), name='login'),
    path('logout/', authv.logout_view, name='logout'),
    # Profile urls
    path('profile/', authv.profile_view, name='profile'),
    path('profile_update/', authv.update_profile_view, name='update_profile'),
    # Association urls
    path('association_create/',
         assoviews.create_association,
         name='create_association'),
    path('association/<int:association_id>/',
         assoviews.association_detail,
         name='association_detail'),
    path('association/<int:association_id>/update',
         assoviews.update_association,
         name='update_association'),
    path('association/<int:association_id>/association_address/',
         assoviews.association_address,
         name="association_address"),
    path('association_list/',
         assoviews.association_list,
         name='association_list'),
    # Events url
    path('association/<int:association_id>/create_event/',
         eviews.create_event,
         name='create_event'),
    path('association/<int:association_id>/association_events/',
         eviews.association_events,
         name='all_asso_event'),
    path('association/<int:association_id>/association_events/<int:event_id>',
         eviews.event_detail,
         name='event_detail'),
    path('association/<int:association_id>/association_events/'\
         '<int:event_id>/delete',
         eviews.event_delete,
         name='event_delete'),
    path('association/<int:association_id>/association_events/'\
         '<int:event_id>/update',
         eviews.event_update,
         name='event_update'),
    path('association/<int:association_id>/association_events/'\
         '<int:event_id>/address',
         eviews.event_address,
         name='event_address')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
