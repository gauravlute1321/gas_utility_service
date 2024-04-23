from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def track_request(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_request.html', {'service_requests': service_requests})

@login_required
def manage_requests(request):
    if not request.user.is_staff:
        return redirect('track_request')
    service_requests = ServiceRequest.objects.all()
    return render(request, 'manage_requests.html', {'service_requests': service_requests})

@login_required
def view_request(request, request_id):
    service_request = ServiceRequest.objects.get(pk=request_id)
    return render(request, 'view_request.html', {'service_request': service_request})


