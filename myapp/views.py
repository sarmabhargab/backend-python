from django.shortcuts import render,redirect
from .models import Users
import datetime
import base64
# Create your views here.
def home(request):
    users = Users.objects.all()

    return render(request,'home.html',{'users':users})

def insert(request):
    if request.method == 'POST':
        name =request.POST['name']
        dob = request.POST['dob']
        address = request.POST['address']
        email = request.POST['email']
        time = datetime.datetime.now().strftime("%H:%M:%S")
        time_bytes = time.encode("ascii")
        sk = str(base64.b64encode(time_bytes))
        sk = sk[2:-1]



        user = Users(name=name,address=address,dob=dob,email=email,sk=sk)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request,'insert.html')
    return render(request,'home.html')

def delete(request,id):
    try:
        user = Users.objects.get(id=id)
        user.delete()
    except Users.DoesNotExist:
        user = None
    return redirect('/')
