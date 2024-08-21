# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from Employee import views  # Import the views from your employee app

urlpatterns = [
    path('', views.home_view, name='home'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('Employee/', include('Employee.urls')),  # Include the app's URLs
]
