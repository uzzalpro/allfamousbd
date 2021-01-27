from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from Product.models import Product, Images, Category, Comment
from django.contrib import messages
from ecomapp.models import Setting
from UserApp.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from UserApp.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'category': category,
               'setting': setting,}
    return render(request, 'user_login.html', context)




#def user_register(request):
    #return render(request, 'Register.html')


def user_logout(request):
    logout(request)
    return redirect('home')



def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password_raw=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password_raw)
            login(request, user)
            current_user=request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "user_img/avatar.jpg"
            data.save()



            return redirect('home')
        else:
            messages.warning(request, "Your new and repeat password in not matching .")

    else:
        form = RegisterForm()
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'category': category,
               'setting': setting,
               'form': form}
    return render(request,'user_register.html', context)


def userprofile(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {'category': category,
               'setting': setting,
               'profile': profile}
    return render(request,'user_profile.html', context)


@login_required(login_url='/user/login') #check login
def user_update(request):
    if request.method == 'POST':
    #request.user is user data
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your account has been updated!.")
            return redirect('userprofile')

    else:
        #category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        #"userprofile" model -> OneToOneField reletion with user
        profile_form = ProfileUpdateForm(instance=request.user.userprofile )
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    
    context = {'category': category,
               'setting': setting,
               'user_form': user_form,
               'profile_form': profile_form}
    return render(request,'userupdated.html', context)



@login_required(login_url='/user/login') #check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Important
            messages.success(request, "Your password has been updated!.")
            return redirect('userprofile')
        else:
            messages.error(
                request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('user_password')

    else:
        category = Category.objects.all()
        setting = Setting.objects.get(id=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'userpasswordupdate.html', {
            'form': form,
            'category': category,
            'setting': setting
        })



@login_required(login_url='/user/login')
def usercomment(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'setting': setting,
               'comment': comment

    }
    return render(request, 'usercomment.html', context)               




def comment_delete(request, id):
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id,id=id)
    comment.delete()
    messages.success(request, 'Your Comment is Successfully Delete')
    return redirect('usercomment')
