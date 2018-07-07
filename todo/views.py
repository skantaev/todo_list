from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import ListElement
from .forms import ListElementForm

# Create your views here.


class ListElementCreate(CreateView):
    model = ListElement
    form_class = ListElementForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_elements'] = ListElement.objects.filter(visible=True)
        return context


class ListElementUpdate(UpdateView):
    model = ListElement
    form_class = ListElementForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_elements'] = ListElement.objects.filter(visible=True)
        return context



class ListElementDelete(DeleteView):
    model = ListElement
    form_class = ListElementForm
    success_url = reverse_lazy('index')


