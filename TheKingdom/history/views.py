from django.http import Http404
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "history/index.html")

def first_state_view(request):
    return render(request, "history/first_saudi_state.html")

def second_state_view(request):
    return render(request, "history/second_saudi_state.html")

def third_state_view(request):
    return render(request, "history/third_saudi_state.html")

def ruler_abdulaziz(request):
    return render(request, 'history/rulers/king_abdulaziz.html')

def ruler_saud(request):
    return render(request, 'history/rulers/king_saud.html')

def ruler_faisal(request):
    return render(request, 'history/rulers/king_faisal.html')

def ruler_khalid(request):
    return render(request, 'history/rulers/king_khalid.html')

def ruler_fahd(request):
    return render(request, 'history/rulers/king_fahd.html')

def ruler_abdullah(request):
    return render(request, 'history/rulers/king_abdullah.html')

def ruler_salman(request):
    return render(request, 'history/rulers/king_salman.html')

def ruler_muhammad_bin_saud(request):
    return render(request, "history/rulers/imam_muhammad_bin_saud.html")

def ruler_abdulaziz_bin_muhammad(request):
    return render(request, "history/rulers/abdulaziz_bin_muhammad.html")

def ruler_saud_bin_abdulaziz(request):
    return render(request, "history/rulers/saud_bin_abdulaziz.html")

def ruler_abdullah_bin_saud(request):
    return render(request, "history/rulers/abdullah_bin_saud.html")

def ruler_turki_bin_abdullah(request):
    return render(request, "history/rulers/turki_bin_abdullah.html")

def ruler_faisal_bin_turki(request):
    return render(request, "history/rulers/faisal_bin_turki.html")

def ruler_abdullah_bin_faisal(request):
    return render(request, "history/rulers/abdullah_bin_faisal.html")

def ruler_saud_bin_faisal(request):
    return render(request, "history/rulers/saud_bin_faisal.html")

def ruler_abdulrahman_bin_faisal(request):
    return render(request, "history/rulers/abdulrahman_bin_faisal.html")