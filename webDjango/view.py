from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso


def home(self,name):
    return HttpResponse(f"Hola soy {name}")

def homePage(self):
    lista=[1,2,3,4,5,6,7,8,9]
    data= {"nombre":"derick", "apellido":"carcamo", "lista":lista}
    planilla= loader.get_template("home.html")
    documento= planilla.render(data)
    return HttpResponse(documento)

def cursos(self):

    cursos = Curso(nombre="UX", camada="54321")
    cursos.save()
    documento = f'Curso: {cursos.nombre} camada: {cursos.camada}'

    #planilla= loader.get_template("cursos.html")
    #cursos = Curso.objects.all()
    #data = {"cursos":cursos}
    #documento= planilla.render(data)
    return HttpResponse(documento)

    #cursos = Curso.objects.all()
    #return HttpResponse(cursos)

def redirectAppCoder(request):
    return redirect('AppCoder/')