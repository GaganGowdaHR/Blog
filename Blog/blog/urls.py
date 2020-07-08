from django.urls import path ,re_path
from blog.views import index
from blog.views import post_details,contact_view,post_form_view,post_edit_form_view,PostListView,PostDetailView,PostFormView,ContactFormView,PostFormUpdateView


urlpatterns = [
    # path('',index),
    path('',PostListView.as_view(), name = "posts"),
    # path("<int:id>",post_details),
    # path("<int:pk>",PostDetailView.as_view()),
    path("posts",PostFormView.as_view()),
    path("posts/<slug:slug>",PostFormUpdateView.as_view()),
    path("contact",ContactFormView.as_view(), name = "contactus"),
    path("<slug:slug>",PostDetailView.as_view(),name ="post-detail"),
    # path("contact",contact_view),
    
    # path("posts",post_form_view),


]