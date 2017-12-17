from .models import *
from django.shortcuts import render
from .forms import AlumniForm


def search(request):
    if request.method == 'POST':
        form=AlumniForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            alumni_list=Alumni.objects.filter(year=cd['year'],typelist=cd['typelist'],field=cd['field'])
            form=AlumniForm()
            return render(request, 'user_list.html', {'alumni_list': alumni_list,'form': form})
    else:
        form=AlumniForm()
        return render(request, 'homepage.html', {'form': form})
            
