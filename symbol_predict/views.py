from django.shortcuts import render
import sys
# sys.path.append(r""D:\沙崙\symbol_predict(css)\symbol_predict"")
# import water
from symbol_predict import water

def home(request):    
    return render(request, 'index.html')


def getPredictions(inpt_symbol):
    return water.water(inpt_symbol)
        

def result(request):
    inpt_symbol = str(request.GET['inpt_symbol'])
    

    result = getPredictions(inpt_symbol)

    return render(request, 'result.html', {'result':result})

    