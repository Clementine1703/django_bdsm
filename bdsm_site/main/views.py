from unicodedata import name
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *

from django.conf import settings
from .forms import *
from django.core.mail import send_mail
from django.utils.safestring import mark_safe



def index(request):
    form = CallForm()
    result_list = []
    all_rooms = Rooms.objects.all()
    for i in range(all_rooms.count()):
        images = RoomsImages.objects.filter(rooms=all_rooms[i])
        urls = []
        counter = 0;
        for s in images:
            urls.append({'path':s.images.url, 'id': counter, 'slide_number': counter + 1})
            counter += 1;
        result_list.append({'this_room':all_rooms[i],'url_list': urls,'id': i})

    context = {
        'rooms': result_list,
        'form': form,
    }

    data = CallForm(request.POST or None)
    if data.is_valid():
        try:
            form_name = data.cleaned_data.get('name')
            form_number = data.cleaned_data.get('number')
            context['form_name'] = form_name
            context['form_number'] = form_number
            new_request = Request(name=form_name, number=form_number)
            new_request.save()
            return render(request, 'main/mail_success.html', context={'success': True})
        except Exception as e:
            return render(request, 'main/mail_success.html', context={'success': False})
            # send_mail('Новая заявка!', f'Имя: {form_name}<br>Номер телефона: {form_number}', settings.EMAIL_HOST_USER,
            #           [settings.EMAIL_HOST_USER], fail_silently=True)





    return render(request, 'main/index.html', context=context)


def rooms(request):
    form = CallForm()
    result_list = []
    all_rooms = Rooms.objects.all()
    for i in range(all_rooms.count()):
        images = RoomsImages.objects.filter(rooms=all_rooms[i])
        cost = RoomsCost.objects.filter(rooms=all_rooms[i])
        devices = RoomsDevices.objects.filter(rooms=all_rooms[i])
        accessories = RoomsAccessories.objects.filter(rooms=all_rooms[i])
        urls = []
        counter = 0;
        for image in images:
            urls.append({'path': image.images.url, 'id': counter, 'slide_number': counter + 1})
            counter += 1

        result_list.append({'this_room': all_rooms[i], 'url_list': urls, 'id': i, 'costs':cost, 'devices':devices, 'accessories': accessories})

        context = {
            'rooms': result_list,
            'form': form,
        }

        data = CallForm(request.POST or None)
        if data.is_valid():
            try:
                form_name = data.cleaned_data.get('name')
                form_number = data.cleaned_data.get('number')
                context['form_name'] = form_name
                context['form_number'] = form_number
                new_request = Request(name=form_name, number=form_number)
                new_request.save()
                return render(request, 'main/mail_success.html', context={'success': True})
            except Exception as e:
                return render(request, 'main/mail_success.html', context={'success': False})
                # send_mail('Новая заявка!', f'Имя: {form_name}<br>Номер телефона: {form_number}', settings.EMAIL_HOST_USER,
                #           [settings.EMAIL_HOST_USER], fail_silently=True)


    return render(request, 'main/rooms.html', context=context)


def rules(request):
    rules_data = SiteRules.objects.all()
    context = {'rules': rules_data}
    return render(request, 'main/rules.html', context=context)


def contacts(request):
    return render(request, 'main/contacts.html')
