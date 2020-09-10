from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import ClothingForm
from .models import Clothing


class Home(TemplateView):
    template_name = 'home.html'


def clothing_list(request):
    clothings = Clothing.objects.all()
    return render(request, 'clothing_list.html', {
        'clothings': clothings
    })


def upload_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clothing_list')
    else:
        form = ClothingForm()
    return render(request, 'upload_clothing.html', {
        'form': form
    })


def delete_clothing(request, pk):
    if request.method == 'POST':
        clothing = Clothing.objects.get(pk=pk)
        clothing.delete()
    return redirect('clothing_list')


class ClothingListView(ListView):
    model = Clothing
    template_name = 'class_clothing_list.html'
    context_object_name = 'clothings'


class UploadClothingView(CreateView):
    model = Clothing
    form_class = ClothingForm
    success_url = reverse_lazy('class_clothing_list')
    template_name = 'upload_clothing.html'
