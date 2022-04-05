import random
from django.shortcuts import render


def home(request):

    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def generator(request):
    names =(['Maggi', 'Lisa', 'Andres', 'Gaston'])

    generator_name = ''

    #obtengo datos del form, mediante la url
    lengh_name = int(request.GET.get('length'))
    male_activate = request.GET.get('male')
    female_activate = request.GET.get('female')

    if male_activate:
        names = (['Andres', 'Gaston', 'Ian', 'Richard', 'Aldric', 'Tom'])

    #CORREGIR. Al tener ambos checkbox activados, solo muestra la lista female
    if female_activate:
        names = (['Maggi', 'Lisa', 'Abi', 'Sofia', 'Viky', 'Sol'])

    if lengh_name == 1:
        pass

    for i in range(lengh_name):
        generator_name += random.choice(names)

    return render(request, 'generator/name.html', {'name': generator_name})