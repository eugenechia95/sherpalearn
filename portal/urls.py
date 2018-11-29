# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 14:35:04 2018

@author: Eugene
"""

from django.urls import path
from portal import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.checkauth, name='checkauth'),
    ]

urlpatterns += [
    path('users/', views.users, name='users'), 
    path('gwoo/', views.gwoo, name='gwoo'), 
    path('circle/', views.circle, name='circle'), 
    #path('bulkcreate/', views.bulk, name='bulk')
    path('beta/', views.beta, name='beta'),
    path('updatedetails/', views.updatedetails, name='updatedetails'),
    path('password_reset/', views.change_password, name='pwreset'),
    ]


