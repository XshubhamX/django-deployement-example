from django.shortcuts import render
# Create your views here.
def base(request):
    return render(request,"base.html")
def index(request):
    return render(request,"index.html")
def main(request):
    dict={"text":"hey shubham","number":100}
    return render(request,"main.html",context=dict)
def other(request):
    return render(request,"other.html")
