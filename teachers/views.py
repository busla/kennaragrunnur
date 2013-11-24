from django.shortcuts import render_to_response
from teachers.models import Genre
from django.template import RequestContext

def show_genres(request):
    return render_to_response("genres.html", {'nodes':Genre.objects.all()}, context_instance=RequestContext(request))