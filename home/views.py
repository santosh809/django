from cProfile import label
from django.shortcuts import render
from django.views.generic import View
from .models import * 
# Create your views here.
class Base(View):
    context = {} #dictionary

class HomeView(Base):
    def get (self,request):
        self.context['catas'] = Category.objects.all()
        self.context['subcatas'] = SubCategory.objects.all()
        self.context['ads'] = Ads.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['brand'] = Brand.objects.all()
        self.context['reviews'] = Review.objects.all()
        self.context['serv']= Service.objects.all()
        self.context['hots'] = Product.objects.filter(lables = 'hot')
        self.context['news'] = Product.objects.filter(lables = 'new')
        self.context['sales'] = Product.objects.filter(lables = 'sale')
        return render(request,'index.html',self.context)

