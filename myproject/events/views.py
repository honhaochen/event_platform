from django.http import JsonResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import EventTab, EventCommentTab, EventImagesTab, EventLikesTab, EventParticipantTab
from auth.models import AuthTab

from json import loads
import math
import datetime
from cryptography.fernet import Fernet

EVENTS_PER_PAGE = 2
fernet = Fernet(Fernet.generate_key())

# Create your views here.
def event_view(request):
    if request.method == "POST":
        return JsonResponse({
            "error": "error_forbidden",
        })
    
    where_key = request.GET.get('key', None)
    page = int(request.GET.get('page', 0))
    current_page = int(request.GET.get('current_page', 0))
    isEOF = False
    if where_key is None:
        events = list(EventTab.objects.all().order_by('-start_time', 'id')[:EVENTS_PER_PAGE])
    else:
        processed_where_key = []
        try:
            processed_where_key = fernet.decrypt(where_key).decode().split("|")
        except Exception:
            return JsonResponse({
                "error": "error_key",
            })
        
        # handle EOF condition
        isEOF = processed_where_key[2] == 'True'
        if isEOF:
            events = list(EventTab.objects.all().order_by('-start_time', 'id')[:EVENTS_PER_PAGE])
        else:
            filter_start_time = datetime.datetime.fromisoformat(processed_where_key[0])
            filter_id = int(processed_where_key[1])
            events = None
            if page > current_page:
                offset = page - current_page 
                events = list(EventTab.objects.filter(Q(start_time__lte=filter_start_time) | Q(start_time=filter_start_time) & Q(id__gt=filter_id)) \
                    .order_by('-start_time', 'id')[(EVENTS_PER_PAGE * offset):(EVENTS_PER_PAGE * offset) + EVENTS_PER_PAGE])
            else:
                offset =  current_page - page
                events = list(EventTab.objects.filter(Q(start_time__gte=filter_start_time) | Q(start_time=filter_start_time) & Q(id__lt=filter_id)) \
                    .order_by('-start_time', 'id')[(EVENTS_PER_PAGE * offset):(EVENTS_PER_PAGE * offset) + EVENTS_PER_PAGE])
    if len(events) > 0:
        where_start_time = events[-1].start_time
        where_id = events[-1].id
    else:
        where_start_time = datetime.datetime(2022, 1, 1)
        where_id = 0
    
    total_pages = EventTab.objects.all().count() / EVENTS_PER_PAGE
    # construct event list
    events_resp = []
    for e in events:
        events_resp.append(
            {
                "id": e.id,
                "title": e.title,
                "description": e.description,
                "start_date": e.start_time.isoformat(),
                "end_date": e.end_time.isoformat(),
                "category": e.category,
                "location": e.location,
                "images": [i.image for i in list(EventImagesTab.objects.filter(event_id=e.id))],
                "participants": [p.name for p in list(EventParticipantTab.objects.filter(event_id=e.id))],
                "likes": [l.name for l in list(EventLikesTab.objects.filter(event_id=e.id))],
                "comments": [{
                    "name": c.name,
                    "comment": c.comment
                } for c in list(EventCommentTab.objects.filter(event_id=e.id))],
            }
        )

    key = where_start_time.isoformat() + "|" + str(where_id) + "|" + str(len(events) == 0)
    current_page_resp = 1
    print(page, isEOF)
    if page > 0 and not isEOF:
        current_page_resp = page

    return JsonResponse({
        "currentPage": current_page_resp,
        "totalPages": math.ceil(total_pages),
        "key": fernet.encrypt(key.encode()).decode(),
        "events": events_resp
    }) 

def event_comment(request):
    if request.method == "GET":
        return JsonResponse({
            "error": "error_forbidden",
        })
    
    request_data = loads(request.body)
    event_id = request_data['id']
    comment = request_data['comment']
    if event_id is None or comment is None:
        return JsonResponse({
            "error": "error_invalid_payload"
        })
    
    try:
        EventTab.objects.get(id=event_id)
    except ObjectDoesNotExist:
        return JsonResponse({
                "error": "error_no_event"
            })
    
    user = AuthTab.objects.get(id=request.user['user_id'])
    comment = EventCommentTab(event_id=event_id, name=user.name, comment=comment)
    comment.save()
    return JsonResponse({
        "comments": [{
                    "name": c.name,
                    "comment": c.comment
                } for c in list(EventCommentTab.objects.filter(event_id=event_id))],
    })

def event_participate(request):
    if request.method == "GET":
        return JsonResponse({
            "error": "error_forbidden",
        })
    
    request_data = loads(request.body)
    event_id = request_data['id']
    if event_id is None:
        return JsonResponse({
            "error": "error_invalid_payload"
        })
    
    try:
        EventTab.objects.get(id=event_id)
    except ObjectDoesNotExist:
        return JsonResponse({
                "error": "error_no_event"
            })

    user = AuthTab.objects.get(id=request.user['user_id'])
    participant = EventParticipantTab(event_id=event_id, name=user.name)
    participant.save()
    return JsonResponse({
        "participants": [p.name for p in list(EventParticipantTab.objects.filter(event_id=event_id))]
    })

def event_like(request):
    if request.method == "GET":
        return JsonResponse({
            "error": "error_forbidden",
        })
    
    request_data = loads(request.body)
    event_id = request_data['id']
    if event_id is None:
        return JsonResponse({
            "error": "error_invalid_payload"
        })
    
    try:
        EventTab.objects.get(id=event_id)
    except ObjectDoesNotExist:
        return JsonResponse({
                "error": "error_no_event"
            })

    user = AuthTab.objects.get(id=request.user['user_id'])
    participant = EventLikesTab(event_id=event_id, name=user.name)
    participant.save()
    return JsonResponse({
        "likes": [l.name for l in list(EventLikesTab.objects.filter(event_id=event_id))]
    })