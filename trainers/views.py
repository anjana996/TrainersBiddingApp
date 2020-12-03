from django.shortcuts import render,redirect
from trainers.forms import *
from trainers.models import *
from institute.models import *
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def trainerRegistraion(request):
    form=TrainerRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tsignin")
        else:
            context["form"] = form
            return render(request, "trainer/trregister.html", context)

    return render(request,"trainer/trregister.html",context)

def signIn(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        psswd = request.POST.get("pwd")
        user = authenticate(request, username=username, password=psswd)
        if user is not None:
            login(request,user)
            return redirect("uhome")
        else:
            messages.error(request,"username/password is incorrect")

            return render(request,"trainer/tsignin.html")
    return render(request, "trainer/tsignin.html",)

@login_required(login_url="tsignin")

def signOut(request):
    logout(request)
    return redirect('tsignin')

@login_required(login_url="tsignin")

def trainerHome(request):
    return render(request,"trainer/uhome.html")

@login_required(login_url="tsignin")

def personalProfile(request):

    form=PersonalProfileForm(initial={"user":request.user})

    context={}
    context["form"]=form
    if request.method=="POST":
        form=PersonalProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("viewjobs")
        else:
            context["form"] = form
            return render(request, "trainer/tprofile.html", context)

    return render(request,"trainer/tprofile.html",context)

@login_required(login_url="tsignin")

def viewProfile(request):
    jobs=PersonalProfile.objects.get(user=request.user)
    context={}
    context["jobs"]=jobs
    return render(request,"trainer/profile.html",context)
@login_required(login_url="tsignin")

def editProfile(request):
    candidate=PersonalProfile.objects.get(user=request.user)
    print(candidate)
    form=PersonalProfileForm(instance=candidate)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=PersonalProfileForm(instance=candidate,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("uhome")
        else:
            context["form"] = form

            return render(request,"trainer/editprofile.html",context)

    return render(request, "trainer/editprofile.html", context)

@login_required(login_url="tsignin")

def viewJobs(request):
    userobj=PersonalProfile.objects.get(user=request.user.username)
    print(userobj.skills)
    jobs = JobRequirements.objects.filter(skills=userobj.skills)
    print(request.user.username)
    context = {}
    context["jobs"] = jobs
    return render(request,"trainer/viewjobs.html",context)
@login_required(login_url="tsignin")

def trainerBidding(request):
    form=TrainerBidForm(initial={"user":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TrainerBidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fsubmit")
        else:
            return render(request,"trainer/bidding.html",context)
    return render(request, "trainer/bidding.html", context)
@login_required(login_url="tsignin")


def finalSubmit(request):
    return render(request,"trainer/finalsubmit.html")
@login_required(login_url="tsignin")

def sentApp(request):
    return render(request,"trainer/sentapplication.html")
@login_required(login_url="tsignin")

def listJob(request):
    jobs = JobRequirements.objects.all()
    context = {}
    context["jobs"] = jobs
    return render(request, "trainer/joblist.html", context)
@login_required(login_url="tsignin")

def jobStatus(request):
    jobs=PersonalProfile.objects.filter(user=request.user)
    context={}
    context["jobs"]=jobs
    return render(request,"trainer/jobstatus.html",context)
@login_required(login_url="tsignin")

def editDetails(request):
    candidate=PersonalProfile.objects.get(user=request.user)
    print(candidate)
    form=PersonalProfileForm(instance=candidate)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=PersonalProfileForm(instance=candidate,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("fsubmit")
        else:
            context["form"] = form

            return render(request,"trainer/editprofile.html",context)

    return render(request, "trainer/editprofile.html", context)
