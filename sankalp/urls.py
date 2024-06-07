from django.contrib import admin
from django.urls import path
from sankalp import views

# for media 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('registeration', views.register, name='register'),
    path('search_results', views.searchResults, name='searchResults'),
    path('result/<res>', views.result, name='result'),
    path('course/<course_name>', views.courseDetails, name='courseDetails'),
    path('privacy_policy', views.privacyPolicy, name='privacyPolicy'),
    path('desclaimer', views.desclaimer, name='desclaimer'),
    path('refund_policy', views.refundPolicy, name='refundPolicy'),
    path('termsandcondition', views.termsandcondition, name='termsandcondition'),
]


# FOR MEDIA UPLOAD 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)