from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import ContactForm
from blog.forms import PostForm

from django.views import View
from blog.models import Post,Catagory
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from account.models import User
# Create your views here.

# def index(request,*args,**kwargs):
#     posts = Post.objects.filter(status = "P")
#     post_titles = [post.title for post in posts]
#     title_str = ("\n\n").join(post_titles)
#     return HttpResponse(title_str)

def index(request,*args,**kwargs):
    posts = Post.objects.filter(status = "P")
    return render(request,"blog/index.html",context = {"posts":posts})

# class PostListView(View):

#     def get(self,request,*args,**kwargs):
#         posts = Post.objects.filter(status = "P")    
#         return render(request,"blog/index.html",context= {"posts":posts})


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status = "P")
    template_name = "blog/index.html"
    context_object_name = "posts"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Catagory.objects.all()
        # context['author'] = Author.objects.all()

        return context


def post_details(request,id,*args,**kwargs):


    post = Post.objects.get(id = id)

    return render(request,"blog/details.html",context={"post":post})


# class PostDetailView(View):

#     def get(self,request,id,*args,**kwargs):
#         post = Post.objects.get(id = id)
        
#         return render(request,"blog/details.html",context={"post":post})

class PostDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Post
    # queryset = Post.objects.filter(status = "P")
    template_name = "blog/details.html"



def contact_view(request,*args,**kwargs):
    # print(request.GET)
    print(request.POST)
    if request.method == "GET":
        form = ContactForm()
        return render(request,"blog/contact.html",context = {"form":form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Thank You")
        else:
            return render(request,"blog/contact.html",context = {"form":form})



    form = ContactForm()
    return render(request,"blog/contact.html",context={"form":form})


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = "contact"
    template_name = "blog/contact.html"

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)



# class PostFormView(View):
#     def get(self,request,*args,**kwargs):
#         form = PostForm()
#         return render(request,"blog/post.html",context={"form":form})

#     def post(self,request,*args,**kwargs):
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data.get('image').image.__dict__)
#             form.save()
#             return HttpResponse("Thank You")
#         else:
#             return render(request,"blog/post.html",context={"form":form})


class PostFormView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    # model = Post
    # fields = ['title','content','status','catagory','image']
    login_url = "login"
    permission_required = 'blog.add_post'
    template_name = "blog/post.html"
    form_class = PostForm 

    def form_valid(self, form):
    # """If the form is valid, save the associated model."""
        print("Data is valid")
        print(form.cleaned_data)
        self.object = form.save()
        return super().form_valid(form)   

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print(type(self.request.user))
        user = User.objects.get(username = self.request.user )
        # print("Getting here")
        # print(type(self.object)) 
        kwargs.update(initial = {"author":user})
        return kwargs



class PostFormUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = 'login'
    permission_required = "blog.change_post"
    model = Post
    form_class = PostForm
    template_name = "blog/post.html"

    def test_func(self,*args,**kwargs):
        slug = self.kwargs.get("slug")
        # author = User.post_set.all()
        post = Post.objects.get(slug = slug)
        if self.request.user.get_username() == post.author.get_username():
            return True
        else:
            return False


def post_form_view(request,*args,**kwargs):
    if request.method == "GET":
        form = PostForm()
        return render(request,"blog/post.html",context={"form":form})

    else:
        print(request.POST)
        print(request.FILES)
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data.get('image').image.__dict__)
            form.save()
            return HttpResponse("Thank You")
        else:
            return render(request,"blog/post.html",context={"form":form})


def post_edit_form_view(request,id,*args,**kwargs):
    try :
        post = Post.objects.get(id = id)
    except:
        return HttpResponse("Invalid Post ID")

    if request.method == "GET":
        form = PostForm(instance = post)
        return render(request,"blog/post.html",context = {"form":form})
    else:    

        form = PostForm(request.POST,request.FILES,instance = post)
        if form.is_valid():
            form.save()
                    
        return render(request,"blog/post.html",context = {"form":form})


# def post_details(request,id,*args,**kwargs):
#     try:
#         post = Post.objects.get(id = id)
#         post_str = "{} \n\n {}".format(post.title,post.content)
#         return HttpResponse(post_str)
#     except:
#         return HttpResponse("Invalid ID")