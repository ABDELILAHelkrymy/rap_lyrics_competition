from django.shortcuts import render, redirect
from admin_argon.forms import RegistrationForm
from .forms import RapperRegisterForm, RapperProfileForm, SongForm
from django.contrib.auth.models import User
from .models import Rapper, Song
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'pages/dashboard.html')

def register(request):
    if request.method == 'POST':
        profile_form = RapperRegisterForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            return redirect('/accounts/login/')
    else:
        profile_form = RapperRegisterForm()
    return render(request, 'accounts/rapper-register.html', {'profile_form': profile_form})

def rapperProfile(request):
    current_user = request.user.rapper
    songs = current_user.song_set.all()
    if request.method == 'POST':
        profile_form = RapperProfileForm(request.POST, request.FILES, instance=current_user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('rapper-profile')
    else:
        profile_form = RapperProfileForm(instance=current_user)
    return render(request, 'pages/rapper-profile.html', {
        'profile_form': profile_form,
        'songs': songs,
        'rapper': current_user
        })

def rapperSongs(request):
    current_user = request.user.rapper
    songs = current_user.song_set.all()
    if request.method == 'POST':
        song_form = SongForm(request.POST)
        if song_form.is_valid():
            song = song_form.save(commit=False)
            song.rapper = current_user
            song.save()
            return redirect('rapper-songs')
    else:
        song_form = SongForm()
    return render(request, 'pages/rapper-songs.html', {
        'song_form': song_form,
        'songs': songs
        })

def rapperSong(request, song_id):
    current_user = request.user.rapper
    song = current_user.song_set.get(id=song_id)
    if request.method == 'POST':
        song_form = SongForm(request.POST, instance=song)
        if song_form.is_valid():
            song_form.save()
            return redirect('rapper-songs')
    else:
        song_form = SongForm(instance=song)
    return render(request, 'pages/rapper-songs.html', {
        'song_form': song_form,
        'song': song
        })

def rapperSongEdit(request, song_id):
    current_user = request.user.rapper
    song = current_user.song_set.get(id=song_id)
    if request.method == 'POST':
        song_form = SongForm(request.POST, instance=song)
        if song_form.is_valid():
            song_form.save()
            return redirect('rapper-songs')
    else:
        song_form = SongForm(instance=song)
    return render(request, 'pages/song_edit.html', {
        'song_form': song_form,
        })

def rapperSongDelete(request, song_id):
    current_user = request.user.rapper
    song = current_user.song_set.get(id=song_id)
    song.delete()
    return redirect('rapper-songs')