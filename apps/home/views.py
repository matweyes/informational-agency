from django.contrib.auth.decorators import login_required
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Topic, Newspaper, Redactor


@login_required(login_url="/login/")
def index(request):
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()

    context = {
        "segment": "index",
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
    }

    return render(request, "home/index.html", context=context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class TopicListView(ListView):
    model = Topic
    template_name = "home/topic_list.html"
    context_object_name = "topic_list"
    queryset = Topic.objects.all().order_by("name")
    # paginate_by = 5


class TopicDetailView(DetailView):
    model = Topic
    template_name = "home/topic_detail.html"
    context_object_name = "topic"


class NewspaperListView(ListView):
    model = Newspaper
    template_name = "home/newspaper_list.html"
    context_object_name = "newspaper_list"
    queryset = Newspaper.objects.all().order_by("title")
    # paginate_by = 5


class NewspaperDetailView(DetailView):
    model = Newspaper
    template_name = "home/newspaper_detail.html"
    context_object_name = "newspaper"


class RedactorListView(ListView):
    model = Redactor
    template_name = "home/redactor_list.html"
    context_object_name = "redactors"
    queryset = Redactor.objects.all().order_by("username")
    # paginate_by = 5


class RedactorDetailView(DetailView):
    model = Redactor
    template_name = "home/redactor_detail.html"
    context_object_name = "redactor"


def tmp_page(request):
    html_template = loader.get_template('home/' + "tmp_page.html")
    return HttpResponse(html_template.render({}, request))
