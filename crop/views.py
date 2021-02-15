from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Crop, Rice
import json
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def home(request):
    crops = Crop.objects.all()
    context_dict = {}
    crop_names = []
    crop_prod = []
    for crop in crops:
        crop_names.append(crop.crop)
        crop_prod.append(crop.production)
        context_dict[crop.crop] = crop.production
    context_dict["crops"] = json.dumps(crop_names)
    context_dict["prod"] = json.dumps(crop_prod)
    return render(request, 'crop/home.html', context_dict)


def added(request):
    return render(request, 'crop/added.html')


class CropListView(ListView):
    model = Crop
    template_name = 'crop/crops.html'
    context_object_name = 'crops'
    ordering = ['-id']
    paginate_by = 12


class CropCreateView(LoginRequiredMixin, CreateView):
    model = Crop
    template_name = 'crop/crop_entry.html'
    fields = ['state', 'year', 'season', 'crop', 'area', 'production']
    success_url = 'added'


def about(request):
    return render(request, 'crop/about.html')


def rice(request):
    states = ['Andaman and Nicobar Islands', 'Arunachal Pradesh', 'Bihar',
              'Chhattisgarh', 'Himachal Pradesh', 'Jammu and Kashmir',
              'Jharkhand', 'Kerala', 'Odisha', 'Punjab', 'Tamil Nadu',
              'Uttarakhand']
    data = {}
    context_dict = {}
    context_dict["nstates"] = list(i.replace(" ", "") for i in states)
    for state in states:
        data[state.replace(" ", "")] = list(Rice.objects.filter(
            state=state).values('year', 'area', 'rainfall', 'production'))
    context_dict["states"] = states
    context_dict["data"] = json.dumps(data)
    return render(request, 'crop/rice_data.html', context_dict)
