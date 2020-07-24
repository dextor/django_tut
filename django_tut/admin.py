from django.contrib import admin
# from django.urls import path, include
# from django.urls import reverse


class MyAdminSite(admin.AdminSite):
	# site_url = reverse('polls:index')
	site_url = '/polls'
	site_header = 'Dexter\'s Awesome Django Tutorial Admin'
	site_title = 'Dexter\'s Awesome Django Tutorial Admin'
# 

admin_site = MyAdminSite(name='myadmin')