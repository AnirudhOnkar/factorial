from django.shortcuts import render
from math import factorial

def calculate(request):
    n1 = 5
    square = n1 ** 2
    fact = factorial(n1)
    
    context = {
        'n1': n1,
        'square': square,
        'fact': fact
    }
    
    return render(request, 'calculations/result.html', context)
