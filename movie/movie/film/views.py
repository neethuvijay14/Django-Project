from django.shortcuts import render
from django.urls import reverse_lazy
from film.models import Movies
from film.forms import Movieform
# from django.db.models import Q
from django.views.generic import ListView
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
# def home(request):
#     m = Movies.objects.all()
#     return render(request, 'home.html',{'m':m})
class Movielistview(ListView):
    model=Movies
    template_name="home.html"
    context_object_name="m"

# def addmovie(request):
#     if (request.method == "POST"):
#         t = request.POST['t']
#         y = request.POST['y']
#         r = request.POST['r']
#         d = request.POST['d']
#         i = request.FILES['i']
#         m = Movies.objects.create(title=t, year=y, rating=r, desc=d, img=i)
#         m.save()
#         return home(request)
#     return render(request,'addmovie.html')

class createview(CreateView):
    model=Movies
    template_name="addmovie.html"
    fields=['title','year','rating','desc','img']
    success_url=reverse_lazy('film:home')

# def viewmovie(request,p):
#     m = Movies.objects.get(id=p)
#     return render(request,'viewmovie.html',{'m':m})

class detailview(DetailView):
    model=Movies
    template_name="viewmovie.html"
    context_object_name="m"

# def deletemovie(request,p):
#
#     m = Movies.objects.get(id=p)
#     m.delete()
#     return home(request)
class deleteview(DeleteView):
    model=Movies
    template_name = "delete.html"
    success_url = reverse_lazy('film:home')

# def editmovie(request,p):
#     m = Movies.objects.get(id=p)
#     form = Movieform(instance=m)
#     if (request.method == "POST"):
#         form = Movieform(request.POST,request.FILES,instance=m)
#
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request, 'editmovie.html', {'form': form})

class updateview(UpdateView):
    model = Movies
    template_name = "addmovie.html"
    fields = ['title', 'year', 'rating', 'desc', 'img']
    success_url = reverse_lazy('film:home')