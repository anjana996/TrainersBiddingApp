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
from django.shortcuts import render
from trainers.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",trainerRegistraion,name="tregister"),
    path('thome/',trainerHome,name="uhome"),
    path('tsignin/',signIn,name="tsignin"),
    path('tprofile/',personalProfile,name="tprofile"),
    path('viewjobs/',viewJobs,name="viewjobs"),
    path('logout/',signOut,name="logout"),
    path('editpro/',editProfile,name="editpro"),
    path('viewpro/',viewProfile,name="viewprofile"),
    path('aviljob/',listJob,name="availjob"),
    path('bidding/',trainerBidding,name="bidding"),
    path('finalsubmit/',finalSubmit,name="fsubmit"),
    path('sentapplication/',sentApp,name="sentapp"),
    path('jobstatus/',jobStatus,name="jobstatus"),
    path('editdetails/',editDetails,name="editd"),
]
