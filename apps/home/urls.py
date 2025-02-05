# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.views import TopicListView, NewspaperListView, RedactorListView, \
    TopicDetailView, NewspaperDetailView, RedactorDetailView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("topics/", TopicListView.as_view(), name='topic_list'),
    path("newspapers/", NewspaperListView.as_view(), name='newspaper_list'),
    path("redactors/", RedactorListView.as_view(), name='redactor_list'),
    path("topics/<int:pk>", TopicDetailView.as_view(), name="topic_detail"),
    path("newspapers/<int:pk>", NewspaperDetailView.as_view(), name="newspaper_detail"),
    path("redactors/<int:pk>", RedactorDetailView.as_view(), name="redactor_detail"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
