from django.shortcuts import render,redirect
from users.forms import UserForm,UserProfileForm
from users.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

class IndexView(View):
    template = 'users/index.html'
    all_users = User.objects.all()

    def get(self,request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user_id:
            return render(request,self.template,{'active_user':active_user[0],'all_users':self.all_users})
        return render(request,self.template,{'all_users':self.all_users})

class LoginView(View):
    empty_form = UserForm()
    template = 'users/login.html'

    def get(self,request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user_id:
            return render(request,self.template,{'user_form':self.empty_form, 'active_user':active_user[0]})
        return render(request,self.template,{'user_form':self.empty_form})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        login_user = User.objects.filter(username=username)
        if login_user:
            if check_password(password, login_user[0].password):
                request.session.flush()
                request.session['user_id'] = login_user[0].id
                return redirect('/users/welcome')
        return render(request, self.template, {'error':'Username and/or password incorrect.  Please try again.', 'user_form':self.empty_form})

class RegisterView(View):
    empty_form = UserForm()
    template = 'users/login.html'

    def get(self,request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user:
            return render(request,self.template,{'user_form':self.empty_form,'active_user':active_user[0]})
        return render(request,self.template,{'user_form':self.empty_form})

    def post(self,request):
        submitted_form = UserForm(request.POST)
        print(submitted_form)
        if submitted_form.is_valid():
            username = submitted_form.cleaned_data.get('username')
            submitted_password = submitted_form.cleaned_data.get('password')
            password = make_password(submitted_password)
            new_user = User(username=username,password=password)
            new_user.save()
            request.session.flush()
            request.session['user_id'] = new_user.id
            return redirect('/users/welcome')
        return render(request,self.template,{'error':'Invalid input, please try again (password must be at least 7 characters long).', 'user_form':self.empty_form})

class WelcomeView(View):
    template = 'users/welcome.html'

    def get(self,request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user_id:
            request.session.set_expiry(500)
            return render(request, self.template,{'active_user':active_user[0]})
        return redirect('/users')

class LogoutView(View):
    template = 'users/logout.html'

    def get(self,request):
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user:
            return render(request,self.template,{'active_user':active_user[0]})
        return redirect('/users/login')

    def post(self,request):
        request.session.flush()
        return redirect('/users')

class UserView(View):
    template = 'users/account.html'

    def get(self,request,username):
        user = User.objects.get(username=username)
        profile_form = UserProfileForm(initial={'email':user.email,'about':user.about})
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user_id == user.id:
    # form = ComplimentForm(initial={'user':user})
    # compliments = user.compliment_set.all()
            return render(request,self.template,{'user':user, 'active_user':active_user[0],'profile_form':profile_form,'user':user})
    # ,'form':form,}) 'compliments': compliments})
        return redirect('/users/login')

    def post(self,request,username):
        user = User.objects.get(username=username)
        active_user_id = request.session.get('user_id')
        active_user = User.objects.filter(id=active_user_id)
        if active_user_id == user.id:
            updated_form = UserProfileForm(request.POST)
            if updated_form.is_valid():
                user.email = updated_form.cleaned_data.get('email')
                user.about = updated_form.cleaned_data.get('about')
                user.save()
                return redirect('/users/{}'.format(user.username))
            return render(request, self.template, {'error':'Invalid input; please try again','user':user,'profile_form':self.profile_form})
        return redirect('/users/login')
# def add(request,user_id):
#     user = User.objects.get(id=user_id)
#     username = user.username
#     compliment_form = ComplimentForm(request.POST)
#     compliment = compliment_form.save()
#     return redirect('/account/'+str(username))
