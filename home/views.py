from django.shortcuts import render, redirect
from admin_argon.forms import RegistrationForm
from .forms import RapperRegisterForm, RapperProfileForm, SongForm, RecommendationForm
from django.contrib.auth.models import User
from .models import Rapper, Song, Recommandations
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from admin_argon.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

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

def rappersProfileList(requetst):
    rappers = Rapper.objects.all()
    return render(requetst, 'pages/rappers-profile-list.html', {
        'rappers': rappers
        })

def getRapper(request, pk):
    rapper = get_object_or_404(Rapper, id=pk)
    form = RecommendationForm()

    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.rapper = request.user.rapper
            recommendation.owner = rapper
            recommendation.save()
            return redirect('rapper-profile-view', pk=rapper.id)
    return render(request, 'pages/rapper-profile-view.html', {
        'rapper': rapper,
        'form' : form
        })

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('rapper-profile')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/sign-in.html', {'form': LoginForm()})

def user_logout_view_custom(request):
  logout(request)
  return redirect('rapper_login')

class CustomLoginView(LoginView):
    template_name = 'accounts/sign-in.html'
    form_class = LoginForm

    def get_success_url(self):
        """
        Determine the URL to redirect to after a successful login.
        """
        if self.request.user.is_staff:
            # If the user is a staff member, redirect to the admin panel.
            return reverse_lazy('admin:index')
        else:
            # Otherwise, redirect to the user's profile page.
            return reverse_lazy('rapper-profile')