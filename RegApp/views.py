from django.shortcuts import render # type: ignore
from django.shortcuts import redirect # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from .models import User

# Create your views here.
def main(request):
    return render(request, 'main.html')
    
def registerdUsers(request):
    users = User.objects.all()
    return render(request, 'registerdUsers.html', {'users': users})
# //Add fuction for delete and edit user using the two buttons in the registerdUsers.html file
def deleteUser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    users = User.objects.all()
    return redirect('/registerdUsers/', {'users': users})

#make table editable and add a button that appers in place of the edit icon "save" to save the changes
def editUser(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.index = request.POST.get('index')
        user.password = request.POST.get('password')
        user.save()
        users = User.objects.all()
        return redirect('/registerdUsers/', {'users': users})
    return redirect('/registerdUsers/', {'user': user})
   



@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        index = request.POST.get('index')
        password = request.POST.get('password')

        user = User(name=name, email=email, phone=phone, index=index, password=password)
        user.save()

        return render(request, 'registerUser.html', {'message': 'User registered successfully'})

    return render(request, 'registerUser.html')