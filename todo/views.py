from django.views.generic.edit import CreateView, View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import ListElement
from .forms import ListElementForm

# Create your views here.


class ListElementCreate(CreateView):
    model = ListElement
    form_class = ListElementForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_elements'] = ListElement.objects.all()
        return context


class ListChangeElement(View):

    def get(self, request):
        try:
            pk = int(request.GET.get('id'))
            list_element = get_object_or_404(ListElement, pk=pk)

            if request.GET.get('delete'):
                list_element.delete()
            else:
                list_element.done = not list_element.done
                list_element.save()

            return HttpResponse(status=200)
        except ValueError:
            return HttpResponse(status=400)
