from django.urls import path
from .views import HomePageView, AboutPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
