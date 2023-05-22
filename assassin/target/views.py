from django.shortcuts import render

# Create your views here.
def list_target(request):
    return render(request, 'target/list_target.html')

def add_target(request):
    return render(request, 'target/add_target.html')

def delete_target(request):
    return render(request, 'target/delete_target.html')