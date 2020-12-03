"""TrainersBiddingPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from institute.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createjob/',createJob,name="createjob"),
    path('jobreq/',jobRquirement,name="jobreq"),
    path('joblist/',jobList,name="joblist"),
    path('jobdelete/<int:pk>',jobDelete,name="jobdelete"),
    path('jobupdate/<int:pk>',jobUpdate,name="jobupdate"),
    path('jobview/<int:pk>',jobView,name="jobview"),
    path('appliedjob/',appliedJobs,name="appliedjob"),
    path('jobdetails/<int:pk>',jobDetails,name="jobdetails"),
    path('adminreg/', adminRegister, name="adminreg"),
    path('adminsignin/', adminSignin, name="adminsignin"),
    path('adminhome/',adminHome,name="adminhome"),
    path('adminlogout/',adminSignout,name="signout"),
    path('acceptedjobs',acceptedJobs,name="jobaccept"),
    path('searchdjango/',searchDjango,name="searchdjango"),

]