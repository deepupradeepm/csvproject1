from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app1.forms import EmpForm
from .models import Emp
import csv


def showindex(request):
    form=EmpForm()
    return render(request,"index.html",{"form":form})


def savedetails(request):
    id=request.POST.get("idno")
    na=request.POST.get("name")
    sa=request.POST.get("sal")
    Emp(idno=id,name=na,sal=sa).save()
    form = EmpForm()
    return render(request, "index.html", {"form": form})


def downloadall(request):
    qs=Emp.objects.all()
    res=HttpResponse(content_type="text/csv")
    res['content_Disposition']='attachment;filename="emp.csv"'
    write=csv.writer(res)
    for x in qs:
        write.writerow([x.idno,x.name,x.sal])
    return res

def downloadoneemp(request):
    return render(request,"onecmd.html")

def downloadone(request):
    id=request.POST.get("idno")
    qs=Emp.objects.get(idno=id)
    if qs:
       res = HttpResponse(content_type="text/csv")
       res['content_Disposition'] = 'attachment;filename="emp.csv"'
       write = csv.writer(res)
       write.writerow([qs.idno,qs.name,qs.sal])
       return res
    else:
        return render(request,"oneemp.html",{"message":"invalid idno"})


def salbased(request):
    return render(request,"sal.html")


def saldownload(request):
    sal= request.POST.get("sal")
    qs = Emp.objects.filter(sal=sal)
    if qs:
        res = HttpResponse(content_type="text/csv")
        res['content_Disposition'] = 'attachment;filename="emp.csv"'
        write = csv.writer(res)
        for x in qs:
            write.writerow([x.idno, x.name, x.sal])
        return res
    else:
        return render(request, "sal.html", {"message": "invalid idno"})


def empfromtoid(request):
    qs=Emp.objects.all()
    return render(request, "emptf.html",{"data":qs})


def empftd(request):
    fidno = request.POST.get("fidno")
    tidno= request.POST.get("tidno")
    a=Emp.objects.get(idno=fidno)
    b=Emp.objects.get(idno=tidno)
    qs=Emp.objects.all()
    list=[]
    for x in qs:
        re=(x.idno)
        list.append(re)
    c=list.index(a.idno)
    d=list.index(b.idno)

    qse=Emp.objects.all()[c:d+1]
    if qse:
        res = HttpResponse(content_type="text/csv")
        res['content_Disposition'] = 'attachment;filename="emp.csv"'
        write = csv.writer(res)
        for x in qse:
            write.writerow([x.idno, x.name, x.sal])
        return res
    else:
        return render(request, "emptf.html", {"message": "invalid idno"})
