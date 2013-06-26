from django.shortcuts import render_to_response,redirect
from lc.apps.data.models import Meeting
from django.template import RequestContext
from django.db import backend, connections
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import send_mail, mail_admins
from django.views.decorators.http import require_http_methods, require_safe, condition


def index(request):
    print request
    meeting = Meeting.objects.filter(published=True).order_by('-id')

    paginator = Paginator(meeting, 2)

    page_num = request.GET.get('page', 1)

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page = paginator.page(1)

    ctx = {
        'page':page
    }
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))

def calendar(request):	
    return render_to_response('calendar.html', context_instance=RequestContext(request))


def calendar_inner(request, num=1):
    import pprint
    pprint.pprint(request)
    return render_to_response('calendar.html', context_instance=RequestContext(request))



def community(request):
    return render_to_response('community.html', context_instance=RequestContext(request))
