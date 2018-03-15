from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

# display the signup page.
def signup(request):
    # logic for post method
    if request.method == 'POST':

        # check and confirm that all fields have been poulated.
        if len(request.POST['username']) > 0 and len(request.POST['email1']) > 0 and len(request.POST['email2']) > 0 \
                and len(request.POST['password1']) > 0 and len(request.POST['password2']) > 0:

            # check to see if email
            if request.POST['email1'] == request.POST['email2']:
                # check to see if password match
                if request.POST['password1'] == request.POST['password2']:
                    # Check if user already exists
                    try:
                        user = User.objects.get(username=request.POST['username'])
                        return render(request, 'accounts/signup.html', {'error': 'User already exists'})
                    # if user doesnt exist
                    except User.DoesNotExist:
                        # check if email exists
                        try:
                            email = User.objects.get(email=request.POST['email1'])
                            return render(request, "accounts/signup.html", {'error': 'Email already exists'})
                        # if email also doesnt exist
                        except User.DoesNotExist:
                            # Post user to Database
                            user = User.objects.create_user(request.POST['username'], request.POST['email1'],
                                                            password=request.POST['password1'])
                            login(request, user)
                            return redirect('index')

                else:
                    return render(request, 'accounts/signup.html', {'error': 'Passwords didn\'t match'})

            else:
                return render(request, 'accounts/signup.html', {'error': 'Emails didn\'t match'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'Some required fields are missing values'})

        return render(request, 'accounts/signup.html')

    else:

        # Runs on first load of the page.
        return render(request, 'accounts/signup.html')


# Login Pages
def loginview(request):
    # logic for post method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                if request.POST['next'] is not None:
                    return redirect(request.POST['next'])

            else:
                return redirect('index')

        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password invalid'})

    else:

        # Runs on first load of the page.
        return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/login.html', {'success': 'User Logged out. Sign back in?'})
    else:
        return render(request, 'accounts/login.html', {'error': 'Please use the logout button to logout'})