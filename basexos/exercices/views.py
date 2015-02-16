import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from exercices.models import Exercice, files

# Create your views here.
##class IndexView(generic.ListView):
##    template_name = 'index.html'
##    context_object_name = 'latest_exercices'
##
##    def get_queryset(self):
##        """Return the list of exercices."""
##        return Exercice.objects



def index(request):
    latest_exercices = Exercice.objects.order_by('titre')[:5]
    context = {'latest_exercices': latest_exercices}
    #print ([id.titre for id in context['latest_exercices']])
    return render(request, 'exercices/index.html', context)

@require_POST
def upload( request ):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.
    file = upload_receive( request )

    instance = files( fichier = file )
    instance.save()

    basename = os.path.basename( instance.file.path )

    file_dict = {
        'name' : basename,
        'size' : file.size,

        'url': settings.MEDIA_URL + basename,
        'thumbnailUrl': settings.MEDIA_URL + basename,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse( request, file_dict )
