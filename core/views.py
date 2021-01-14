from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(resquest, a, b):
    soma = a + b
    return HttpResponse('<h2>O valor da soma de {} + {} é {}.</h2>'.format(a, b, soma))

def subtracao(resquest, a, b):
    sub = a - b
    return HttpResponse('<h2>O valor de {} - {} = {}.</h2>'.format(a, b, sub))

def mult(resquest, a, b):
    multip = a * b
    return HttpResponse('<h2>O valor de {} x {} = {}.</h2>'.format(a, b, multip))

def divisao(resquest, a, b):
    divi = a / b
    return HttpResponse('<h2>O valor de {} / {} = {}.</h2>'.format(a, b, divi))