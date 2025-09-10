# devoyage_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# This is the root URL configuration for the entire project.
urlpatterns = [
    # The standard URL for the built-in Django admin site.
    path('admin/', admin.site.urls),

    # This line is the key connection to our app.
    # It tells Django that any URL starting with 'api/' should be
    # forwarded to the 'content.urls' file for processing.
    path('api/', include('api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)