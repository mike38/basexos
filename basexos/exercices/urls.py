#from django.conf.urls import patterns, url
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from exercices import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url( r'^ajout', views.Ajout.as_view(), name = 'ajout' ),
    url( r'upload/', views.upload, name = 'jfu_upload' ),
    url( r'^delete/(?P<pk>\d+)$', views.upload_delete, name = 'jfu_delete' ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
