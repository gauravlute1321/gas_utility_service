from django.contrib import admin
from .models import ServiceRequest, RequestStatus

admin.site.register(ServiceRequest)
admin.site.register(RequestStatus)


