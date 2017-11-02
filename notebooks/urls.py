from django.conf.urls import url
from . import views
from .models import Note

app_name = 'notebooks'


urlpatterns = [
    url(r'^index', views.index, name = 'index'),
    url(r'^(?P<note_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<note_id>[0-9]+)/delete/$', views.NoteDelete.as_view(), name = 'delete'),
    url(r'^edit/(?P<note_id>[0-9]+)/$', views.NoteEdit.as_view(model=Note, success_url="/notebooks/index"), name = 'edit'),
    url(r'^create/$', views.NoteCreate.as_view(model=Note, success_url="/notebooks/index"), name = 'create'),
]
