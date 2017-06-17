from django.views.decorators.csrf import csrf_exempt
import json
from courier_mb.models import Package
from courier_mb.models import PackageType
from courier_mb.models import Airport
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from courier_mb.air_fracht_algo.run import Run
from courier_mb.air_fracht_algo.utils.utils import Utils
from django.http import JsonResponse
from django.http import HttpResponse
from courier_mb.air_fracht_algo.controller.airports_context import AirportContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
import logging


@csrf_exempt
@login_required
def get_airport(request):
    if request.is_ajax():
        if request.method == 'POST':
            received_json_data = json.loads(request.body)
            airport = Airport.objects.get(name=received_json_data["name"])
            # AirportContext.init_airports_context()
            # airports_list = AirportContext.get_airport_by_name(received_json_data["name"])
            print("name: {}".format(airport.get_name()))
            return JsonResponse({"latitude": airport.get_lat(), "longitude": airport.get_long()})

@login_required
def run_computations(request):
    if request.is_ajax():
        if request.method == 'GET':
            packages = Package.objects.all()
            airports = Airport.objects.all()
            logger = logging.getLogger("init_database_logger")
            value = Run.run_algo(airports, packages)
            # get from database all packages and then compute all prices value
            packages = list(packages)
            earnings = 0
            for package in packages:
                # package = Package(package.post_air_port, package.dest_air_port, package.weight)
                earnings += Utils.compute_pack_price(package)
            return JsonResponse({"value": value, "total_earnings": earnings})

@csrf_exempt
@login_required
def save_package(request):
    if request.is_ajax():
        if request.method == 'POST':
            received_json_data = json.loads(request.body)

            # create Airport object
            dest_airport = Airport.objects.get(name = str(received_json_data["dest_air_port"]))
            post_airport = Airport.objects.get(name = str(received_json_data["post_air_port"]))
            package_type = PackageType.objects.get(package_type = str(received_json_data["package_type"]))

            package = Package(weight=str(received_json_data["weight"]), post_air_port=post_airport,
                                dest_air_port=dest_airport, contents=str(received_json_data["contents"]),
                                package_type=package_type)
            package.save()
            return HttpResponse("Test object saved")
    return HttpResponse("Json object not found")

@login_required()
def logout_action(request):
    logout(request)
    return HttpResponseRedirect('/courierMB/login/')

@login_required()
def init_database(request):
    logger = logging.getLogger("init_database_logger")
    airports = Airport.objects.all()
    for airport in airports:
        AirportContext.add_airport(airport)
    packages = AirportContext.get_amount_of_packages(3000)
    AirportContext.init_airports_with_packages(packages)
    # save packages into database
    for package in packages:
        package.save()

    logger.info("context was initialized with airports and packages")
    return HttpResponse("Database was initialized!!!")

