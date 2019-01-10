from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView

from lab6.models import Bullet

# Create your views here.

class ExampleView(View):
    def get(self, request):
        return render(request, 'base.html')

class BulletsView(ListView):
    model = Bullet
    context_object_name = 'bullets'
    template_name = 'bullets.html'
    
    def get_queryset(self):
        qs = Bullet.objects.all().order_by('id').values()
        return qs

class BulletView(View):
    def get(self, request, id):
        data = Bullet.objects.get(id__exact=id)
        return render(request, 'bullet.html', {'bullet':data})
