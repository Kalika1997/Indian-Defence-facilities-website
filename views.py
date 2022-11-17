from audioop import reverse
import django.contrib.auth.views as v
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, response,JsonResponse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import CreateView,UpdateView,DeleteView,View
from math import ceil

from sms.forms import LeaveForm, Register, MyLogin, Userprofile, Upprofile, Hospital
from .models import Employee,Hospi,Hospit, Timesheet, Leave,Status,Salary,Profiles,Canteen_Product, Orders


def home(request):
    if request.user.is_authenticated:
        master= 'employ.html'
        return render(request, 'home.html',{'master':master})
    else:
        master = 'master.html'
        return render(request, 'home.html',{'master':master})


def aboutus(request):
    if request.user.is_authenticated:
        return render(request, 'detail1.html')
    else:
        return render(request, 'detail.html')
def galary(request):
    if request.user.is_authenticated:
        return render(request, 'school_gallary.html')
    else:
        return render(request, 'school_gallary.html')

def rules(request):
    return render(request,'rules.html')
def contact(request):
    if request.user.is_authenticated:
        master = 'employ.html'
        return render(request, 'contact.html', {'master': master})
    else:
        master = 'master.html'
        return render(request, 'contact.html', {'master': master})

def admission(request):
    return render(request,'admission.html')


    # return render(request,'aboutus.html')
def about_hospital(request):
    if request.user.is_authenticated:
        master = 'hospital_nav.html'
        return render(request, 'aboutus.html', {'master': master})
    else:
        master = 'master.html'
        return render(request, 'aboutus_hospital.html', {'master': master})

    # return render(request,'aboutus_hospital.html')
def medical(request):

    return render(request,'medical_process.html')
@login_required(login_url='sms:login')
def School_home(request):
    if request.user.is_authenticated:
        master = 'employ.html'

    else:
        master = 'master.html'
    new='new'
    old='old'
    return render(request,'armySchool.html',{'old':old,'new':new,'master':master})

def School(request,slug):
    print('slug',slug)
    if request.user.is_authenticated:
        master = 'employ.html'

    else:
        master = 'master.html'

    new=request.GET.get(slug)
    print('slug',new)

    return render(request,'schools.html',{'cant':slug,'master':master})
def School_details(request,slug):
    print('slug',slug)
    if request.user.is_authenticated:
        master = 'employ.html'

    else:
        master = 'master.html'

    new=request.GET.get(slug)
    print('slug',new)

    return render(request,'schooldetail.html',{'cant':slug,'master':master})

#@login_required(login_url='sms:login')
# class Melitory_home(View):
#     def get(self, request):
#         form = Hospital(None)
#         return render(request, 'melitoryHospital.html', {'hos': form})
#



        # omereturn redirect('sms:militory_home')
@login_required(login_url='sms:login')
def Canteen_home(request):
    if request.user.is_authenticated:
        master = 'employ.html'

    else:
        master = 'master.html'

    new='new'
    old='old'
    products = Canteen_Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products,'master':master}
    return render(request,'armyCanteen.html',params)

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request, 'checkout.html')
@login_required(login_url='sms:login')
def armyHospital(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '')
        age=request.POST.get('age', '')
        bg=request.POST.get('bg', '')
        gender=request.POST.get('gender', '')

        phone=request.POST.get('phone', '')
        problem = request.POST.get('problem', '')

        order = Hospit( user_id=request.user,name=name, email=email, address= address, age=age, bg=bg, gender=gender, phone=phone,problem=problem)
        order.save()
        messages.success(request, 'Details Added Successfully,Check Your Appointment below')
        print(gender)
        thank=True
        id=order.book_id
        return render(request, 'melitoryHospital.html', {'thank':thank,'name':'arbaz', 'id':id})
    return render(request, 'melitoryHospital.html')
@login_required(login_url='sms:login')
class  Hospital_form(CreateView):
    login_url = 'sms:admin_login'
    template_name = 'melitoryHospital.html'
    context_object_name = 'form'
    success_url = 'sms:hospital'
    model=Hospit
    fields = ['name','address','age','email','bg','gender','problem']
    def form_valid(self, form):
        data=form.save(commit=False)
        data.user_id=self.request.user
        data.save()
        name='arrbaz'
        # d=Hospitals.objects.filter(u_id=self.request.user)


        messages.success(self.request, 'Details Added Successfully,Check Your Appointment below')

        return render(self.request, 'melitoryHospital.html', {'name':name})

def mybooking(request):
    books=Hospit.objects.filter(user_id=request.user)
    a=books.count()
    r=range(a)
    print(books)
    context = {
        'val':books,
        'num':r
    }



    return render(request,'mybooking.html',context)

@staff_member_required
def Admin_home(request):
    return render(request,'admin_home.html')
class Emp_login(View):
    def get(self,request):
        form=MyLogin(None)
        return render(request,'login.html',{'form':form})


    def post(self,request):
        form = MyLogin(request.POST)
        if form.is_valid():
            u = form.cleaned_data['UserName']
            p = form.cleaned_data['Password']
            v = authenticate(username=u, password=p)
            n=request.GET.get('next',None)
            print('form valid')


            if v is not None and v.is_active and not v.is_staff:
                print('login')



                login(request, v)


                if n:
                    return redirect(n)
                else:
                    print('home')
                    try:
                        if request.user.profile:
                            print('profile')
                            return redirect('sms:home')
                    except:
                        print('not exist')
                        return redirect('sms:add_profile')





                return redirect('sms:home')
            else:
                if v.is_staff:
                    print('staff')
                    messages.warning(request, 'Please Enter Valid Username and Password')

                print('form invalid')





        else:
            print('invalid')




        return render(request, 'login.html', {'form': form})

class Admin_login(View):
    def get(self,request):
        form=MyLogin(None)
        return render(request,'admin_login.html',{'form':form})


    def post(self,request):
        form = MyLogin(request.POST)
        if form.is_valid():
            u = form.cleaned_data['UserName']
            p = form.cleaned_data['Password']
            v = authenticate(username=u, password=p)
            n=request.GET.get('next',None)


            if v is not None and v.is_active and v.is_staff:




                login(request, v)
                print(u)
                if n:
                    return redirect(n)
                else:
                    return redirect('sms:admin_home')
            messages.warning(request, 'Please Enter Valid Username and Password')
            return render(request, 'admin_login.html', {'form': form})

class Admin_signup(View):
    def get(self,request):
        form=Register(None)
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form=Register(request.POST)
        if form.is_valid():

            data=form.save(commit=False)

            p = form.cleaned_data['Password']
            data.set_password(p)
            data.is_staff = True

            data.save()

            return redirect('sms:admin_login')

        return render(request, 'register.html',{'form': form})

class Emp_signup(View):
    def get(self,request):
        form=Register(None)
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form=Register(request.POST)
        if form.is_valid():

            data=form.save(commit=False)
            u = form.cleaned_data['username']

            p = form.cleaned_data['Password']

            data.set_password(p)
            val = authenticate(username=u, password=p)
            u_form = Profiles(user=val)
            u_form.save()



            data.save()

            return redirect('sms:login')

        return render(request, 'register.html',{'form': form})

class logoutpage(View):
    def get(self,request):
        logout(request)
        return redirect('sms:home')




@login_required(login_url='sms:admin_login')




@login_required(login_url='sms:login')
def profile(request):
    if request.method=='POST':
        u_form=Userprofile(request.POST,instance=request.user)
        p_form=Upprofile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'user creation')
            return redirect('sms:profile')
    else:
        if request.user.profile:
            u_form = Userprofile(instance=request.user)
            print(u_form)
            p_form = Upprofile(instance=request.user.profile)
            context = {

                'u_form': u_form,
                'p_form': p_form
            }
            return render(request, 'userprofile.html', context)
            print('not ex')
        return redirect('sms:add_profile')
    return redirect('sms:profile')


class Add_profile(UpdateView):
    login_url = 'sms:admin_login'
    def get(self, request):
        u_form = Userprofile(request.POST, instance=request.user)
        p_form = Upprofile(request.POST, request.FILES)
        context = {

            'u_form': u_form,
            'p_form': p_form
        }


        return render(request, 'addprofile.html', context)

    def post(self, request):
        u_form = Userprofile(request.POST, instance=request.user)
        p_form = Upprofile(request.POST, request.FILES)
        context = {

            'u_form': u_form,
            'p_form': p_form
        }
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'yuvgyu')
            return redirect('sms:home')

        return render(request, 'addprofile.html', context)



def User_manage(request):
    u=User.objects.filter(is_superuser=False)




    return render(request,'user.html',{'val':u})

class Edit_User(LoginRequiredMixin,UpdateView):
    login_url = 'sms:admin_login'
    template_name = 'add.html'
    model = User
    fields = ['first_name','last_name','username','email','is_active']
    def form_valid(self, form):
        form.save()
        return redirect('sms:user')




