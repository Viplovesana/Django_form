from django.shortcuts import render,HttpResponse
from .models import Student
# Create your views here.

def home(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')
def form(req):
    if req.method == "POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        contact=req.POST.get('contact')
        dob=req.POST.get('dob')
        education=req.POST.getlist('education')
        gender=req.POST.get('gender')
        password=req.POST.get('password')
        image=req.FILES.get('image')
        file=req.FILES.get('file')
        discription=req.POST.get('discription')
        user = Student.objects.filter(email=email)
        if user:
            eml="Email id already exist"

            return render(req,'form.html',{'eml':eml})
        else:
            Student.objects.create(name=name,email=email,contact=contact,education=education,dob=dob,gender=gender,password=password,image=image,file=file,discription=discription)
            msg="Data save successfully (:"
            return render(req,"login.html",{"msg":msg})
    return render(req,"form.html")
def login(req):
    return render(req,'login.html')
def logindata(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        user = Student.objects.filter(email=email)
        if user:
            userdata=Student.objects.get(email=email)
            # print(userdata.name)
            # print(userdata.email)        
            # print(userdata.contact)
            # print(userdata.dob)
            # print(userdata.education)
            # print(userdata.gender)
            # print(userdata.password)
            # print(userdata.image)
            # print(userdata.file)
            # print(userdata.discription)
            pass1=userdata.password
            if password == pass1:
                data={'name':userdata.name,'email':userdata.email,'contact':userdata.email,'dob':userdata.dob,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.image,'file':userdata.file,'discription':userdata.discription}
                return render(req,"dashboard.html",{'data':data})
            else:
                msg= "Email and Password not matched"
                return render(req,'login.html',{"alert":msg})
        else:
            msg = "Email not register"
            return render(req,'form.html',{"msg":msg})
            
def dashboard(req):
    return render(req,"dashboard.html")
def logout(req):
    return render(req,"logout.html")
