from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models  import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import SongForm
from django.forms import inlineformset_factory, modelformset_factory, formset_factory
import requests
from django.conf import settings
from isodate import parse_duration
import os.path
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorator import allowed_users
from django.utils.datastructures import MultiValueDictKeyError
import datetime
import requests
import vlc
import pafy

# Create your views here.
def you(request):
    url = "https://www.youtube.com/watch?v=1yNfzVABvCM"
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
    return render(request, 'todo/youtube.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['adim'])
def Addsong(request):
	alert = {}
	addsongset = modelformset_factory(Song, fields=('name', 'artist', 'year', 'audio'), extra=5)
	formset = addsongset(queryset=Song.objects.none())
	if request.method == "POST":
		formset = addsongset(request.POST,  request.FILES)
		if formset.is_valid():
			formset.save()
			alert = "uploaded"
		else:
		    alert = "not added"
	context = {'formset':formset, 'alert':alert}
	return render(request, 'mp3/add_song.html', context)


trend_PER_PAGE = 10
def Video(request):
	currentTime = datetime.datetime.now()
	currentTime.hour
	if currentTime.hour < 4:
		keypass = settings.YOUTUBE_DATA_API_1KEY
	elif 4 <= currentTime.hour < 6:
		keypass = settings.YOUTUBE_DATA_API_2KEY
	elif 6 <= currentTime.hour < 9:
		keypass = settings.YOUTUBE_DATA_API_3KEY
	elif 9 <= currentTime.hour < 12:
		keypass = settings.YOUTUBE_DATA_API_4KEY
	elif 12 <= currentTime.hour < 17:
		keypass = settings.YOUTUBE_DATA_API_5KEY
	elif 17 <= currentTime.hour < 21:
		keypass = settings.YOUTUBE_DATA_API_6KEY
	elif currentTime.hour >=21:
		keypass = settings.YOUTUBE_DATA_API_KEY
	else:
		keypass = settings.YOUTUBE_DATA_API_7KEY
	videos = []
	if request.method == "GET":
		try:
		    entry = request.GET['search']
		except MultiValueDictKeyError:
		    entry = 'new music'
		search_url = 'https://www.googleapis.com/youtube/v3/search'
		video_url = 'https://www.googleapis.com/youtube/v3/videos'
		search_params = {
			'part' : 'snippet',
			'q' : entry,
			'key' : keypass,
			'maxResults' : 3,
			'type' : 'video'

		}

		video_ids = []
		r = requests.get(search_url,params=search_params)

		results = r.json()['items']

		for result in results:
			video_ids.append(result['id']['videoId'])

		video_params = {
			'key' : keypass,
			'part' : 'snippet,contentDetails',
			'id': ','.join(video_ids),
			'maxResults' : 3,
		}
		r = requests.get(video_url, params=video_params)

		results = r.json()['items']
		for result in results:
			video_data = {
				'title' : result['snippet']['title'],
				'id' : result['id'],
				'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
				'duration' : parse_duration(result['contentDetails']['duration']),
				'thumbnail' : result['snippet']['thumbnails']['high']['url']
			}
			videos.append(video_data)
	context={'videos' : videos}

	return render(request, 'mp3/videodownloader.html', context)


def Playlist(request, pk_test):
	music = Song.objects.get(name=pk_test)
	name = music.artist
	context={'music':music,'name':name}
	return render(request, 'mp3/playlist.html', context)

def Search(request):
	currentTime = datetime.datetime.now()
	currentTime.hour

	if currentTime.hour < 4:
		keypass = settings.YOUTUBE_DATA_API_1KEY
	elif 4 <= currentTime.hour < 6:
		keypass = settings.YOUTUBE_DATA_API_2KEY
	elif 6 <= currentTime.hour < 9:
		keypass = settings.YOUTUBE_DATA_API_3KEY
	elif 9 <= currentTime.hour < 12:
		keypass = settings.YOUTUBE_DATA_API_4KEY
	elif 12 <= currentTime.hour < 17:
		keypass = settings.YOUTUBE_DATA_API_6KEY
	elif 17 <= currentTime.hour < 21:
		keypass = settings.YOUTUBE_DATA_API_7KEY
	elif currentTime.hour >=21:
		keypass = settings.YOUTUBE_DATA_API_KEY
	else:
		keypass = settings.YOUTUBE_DATA_API_5KEY
	videos = []
	status = {}
	if request.method == "GET":
		try:
		    entry = request.GET['search']
		except MultiValueDictKeyError:
		    entry = '2020 music'
		if entry:    
			status = Song.objects.filter(name__icontains=entry)[0:3]

		search_url = 'https://www.googleapis.com/youtube/v3/search'
		video_url = 'https://www.googleapis.com/youtube/v3/videos'
		search_params = {
			'part' : 'snippet',
			'q' : entry,
			'key' : keypass,
			'maxResults' : 3,
			'type' : 'video'

		}

		video_ids = []
		r = requests.get(search_url,params=search_params)

		results = r.json()['items']

		for result in results:
			video_ids.append(result['id']['videoId'])

		video_params = {
			'key' : keypass,
			'part' : 'snippet,contentDetails',
			'id': ','.join(video_ids),
			'maxResults' : 3,
		}
		r = requests.get(video_url, params=video_params)

		results = r.json()['items']
		for result in results:
			video_data = {
				'title' : result['snippet']['title'],
				'id' : result['id'],
				'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
				'duration' : parse_duration(result['contentDetails']['duration'])
			}
			videos.append(video_data)

	context={'videos' : videos,'status':status}
	return render(request, 'mp3/search.html', context)

def Home(request):
	return render(request, 'mp3/home.html')

def About(request):

	
		#artist = request.POST.get('artist')
		#song = request.POST.get('song')
	return render(request, 'mp3/about.html')

def Ad(request):

	
		#artist = request.POST.get('artist')
		#song = request.POST.get('song')
	return render(request, 'mp3/glx_d831efaa1dcca0de109d5114b0c9f029.txt')


def Privacy(request):

	
		#artist = request.POST.get('artist')
		#song = request.POST.get('song')
	return render(request, 'mp3/privacy.html')

def Contact(request):
	form = ContactForm()
	done = " "
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			done = "messages has been sent"

	context = {'form': form, 'done': done}
	return render(request, 'mp3/contact.html', context)

def Login(request):
	if request.method == "POST":
		username = request.POST.get('uname')
		password = request.POST.get('psw')

		user =authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('add')
		else:
			messages.info(request, "username or password is incorrect")

	return render(request, 'mp3/login.html')

def logoutUser(request):
	logout(request)
	return redirect('Login')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['adim'])
def Message(request):
	messag = Messages.objects.all().order_by("-id")
	

	page = request.GET.get('page', 1)
	trend_paginator = Paginator(messag, trend_PER_PAGE)
	try:
		messag = trend_paginator.page(page)
	except PageNotAnInteger:
		messag = trend_paginator.page(trend_PER_PAGE)
	except EmptyPage:
		messag = trend_paginator.page(trend_paginator.num_pages)

	context = {'contact': messag, 'trend': messag}
	
		#artist = request.POST.get('artist')
		#song = request.POST.get('song')
	return render(request, 'mp3/messages.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['adim'])
def DeleteSong(request):
	music = Song.objects.all().order_by("-id")

	context ={'music':music}

	return render(request, 'mp3/delete.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['adim'])
def Confirm(request, pk_test):
	title = "delete song"
	music = Song.objects.get(id=pk_test)
	if request.method == 'POST':
		music.delete()
		return redirect('DeleteSong')
	context = {'title':title,'song':music}
	return render(request, 'mp3/confirm.html', context)
