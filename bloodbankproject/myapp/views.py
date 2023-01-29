from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from . import forms,models
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request,'home.html')

class Logins(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        unm=request.POST['unm']
        passs=request.POST['pass']
        data=models.MyUser.objects.filter(username__iexact=unm).filter(password__iexact=passs)
        if data:
            for dt in data:
                request.session['utype']=dt.usertype
                request.session['username']=dt.firstname+" "+dt.lastname
            return redirect('home')
        else:
            return HttpResponse("<h1>Invalid Credentials</h1>")

class Registration(View):
    def get(self,request):
        myforms=forms.MyUserForm
        return render(request,'register.html',{'myforms':myforms})
    def post(self,request):
        myforms=forms.MyUserForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('login')
        else:
            return HttpResponse("Invalid Data")

def logouts(request):
    logout(request)
    return redirect('login')


class AddComplaint(View):
    def get(self,request):
        myforms=forms.ComplaintForm
        return render(request,'addComplaint.html',{'myforms':myforms})
    def post(self,request):
        myforms=forms.ComplaintForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def showList(request):
    data=models.BloodBank.objects
    return render(request,'showcmplist.html',{'data':data})


class AddBloodBank(View):
    def get(self,request):
        myforms=forms.BloodBankForm
        return render(request,'addbank.html',{'myforms':myforms})
    def post(self,request):
        myforms=forms.BloodBankForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def showList(request):
    data=models.BloodBank.objects.all().order_by('bloodbankid')
    return render(request,'showBBlist.html',{'data':data})

class AddDonor(View):
    def get(self,request):
        myforms=forms.DonorForm
        return render(request,'adddonor.html',{'myforms':myforms})
    def post(self,request):
        myforms=forms.DonorForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def showList(request):
    data=models.Donor.objects.all().order_by('donorid')
    return render(request,'showDNlist.html',{'data':data})


class AddReceiver(View):
    def get(self,request):
        myforms=forms.ReceiverForm
        return render(request,'addreceiver.html',{'myforms':myforms})
    def post(self,request):
        myforms=forms.ReceiverForm(request.POST)
        if myforms.is_valid():
            myforms.save()
            return redirect('home')

def showList(request):
    data=models.Receiver.objects.all().order_by('receiverid')
    return render(request,'showRlist.html',{'data':data})

class UpdateBloodBank(View):
    def get(self,request,id):
        obj=get_object_or_404(models.BloodBank,bloodbankid=id)
        myforms=forms.BloodBankForm(instance=obj)
        return render(request,'updbb.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.BloodBank,bloodbankid=id)
        myforms=forms.BloodBankForm(request.POST,instance=obj)
        if myforms.is_valid():
            myforms.save()
            return redirect('showBBlist')
              
class DeleteBloodBank(View):
    def get(self,request,id):
        obj=get_object_or_404(models.BloodBank,bloodbankid=id)
        myforms=forms.BloodBankForm(instance=obj)
        return render(request,'delbb.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.BloodBank,bloodbankid=id)
        obj.delete()
        return redirect('showBBlist')

class Search(View):
    def get(self,request):
        return render(request,'search.html')
    def post(self,request):
        bg=request.POST['bg']
        ct=request.POST['ct']
        if(bg and not ct):
                data=models.Donor.objects.filter(bloodgroup__iexact=bg)
        elif(not bg and ct):
                data=models.Donor.objects.filter(city__iexact=ct)
        elif(bg and ct):
                data=models.Donor.objects.filter(bloodgroup__iexact=bg).filter(city__iexact=ct)
        else:
            data=models.Donor.objects.all()
        return render(request,'donorlist.html',{'mydata':data})

class UpdateDonor(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        myforms=forms.DonorForm(instance=obj)
        return render(request,'upddonor.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        myforms=forms.DonorForm(request.POST,instance=obj)
        if myforms.is_valid():
            myforms.save()
            return redirect('showDNlist')

class DeleteDonor(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        myforms=forms.DonorForm(instance=obj)
        return render(request,'deld.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Donor,donorid=id)
        obj.delete()
        return redirect('showDNlist')


class UpdateReceiver(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        myforms=forms.ReceiverForm(instance=obj)
        return render(request,'updreceiver.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        myforms=forms.RecieverForm(request.POST,instance=obj)
        if myforms.is_valid():
            myforms.save()
            return redirect('showRlist')
        
class DeleteReceiver(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        myforms=forms.ReceiverForm(instance=obj)
        return render(request,'delr.html',{'myforms':myforms})
    def post(self,request,id):
        obj=get_object_or_404(models.Receiver,receiverid=id)
        obj.delete()
        return redirect('showRlist')
