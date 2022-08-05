from django.shortcuts import render
from django.views.generic import View
from .models import * 
# Create your views here.
class Base(View):
    context = {}

class HomeView(Base):
    def get (self,request):
        self.context['catas'] = Category.object.all()
        self.context['Subcatas'] = SubCategory.object.all()
        #self.context['ads'] = Category.object.all()
        #self.context['sliders'] = Category.object.all()
        return render(request,'index.html')