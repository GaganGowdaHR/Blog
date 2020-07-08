from django.shortcuts import render,redirect
from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
from account.forms import SignUpform, ProfileUpdateForm
# Create your views here.

class UserCreateView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpform                             
    success_url = "/blogs"


def profile_page_view(request):

    

    return render(request, 'account/profile.html')


def profile_update_view(request, *args, **kwargs):
    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/blogs')
    else:
        profile_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
       'profile_form' : profile_form
    }
    return render(request, 'account/profile-update.html',context)

