import json
from django.shortcuts import render
from .models import Semester, Subject, Notice

def home(request):
    return render(request, 'mainapp/home.html')

def semester_detail(request, semester_name):
    try:
        semester = Semester.objects.get(name__iexact=semester_name)
        semester_subjects = semester.subjects.all()
    except Semester.DoesNotExist:
        semester_subjects = []
    context = {
        'semester_name': semester_name.title(),
        'subjects': semester_subjects,
    }
    return render(request, 'mainapp/semester_detail.html', context)

def notices(request):
    notices_qs = Notice.objects.all().order_by('-date')
    notices_data = {
        'upcoming_programs': list(notices_qs.filter(notice_type='program')),
        'results': list(notices_qs.filter(notice_type='result')),
        'exam_dates': list(notices_qs.filter(notice_type='exam')),
        'holidays': list(notices_qs.filter(notice_type='holiday')),
        'class_schedules': list(notices_qs.filter(notice_type='schedule')),
    }
    # Prepare notices for calendar highlighting: date -> list of {title, type}
    calendar_notices = {}
    for notice in notices_qs:
        date_str = notice.date.strftime('%Y-%m-%d')
        calendar_notices.setdefault(date_str, []).append({'title': notice.title, 'type': notice.notice_type})

    context = {
        'notices': notices_data,
        'notices_json': json.dumps(calendar_notices),
    }
    return render(request, 'mainapp/notices.html', context)

def sign_in(request):
    return render(request, 'mainapp/sign_in.html')

def create_account(request):
    return render(request, 'mainapp/create_account.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
