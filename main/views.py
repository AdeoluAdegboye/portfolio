from django.shortcuts import render
from django.views.generic import ListView
from .models import Career, Education, Project, Social, Testimonial

# Create your views here.

class Portfolio(ListView):
    template_name = 'index.html'
    model = Project
    
    def get_context_data(self, **kwargs):
        ctx = super(Portfolio, self).get_context_data(**kwargs)
        ctx['educations'] = Education.objects.all()
        ctx['careers'] = Career.objects.all()
        ctx['testimonials'] = Testimonial.objects.all()
        ctx['socials'] = Social.objects.all()
        
        return ctx
    