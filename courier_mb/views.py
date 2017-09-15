from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import  render
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from .forms import SignUpForm, LoginForm, SenderForm, ReceiverForm
from django.shortcuts import redirect
from courier_mb.utils import Utils
from courier_mb.models import Airport
from courier_mb.models import Package
from courier_mb.air_fracht_algo.controller.airports_context import AirportContext
from django.contrib.auth.decorators import login_required


@login_required()
def get_home_page(request):
    return render(request, 'courier_mb/home.html')


@login_required()
def get_admin_panel(request):
    if request.user.is_superuser:

        # init AirportContext with airports
        airports = Airport.objects.all()
        AirportContext.init_airports_context(airports)
        num_of_packages_in_database = Package.objects.count()
        return render(request, 'courier_mb/admin_panel.html', {"database_status" : num_of_packages_in_database})
    else:
        status_code = 403
        return HttpResponse("Status code returned: {} .You are not allowed to see this page. Contact with service admin".format(str(status_code)), status=status_code)

@login_required()
def get_my_profile(request):
    return render(request, 'courier_mb/my_profile.html')


def get_signup_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name_surname = form.cleaned_data['your_name_surname']
            name_surname = name_surname.split(" ")
            user = User.objects.create_user(form.cleaned_data['your_username'], form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.first_name = name_surname[0]
            if len(name_surname) > 1:
                user.last_name = name_surname[1]
            user.save()
            return HttpResponseRedirect('/courierMB/home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'courier_mb/sgn_log_form.html', {'form': form, 'signup': True})


def get_login_form(request):
    # static variables
    no_user_message = 'There is no user with given credentials'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['your_username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/courierMB/home')
            else:
                messages.add_message(request, messages.INFO, no_user_message)
                return HttpResponseRedirect('/courierMB/login')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'courier_mb/sgn_log_form.html', {'form': form, 'signup': False})


@login_required()
def get_package_details_page(request):
    return render(request, 'package_details_page.html')


@login_required()
def get_send_package_page(request):
    # check whether it's valid:
    if request.method == 'POST':
        senderForm = SenderForm(request.POST)
        receiverForm = ReceiverForm(request.POST)
        print("post works!!!")
        if senderForm.is_valid() and receiverForm.is_valid():
            # sender_data = Utils.get_form_data(senderForm, senderForm.cleaned_data)
            # receiver_data = Utils.get_form_data(receiverForm, receiverForm.cleaned_data)
            print("valid")
            return get_package_type_page(request, senderForm.cleaned_data, receiverForm.cleaned_data)
            # return HttpResponseRedirect('/courierMB/package_details')
    else:
        senderForm = SenderForm()
        receiverForm = ReceiverForm()
    return render(request, 'courier_mb/transfer_details.html', {'senderForm': senderForm, 'receiverForm': receiverForm})


@login_required()
def get_package_type_page(request, sender_data, receiver_data):
    return render(request, 'courier_mb/transfer_details.html', {'sender_data': sender_data, 'receiver_data' : receiver_data})


