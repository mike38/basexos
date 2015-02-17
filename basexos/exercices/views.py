import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from exercices.models import Exercice, Files, Test_files

# Create your views here.
##class IndexView(generic.ListView):
##    template_name = 'index.html'
##    context_object_name = 'latest_exercices'
##
##    def get_queryset(self):
##        """Return the list of exercices."""
##        return Exercice.objects



def index(request):
    latest_exercices = Exercice.objects.order_by('id')[:5]
#    fichiers = Files.objects.all()
    context = {'latest_exercices': latest_exercices}
#    context['fichiers']= fichiers
    #print ([id.titre for id in context['latest_exercices']])
    return render(request, 'exercices/index.html', context)

class DetailView(generic.DetailView):
    model = Exercice
    template_name = 'exercices/detail.html'
    
class Ajout( generic.TemplateView ):
    template_name = 'exercices/ajout.html'

    def get_context_data(self, **kwargs):
        context = super( Ajout, self ).get_context_data( **kwargs )
        context['accepted_mime_types'] = ['image/*']
        print(context)
        return context


@require_POST
def upload( request ):
    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.
    file = upload_receive( request )
    instance = Test_files( fichier = file )
    instance.save()
    basename=os.path.basename(instance.fichier.path)
    
    file_dict = {
        'name' : basename,
        'size' : file.size,

        'url': settings.MEDIA_URL + basename,
        'thumbnailUrl': settings.MEDIA_URL + basename,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.id }),
        'deleteType': 'POST',
    }
    print('file',file_dict)
    return UploadResponse( request, file_dict )

@require_POST
def upload_delete( request, pk ):
    success = True
    try:
        instance = Test_files.objects.get( id = pk )
        os.unlink( instance.fichier.path )
        instance.delete()
    except files.DoesNotExist:
        success = False

    return JFUResponse( request, success )
