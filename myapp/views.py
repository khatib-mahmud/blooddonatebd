from django.core.checks import messages
from myapp.decorators import allowed_user, unauthenticated_user
from myapp.models import Donor
from django.shortcuts import redirect, render
from myapp import forms
from myapp.filters import DonorFilter
from .forms import DonorForm, CreateUserForm
from datetime import date
from django.contrib import messages

from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

def home(request):
    
    return render(request, 'index.html', {'title':'Home Page'})

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']

            group = Group.objects.get(name='client')
            user.groups.add(group)

            messages.success(request,"Account created for "+username)
            return redirect('login')

    return render(request, 'register.html', {'form':form})

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username or Password incorrect!")        
    return render(request, 'login.html', {})
    

def logout(request):
    auth_logout(request)
    return redirect('login')
    
    
def donorlist(request):
    donor_list = Donor.objects.order_by('name')
    myFilter = DonorFilter(request.GET,queryset=donor_list)
    donor_list = myFilter.qs
    # today = date.today()
    # l =[]
    # for d in donor_list:
    #     ld = today - d.lastdonationdate
    #     if ld.days<90:

    #         l.append('RED')
    #     else:
            
    #         l.append('GREEN')
   
    return render(request, 'donor_list.html', {'donor_list':donor_list , 'myFilter':myFilter,'title':'Donor List' })
 
def donorform(request):
     
    form = DonorForm()
    if request.method == 'POST':
        form = forms.DonorForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('donorlist')


    return render(request, 'be_a_donor.html', {'form':form , 'title':'Donor Form'})

@allowed_user(allowed_roles=['admin'])
def donorupdate(request,donor_id):
    donor_info = Donor.objects.get(pk=donor_id)
    form = forms.DonorForm(instance=donor_info)
    if request.method == 'POST':
        form = forms.DonorForm(request.POST,instance=donor_info)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request,"Info up to date")
           
    return render(request, 'donorupdate.html', {'form':form,'title':'Donor Update'})




def donorinfo(request,donor_id):
    donor_info = Donor.objects.get(pk=donor_id)
    today = date.today()
    # ld = today - donor_info.lastdonationdate

    # if ld.days<90:
    #     avail = "Not Available"
    # else:
    #     avail = "Available"
    


    return render(request, 'donorinfo.html', {'donor_info':donor_info,'today':today , 'title':'Donor Infromations'})


@allowed_user(allowed_roles=['admin'])
def donordelete(request,donor_id):

    donor_info = Donor.objects.get(pk=donor_id)
    if request.method == "POST":
        donor_info.delete()
        messages.success(request,"Donor removed succesfully")
        return redirect('donorlist')
          
    return render(request, 'donordelete.html', {'donor_info':donor_info})
    




def aboutus(request):

    return render(request, 'aboutus.html', {'title':'About Us'})



