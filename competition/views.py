from django.shortcuts import render, redirect
from .forms import CompetitionForm
from .models import Competition

def competitions(request):
    competitions = Competition.objects.all()
    return render(request, 'pages/competitions.html', {
        'competitions': competitions
    })

def createCompetition(request):
    competitions = Competition.objects.all()
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST)
        if competition_form.is_valid():
            competition = competition_form.save(commit=False)
            competition.save()
            return redirect('create-competition')
    else:
        competition_form = CompetitionForm()
    return render(request, 'pages/create-competition.html', {
        'competition_form': competition_form,
        'competitions': competitions
    })

def updateCompetition(request, pk):
    competition = Competition.objects.get(id=pk)
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST, instance=competition)
        if competition_form.is_valid():
            competition_form.save()
            return redirect('create-competition')
    else:
        competition_form = CompetitionForm(instance=competition)
    return render(request, 'pages/update-competition.html', {
        'competition_form': competition_form,
    })

def deleteCompetition(request, pk):
    competition = Competition.objects.get(id=pk)
    competition.delete()
    return redirect('create-competition')
