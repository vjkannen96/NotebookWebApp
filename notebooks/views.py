from django.http import HttpResponse
from .models import Note
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):
    latest_notes_list = Note.objects.order_by('-pub_date')[:10]
    context = {
    'latest_notes_list': latest_notes_list,
    }
    return render(request, 'notebooks/index.html', context)

def detail(request, note_id):
    note = get_object_or_404(Note, pk = note_id)
    return render(request, 'notebooks/detail.html', {'note': note})


class NoteCreate(CreateView):
    model = Note
    fields=['note_title','note_description']
    pk_url_kwarg = 'note_id'

class NoteEdit(UpdateView):
    model = Note
    fields=['note_title','note_description']
    pk_url_kwarg = 'note_id'

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notebooks:index')
    pk_url_kwarg = 'note_id'
