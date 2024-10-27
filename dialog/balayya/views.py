from django.shortcuts import render
from django.http import HttpResponse

def D1(request):
        return HttpResponse (f"<p>chudu..... <br>oka vaipe chudu ... </p>")
def D2(request):
        return HttpResponse (f"<p>okadu naaku edurochina vadike rissku.....<br> nenu okadiki eduru vachinaa vadike riskuu<br> THOKKI PADESTHAAA..!!!</p>")
def D3(request):
        return HttpResponse (f"<p>nendi modhalu pettanu... <br> modaledithe.. vadili pettanuu...!</p>")


def nanda1(request,s):
    if s=="chiru1":
        return HttpResponse (f"<p>chudu..... <br>{s}oka vaipe chu...</p>")
    elif s=="chiru2":
        return HttpResponse (f"<p>chudu..... <br>{s}oka vaipe chu...</p>")
    elif s=="chiru3":
        return HttpResponse (f"<p>chudu..... <br>{s}oka vaipe chu...</p>")
def nanda2(request,s):
    if s=="pawan1":
        return HttpResponse (f"<p>chudu..... <br>{s}oka vaipe chu...</p>")
    elif s=="pawan2":
        return HttpResponse (f"<p>chudu..... <br>{s}oka vaipe chu...</p>")
    elif s=="pawan3":
        return  HttpResponse (f"<p>chudu..... <br>{s}oka vaipe chu...</p>")
