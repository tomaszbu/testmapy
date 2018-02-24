from django.shortcuts import render
from . import forms #dodajemy tą linijkę

# Create your views here.
def index(request): #tworzymy widok index
    return render(request,'formapp/index.html') #ścieżka brana z templates



def form_name_view(request):
    form = forms.FormName() # bierzemy kklasę z forms.py
    if request.method == 'POST':  #czyli jeżeli ktoś kliknął submit
        form = forms.FormName(request.POST)

        if form.is_valid(): # dotyczy walidacji np. maila z tego formularza
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            #print("lng: "+form.cleaned_data['lng'])  #doczytać co to za metoda cleaned_data
            print("lat: "+str(form.cleaned_data['lat']))
            print("desc: "+form.cleaned_data['description'])


    return render(request,'formapp/form1.html',{'form':form}) #przekazujemy stronę/widok,ktory chccemy pokazać i context dictionary

def result_view(request):
    form = forms.FormName() # bierzemy kklasę z forms.py
    if request.method == 'POST':  #czyli jeżeli ktoś kliknął submit
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("lat: "+str(form.cleaned_data['lat']))
            lat=form.cleaned_data['lat']
            lng=form.cleaned_data['lng']
            desc = form.cleaned_data['description']+str(lng)+str(lat)

    return render(request,'formapp/resultmap.html', {'desc': desc, 'lat': lat, 'lng': lng}) #ścieżka brana z templates
