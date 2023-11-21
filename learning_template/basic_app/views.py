from django.shortcuts import render

# Create your views here.
def index(request):
    print("basicapp index view")
    context_dict={'text':'hello world','number':100}
    return render(request,"basic_app/index.html",context=context_dict)

def other(request):
    print("basicapp other view")
    return render(request,"basic_app/other.html")

def relative(request):
    print("basicapp relative view")
    return render(request,"basic_app/relative_url_templates.html")






