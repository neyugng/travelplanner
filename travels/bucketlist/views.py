from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BucketList, BucketListLocation
import datetime

def index(request):
    context = {}
    context['bucket_lists'] = BucketList.objects.all()
    return render(request, "bucketlist/lists.html", context)


def add_list(request):
    context = {}

    if request.method == "POST":
        pass

    return render(request, "bucketlist/add_list.html", context)


def add_location(request, list_id):
    context = {}

    this_list = BucketList.objects.get(id=list_id)
    
    if request.method == 'POST':
        BucketListLocation.objects.create(
            item=request.POST['location_name'],
            list_num=list_id,
        )

    context['list_id'] = list_id

    return render(request, "bucketlist/add_location.html", context)


def create_list(request):
    if request.method == 'POST':
        this_bucketlist = BucketList(
            name=request.POST['list_name'],
            description=request.POST['list_description'],
        )
        this_bucketlist.save()

    return redirect('bucketlist/index')


def create_location(request, list_id):
    if request.method == 'POST':
        this_bucketlistlocation = BucketListLocation(
            item=request.POST['location_name'],
            list_num=list_id
        )
        this_bucketlistlocation.save()

    return redirect('bucketlist/index')


def view_list_locations(request, list_id):
    context = {}
    this_list = BucketList.objects.get(id=list_id)
    context['list_name'] = this_list.name
    context['list_id'] = this_list.id

    queryset = BucketListLocation.objects.filter (
        list_num = list_id
    )
    context['queryset'] = queryset

    return render(request, "bucketlist/list-locations.html", context)
    


def delete_list(request, list_id):
    this_list = BucketList.objects.get(id=list_id)
    this_list.delete()
    return redirect('bucketlist/index')


def delete_location(request, location_id):
    this_location = BucketListLocation.objects.get(id=location_id)
    this_location.delete()
    return redirect('bucketlist/index')


def home(request):
	return render(request, "bucketlist/index.html", {})


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)