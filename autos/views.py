from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Auto, Comment, Alquiler
from django.db.models import Q

from django.http import HttpResponseRedirect

# Create your views here.
class Home(TemplateView):
    template_name = 'autos/index.html'

    def get_context_data(self, **kwargs):
        autos = Auto.objects.filter(status=1)
        context = super(Home, self).get_context_data(**kwargs)
        context['autos'] = autos
        return context
    
class AutoDetail(DetailView):
    model = Auto
    template_name = 'autos/detail.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        comments = Comment.objects.filter(status=1, auto__slug=slug)
        context = super(AutoDetail, self).get_context_data(**kwargs)
        context['comments'] = comments
        return context

    def post(self, request, **kwargs):
        auto_comment = request.POST['comment']
        auto_id = request.POST['id']
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        Comment.objects.create(user_id=request.user.id, auto_id=auto_id, content=auto_comment)
        # Auto.objects.update(status=1)
        Alquiler.objects.create(user_id=request.user.id, auto_id=auto_id, date_start=date_start, date_end=date_end)
        self.get_object()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
