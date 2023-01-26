from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)
from .models import Snack, MyForm


# def snacks(request):
#     return render(request, 'snack_list.html')
#
# def snacksDetail(request):
#     return render(request, 'snack_detail.html')

class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snacks'


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = "__all__"


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ["name", "rating", "reviewer", "image_url"]  # fields = "__all__" for all fields


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy("snack_list")


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success')
    else:
        form = MyForm()
    return render(request, 'snack_create.html', {'form': form})
