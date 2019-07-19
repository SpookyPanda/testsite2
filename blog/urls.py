from django.urls import path, re_path
from . import views

urlpatterns = [
	path('',views.PostListView.as_view(),name='post_list'),
	path('about/',views.AboutView.as_view(),name='about'),
	re_path(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
	path('post/new/',views.PostCreateView.as_view(),name='new_post'),
	re_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(), name='edit_post'),
	re_path(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='delete_post'),
	path('drafts/',views.DraftListView.as_view(),name='post_drafts'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_delete, name='delete_comment'),
]