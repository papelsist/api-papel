from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from .builders.ventasReport import VentasReport
# Create your views here.


@csrf_exempt
def report(request):
    report = VentasReport()
    reportPdf = report.run()   
    return reportPdf
    #return JsonResponse("Success", safe=False)
