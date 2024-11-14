from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden , HttpResponse , JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact_Us , AddUser , UserLogin,UserRegister
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt






# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'accounts/profile/profile.html')

@login_required
def contact(request):
    return render(request, 'contact_us.html')

@login_required
def about_us(request):
    return render(request, 'accounts/profile/about_us.html')

def base(request):
    return render(request, 'base.html')




# def user_login(request):
#     if request.method == 'POST':
#         # Get the username and password from the form
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page
#             return redirect('profile_home')
#         else:
#             messages.error(request, 'Invalid username or password.')
            


    # If not a POST request or authentication failed, render the login page with the form
    # return render(request, 'registration/login.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')  # Corrected this line
#         password = request.POST.get('password') 
        
#         obj_login = UserLogin()

#         obj_login.username = username
#         obj_login.password = password
#         obj_login.save()


#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page or any other page
#             return redirect('profile_home')
#         else:
#             # Return an error message or render the login page again with an error message
#             messages.error(request, 'Invalid username or password.')
#             return render(request, 'registration/login.html', {'error': 'Invalid username or password.'})   
#     else:
#         # Render the login page
#         return render(request, 'registration/login.html')
@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        obj_contact = Contact_Us()

        obj_contact.name = name
        obj_contact.email = email
        obj_contact.message = message
        obj_contact.save()

        messages.success(request, 'Your message has been sent successfully')
        return redirect('home')

    return render(request, 'contact_us.html')
    


@login_required
def profile_home(request):
    if request.user.is_authenticated:
        
        return render(request, 'accounts/profile/profile.html')
    
    if not request.user.logged_in:
        return render(request, 'registration/login.html')

    return render(request,'registration/register.html')


# def user_register(request):
#     if request.method =='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         phone_number = request.POST['phone_number']
        

        # error = []

        
        # if len(username) < 6:
        #     error.append('Username must be at least 6 characters')

        # if len(password) < 6:
        #     error.append('Password must be at least 6 characters')

        # if password != confirm_password:
        #     error.append('Password do not match')

        # if len(phone_number) != 10:
        #     error.append('Phone number must be 10 digits')

        
    #     user = UserRegister()
    #     user.username = username
    #     user.email = email
    #     user.password = (make_password(password))
    #     user.confirm_password = confirm_password
    #     user.phone_number = phone_number
    #         # user = register.objects.create_user(username=username, email=email, password=password)
    #         # user.phone_number = phone_number
            
    #     user.save()
    #     messages.success(request, 'Your account has been created. You can login now.')
    #     return redirect('login')

    # else:
    #     return render(request, 'registration/register.html')
    
    # return render(request, 'registration/register.html', {'error': None})
            
# def user_register(request):
#     if request.method == 'POST':
#         username = request.POST('username')
#         email = request.POST('email')
#         password = request.POST('password')

#         # Server-side validation
#         if not (username and email and password):
#             return JsonResponse({'message': 'All fields are required'}, status=400)

#         if User.objects.filter(username=username).exists():
#             return JsonResponse({'message': 'Username already exists'}, status=400)

#         # Create new user
#         user = User.objects.create_user(username=username, email=email, password=password)

#         # Log in the new user
#         login(request, user)

#         return JsonResponse({'message': 'Registration successful'}, status=200)

#     return JsonResponse({'message': 'Method not allowed'}, status=405)       

@login_required
def user_profile(request):
    if request.user.is_authenticated:
            return render(request, 'accounts/profile/profile.html')

    return render(request, 'accounts/profile/profile.html')

def user_logout(request):
    logout(request)
    return redirect('index')



@login_required
def list_user(request):
    user = AddUser.objects.all()  # Retrieve all users from the database
    return render(request,"accounts/profile/user_list.html", {'user': user})

# add user 
@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone_number = request.POST['phone_number']


        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return redirect('add_user')
        
        obj_add= AddUser()
        obj_add.username = username
        obj_add.f_name = first_name
        obj_add.l_name = last_name
        obj_add.email = email
        obj_add.password = password
        obj_add.confirm_password = confirm_password
        obj_add.phone_number = phone_number
        obj_add.save()
        messages.success(request, 'User added successfully.')
        return redirect('users')

    
    return render(request, 'accounts/profile/add_user.html')



@login_required
def delete_user(request, id):
    # Retrieve the user object or return a 404 error if not found
    user = get_object_or_404(AddUser, id=id)

    if request.method == 'POST':
        # Delete the user
        user.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('users')  # Redirect to the appropriate URL after deletion
    
    # Render a confirmation page for deleting the user
    return render(request, 'delete_user_confirm.html', {'user': user})

@login_required
def delete_user_confirm(request, id):
    # Retrieve the user object based on the provided ID
    user = get_object_or_404(AddUser, id=id)

    # Render the delete_user_confirm.html template with the user data
    return render(request, 'delete_user_confirm.html', {'user': user})

@login_required
def update_user_confirm(request, id):
    user = AddUser.objects.get(id=id)   
    return render(request, 'update_user_confirm.html', {'user': user})
  



@login_required
def update_user(request, id):
    # Retrieve the user object from the database
    user = get_object_or_404(AddUser, id=id)
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Extract form data from request
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        # Update the user object with the new data
        user.username = username
        user.f_name = first_name
        user.l_name = last_name
        user.email = email
        
        # Save the updated user object
        user.save()
        
        # Add a success message
        messages.success(request, 'User updated successfully')
        
        # Redirect to a relevant page
        return redirect('update_user_confirm', id=id)
    
    # Render the update_user.html template with the user object
    return render(request, 'update_user.html', {'user': user})



from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def password_change(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Check if the old password is correct
        if not request.user.check_password(old_password):
            messages.error(request, 'Your old password was entered incorrectly.')
            return redirect('password_change')

        # Check if the new passwords match
        if new_password1 != new_password2:
            messages.error(request, 'The new passwords do not match.')
            return redirect('password_change')

        # Check if the new password is different from the old password
        if old_password == new_password1:
            messages.error(request, 'Your new password must be different from your old password.')
            return redirect('password_change')

        # Change the password
        request.user.set_password(new_password1)
        request.user.save()

        # Update the session by logging the user in again
        user = authenticate(username=request.user.username, password=new_password1)
        if user is not None:
            login(request, user)

        messages.success(request, 'Your password was successfully updated!')
        return redirect('password_change_done')

    return render(request, 'registration/password_change.html')

@login_required
def password_change_done(request):
    return render(request, 'registration/password_change_done.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(request.POST)
        if password!= confirm_password:
            return JsonResponse({'success': False, 'message': 'Passwords do not match.'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already taken.'})

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'success': True, 'message': 'Registration successful'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return render(request, 'registration/register.html')
    

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return JsonResponse({'success': True, 'message': 'Logged in successfully'})
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')