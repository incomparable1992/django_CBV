from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Notes
from .forms import NoteForm


class NoteList(ListView):
    model = Notes


class NoteDetail(DetailView):
    model = Notes


class NoteCreate(CreateView):
    form_class = NoteForm
    model = Notes
    success_url = reverse_lazy('note_list')
    # return reverse('note_list')


class NoteUpdate(UpdateView):
    form_class = NoteForm
    model = Notes
    success_url = reverse_lazy('note_list')


class NoteDelete(DeleteView):
    model = Notes
    success_url = reverse_lazy('note_list')

def my_view(request):
    a = '3'-2.0
    print(a)
    return HttpResponse("function viewww.")