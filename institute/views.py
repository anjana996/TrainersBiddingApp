from django.shortcuts import render,redirect
from institute.forms import *
from institute.models import *
from trainers.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here
def adminRegister(request):
    form=InstituteRegister()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = InstituteRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminsignin")
        else:
            context["form"] = form
    return render(request, "insti/adminreg.html", context)
def adminSignin(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        psswd = request.POST.get("pwd")
        user = authenticate(request, username=username, password=psswd)
        if user is not None:
            login(request,user)
            return redirect("adminhome")
        else:
            messages.error(request,"username/password is incorrect")

    return render(request,"insti/adminsignin.html")
@login_required(login_url="adminsignin")

def adminSignout(request):
    logout(request)
    return redirect("adminsignin")
@login_required(login_url="adminsignin")

def adminHome(request):
    return render(request,"insti/adminhome.html")
@login_required(login_url="adminsignin")

def createJob(request):
    form=CreateJob()
    context={}
    context["form"]=form
    if request.method == "POST":
        form = CreateJob(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jobreq")
        else:
            context["form"] = form
            return render(request,"insti/createjob.html",context)
    return render(request, "insti/createjob.html", context)
@login_required(login_url="adminsignin")

def jobRquirement(request):
    form=JobReqForm()
    item=JobRequirements.objects.all()
    context={}
    context['items']=item
    context['form']=form
    if request.method=="POST":
        form = JobReqForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("joblist")
        else:
            context['form'] = form
            return render(request,"insti/jobreq.html",context)

    return render(request, "insti/jobreq.html", context)
@login_required(login_url="adminsignin")

def jobList(request):
    jobs=JobRequirements.objects.all()
    context={}
    context["jobs"]=jobs
    return render(request,"insti/joblist.html",context)
@login_required(login_url="adminsignin")

def jobDelete(request,pk):
    jobs=JobRequirements.objects.get(id=pk).delete()
    return redirect("joblist")
@login_required(login_url="adminsignin")


def jobUpdate(request,pk):
    jobs=JobRequirements.objects.get(id=pk)
    form=JobUpdateForm(instance=jobs)
    context={}
    context["jobs"]=jobs
    context["form"]=form
    if request.method=="POST":
        form = JobUpdateForm(instance=jobs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("joblist")
        else:
            context["form"]=form
            return render(request,"insti/jobupdate.html",context)
    return render(request, "insti/jobupdate.html", context)
@login_required(login_url="adminsignin")

def jobView(request,pk):
    jobs=JobRequirements.objects.get(id=pk)
    context={}
    context["jobs"]=jobs
    return render(request,"insti/jobview.html",context)
@login_required(login_url="adminsignin")

def appliedJobs(request):
    jobs=PersonalProfile.objects.filter(status="applied")

    context={}
    context["jobs"]=jobs
    return render(request,"insti/appliedjobs.html",context)
@login_required(login_url="adminsignin")

def acceptedJobs(request):
    jobs=PersonalProfile.objects.filter(status="accepted")
    context={}
    context["jobs"]=jobs
    return render(request,"insti/acceptedjobs.html",context)

@login_required(login_url="adminsignin")

def jobDetails(request,pk):
    jobs=PersonalProfile.objects.get(id=pk)
    amount=TrainerBidding.objects.get(user=jobs.user)
    amt=TrainerBidForm(instance=amount)
    form=PersonalProfileForm(instance=jobs)
    context={}
    # context["amount"]=amount
    context["amt"]=amt
    context["form"]=form
    if request.method=="POST":
        form = PersonalProfileForm(instance=jobs,data=request.POST)
        if form.is_valid():
               form.save()
               return redirect("jobaccept")
        else:
            form=PersonalProfileForm(request.POST)
            context["form"] = form

            return render(request,"insti/jobdetails.html",context)
    return render(request, "insti/jobdetails.html", context)


def searchDjango(request):
    jobs=PersonalProfile.objects.filter(skills="Django",status="applied")
    context={}
    context["jobs"]=jobs
    return render(request,"insti/jobfilter.html",context)
