from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# function name Movie
from .forms import MovieForm
from movie_app.models import Movie




def film(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie':movie})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, 'add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})

def delete(request, id):
    if  request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')



