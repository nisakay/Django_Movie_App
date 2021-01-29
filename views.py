from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movie
import requests


def Movie_home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'MovieUpapp/MovieUpHome.html', context)

def createItem(request):
    form = MovieForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MovieUpHome')
    else:
        print(form.errors)
        form = MovieForm()
    context = {'form': form}
    return render(request, 'MovieUpapp/createItem.html', context)

def MovieUp_index(request):
# gets all movies from database
    movies = Movie.objects.all()
# print to movies terminal
    print(movies)
    context = {'movies': movies, }
    return render(request, 'MovieUpapp/MovieUp_index.html', context)

def MovieUp_details(request, pk):
# gets instance of the Movie model object
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie': movie, }
    return render(request, 'MovieUpapp/MovieUp_details.html', context)


# Edit page
def MovieUp_edit(request, pk):
    pk = int(pk)
    movies = get_object_or_404(Movie, pk=pk)
# Finds the form that was submitted by a user
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movies)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MovieIndex')
        else:
            print(form.errors)
    else:
        form = MovieForm(instance=movies)
        context = {'form': form}
    return render(request, 'MovieUpapp/MovieUp_edit.html', context)


# Delete movies from database
def MovieUp_delete(request, pk):
    pk = int(pk)
    movies = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        return redirect('MovieIndex')
    context = {'movies': movies, }
    return render(request, 'MovieUpapp/MovieUp_delete.html', context)


# Confirm delete
def confirm_delete(request, pk):
    pk = int(pk)
    movies = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movies.delete()
        return redirect('MovieUpHome')
    else:
        return redirect('MovieUpHome')


def MovieUp_api(request):
    movie = {}
    if 'Title' in request.GET:
        Title = request.GET['Title']
        url = 'http://www.omdbapi.com/?apikey=7a0111a7' % Title
        response = requests.get(url)
        movie = response.json()
    return render(request, 'MovieUpapp/MovieUp_api.html', {'movie': movie})