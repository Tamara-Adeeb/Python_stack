from django.shortcuts import redirect, render
from django.contrib import messages
from TV_show_app.models import *

def main(request):
    return redirect("shows/new")

def add_show(request):
    return render(request,"add_show.html")

def process(request):
    title = request.POST["title"]
    network = request.POST["network"]
    date = request.POST["release_date"]
    decs = request.POST["desc"]
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    create_show(title,network,date,decs)
    lastShow = Show.objects.last()
    id = lastShow.id
    return redirect('/shows/'+str(id))

def view(request,id):#for displaying the data induvjualy
    # selected_show = Show.objects.get(id=id)
    
    context = {
        "display_show" : Show.objects.get(id=id)
    }
    return render(request,"display.html",context)

def show_table(request):
    context = {
        'Shows':Show.objects.all()
    }
    return render(request,"all_show.html",context)

def edit(request,id):
    request.session["id"] = id
    context = {
    "edit_show": Show.objects.get(id=request.session["id"])
    }
    return render(request,"show_edit.html",context)

def update(request):
    show_id = request.session["id"]
    title = request.POST["title"]
    network = request.POST["network"]
    date = request.POST["release_date"]
    decs = request.POST["desc"]
    errors = Show.objects.validator(request.POST)
    update_show(show_id,title,network ,date,decs)
    return redirect('shows/'+str(show_id)+'/edit')

def delete(request,id):
    delete_id = id
    delete_show(delete_id)
    return redirect('/shows')