from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import Crop
import json
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
	crops = Crop.objects.all()
	context_dict={}
	crop_names=[]
	crop_prod=[]
	for crop in crops:
		crop_names.append(crop.crop)
		crop_prod.append(crop.production)
		context_dict[crop.crop]=crop.production
	context_dict["crops"]=json.dumps(crop_names)
	context_dict["prod"]=json.dumps(crop_prod)
	return render(request,'crop/home.html',context_dict)

def added(request):
	return render(request, 'crop/added.html')

class CropListView(ListView):
	model = Crop
	template_name = 'crop/crops.html'
	context_object_name = 'crops'
	ordering=['-id']
	paginate_by=12

class CropCreateView(LoginRequiredMixin, CreateView):
	model=Crop
	template_name='crop/crop_entry.html'
	fields= ['state','district','year','season','crop','area','production']
	success_url= 'added'

def about(request):
	return render(request, 'crop/about.html')

