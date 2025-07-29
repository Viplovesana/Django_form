from django.shortcuts import render,HttpResponse
from .models import Student,Query
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
        confirmpass=req.POST.get('confirmpass')
        image=req.FILES.get('image')
        file=req.FILES.get('file')
        discription=req.POST.get('discription')
        user = Student.objects.filter(email=email)
        if user:
            eml="Email id already exist"
            return render(req,'form.html',{'eml':eml})
        else:
            if confirmpass==password:
             Student.objects.create(name=name,email=email,contact=contact,education=education,dob=dob,gender=gender,password=password,image=image,file=file,discription=discription,)
             msg="Data save successfully (:"
             return render(req,"login.html",{"msg":msg})
        
            else:
                pswd="password not matched!!"
                return render (req,'form.html',{'pswd':pswd})
    
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
            pass1=userdata.password
            if password == pass1:
                data={'id':userdata.id,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.dob,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.image,'file':userdata.file,'discription':userdata.discription          } 
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

def query(req,pk):
    userdata=Student.objects.get(id=pk)
    return render(req,"dashboard.html",{'data':userdata,'query':pk})

def querydata(req,pk):
    print(req.POST)
    print(pk)
    name=req.POST.get('name')
    email=req.POST.get('email')
    query=req.POST.get('query')
    print(name,email,query)
    Query.objects.create(name=name,email=email,query=query)
    userdata=Student.objects.get(id=pk)
    data={'id':userdata.id,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.dob,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.image,'file':userdata.file,'discription':userdata.discription} 
    email=data['email']
    aquery=Query.objects.filter(email=email)
    return render(req,"dashboard.html",{'data':data,'query':pk,'aquery':aquery})


def allquery(req,pk):
    userdata=Student.objects.get(id=pk)
    email=userdata.email
    aquery=Query.objects.filter(email=email)
    return render(req,'dashboard.html',{'data':userdata,'aquery':aquery})

def edit(req,id,pk):
    print(id,pk)
    editdata=Query.objects.get(id=id)
    userdata=Student.objects.get(id=pk)
    data={'id':userdata.id,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.dob,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.image,'file':userdata.file,'discription':userdata.discription} 
    return render(req,'dashboard.html',{'editdata':editdata,'data':data})

    
def update(req,id,pk):
    print("Hello........")
    if req.method=='POST':
        name=req.POST.get("name")
        email=req.POST.get("email")
        query1=req.POST.get("query")
        olddata=Query.objects.get(id=id)
        print(name,email,query1,olddata)
        olddata.query=query1
        olddata.save()
        aquery=Query.objects.filter(email=email)
        userdata=Student.objects.get(id=pk)
        data={'id':userdata.id,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.dob,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.image,'file':userdata.file,'discription':userdata.discription} 
    return render(req,'dashboard.html',{'aquery':aquery,'data':data})


def delete(req,id,pk):
    deletedata=Query.objects.get(id=id)
    deletedata.delete()
    userdata=Student.objects.get(id=pk)
    data={'id':userdata.id,'name':userdata.name,'email':userdata.email,'contact':userdata.contact,'dob':userdata.dob,'education':userdata.education,'gender':userdata.gender,'password':userdata.password,'image':userdata.image,'file':userdata.file,'discription':userdata.discription} 
    aquery=Query.objects.filter(email=userdata.email)
    return render(req,'dashboard.html',{'aquery':aquery,'data':data}) 


from django.db.models import Q

def search(req,pk):
    userdata=Student.objects.get(id=pk)
    sdata=req.POST.get('search')
    aquery=Query.objects.filter(Q(email=userdata.email) & Q(query__contains=sdata))
    return render(req,'dashboard.html',{'aquery':aquery,'data':userdata}) 




    













