from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name='home'),
	path('add/', views.Addsong, name="add"),
	path('About/', views.About, name="About"),
	path('Privacy/', views.Privacy, name="privacy"),
	path('Contact/', views.Contact, name="Contact"),
	path('Login/', views.Login, name="Login"),
	path('Logout/', views.logoutUser, name="Logout"),
	path('Messages/', views.Message, name="Messages"),
	path('DeleteSong/', views.DeleteSong, name="DeleteSong"),
	path('confirm/<str:pk_test>', views.Confirm, name='confirm'),
	path('search', views.Search, name='search'),
	path('playlist/<str:pk_test>', views.Playlist, name="playlist"),
	path('video', views.Video, name="video"),
	path('glx_d831efaa1dcca0de109d5114b0c9f029.txt', views.Ad, name="glx_d831efaa1dcca0de109d5114b0c9f029.txt"),
	path('you/', views.you, name="you"),
	
]
