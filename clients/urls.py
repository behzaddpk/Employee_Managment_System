from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import(
    client,
    add_client,
    client_profile,
)


urlpatterns = [
    path('clients/', client, name='clients'),
    path('add-client/', add_client, name='add-client'),
    path('client/<slug:slug>/', client_profile, name='client-profile'),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)