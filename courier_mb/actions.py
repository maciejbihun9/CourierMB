

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
from courier_mb.mb_message import MBMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
import logging

actions_logger = logging.getLogger(MBMessage.ACTIONS_LOGGER)


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
            logger = logging.getLogger("init_database_logger")
            best_tour = Run.run_algo(packages)
            # get from database all packages and then compute all prices value
            packages = list(packages)
            best_tour_string = ""
            for flight in best_tour.get_flights():
                best_tour_string += str(flight.get_post().get_name()) + " -> "
            best_tour_string += 'Wroclaw'
            # earnings from packages
            earnings_from_packages = 0
            for package in packages:
                # package = Package(package.post_air_port, package.dest_air_port, package.weight)
                earnings_from_packages += Utils.compute_pack_price(package)
            earnings_from_packages = round(earnings_from_packages, 2)
            best_tour_cost = round(best_tour.get_tour_cost(), 2)
            total_earnings = earnings_from_packages - best_tour_cost
            total_earnings = round(total_earnings, 2)
            return JsonResponse({"value": best_tour_cost, "earnings_from_packages": earnings_from_packages,
                                 "best_trip": best_tour_string, "total_earnings": total_earnings})

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

@csrf_exempt
@login_required()
def add_to_database(request):
    if request.is_ajax():
        if request.method == 'POST':
            received_json_data = json.loads(request.body)
            # create Airport object
            number_of_packages = str(received_json_data["number_of_packages"])
            random_packages = AirportContext.get_amount_of_packages(int(number_of_packages))
            num_iterator = 0
            for package in random_packages:
                if num_iterator % 100 == 0:
                    print((str(num_iterator) + " " + MBMessage.PACKAGE_ADDED))
                package.save()
                num_iterator += 1
            print(MBMessage.PACKAGES_ADDED)
            num_of_packs = Package.objects.count()
            return JsonResponse({"num_of_packs": num_of_packs})
    return HttpResponse("Could not add object to the database")

@login_required()
def clear_database(request):
    Package.objects.all().delete()
    print(MBMessage.CLEAR_DATABASE)
    return JsonResponse({"num_of_packs": 0})

@csrf_exempt
@login_required()
def remove_packages(request):
    if request.is_ajax():
        if request.method == 'POST':
            received_json_data = json.loads(request.body)
            packs_to_delete = received_json_data["packs_to_delete"]
            packs_to_delete = int(packs_to_delete)
            packs_status = Package.objects.count()
            if packs_status < packs_to_delete:
                packs_to_delete = packs_status
            for i in range(packs_to_delete):
                Package.objects.all().first().delete()
            packs_status = Package.objects.count()
            return JsonResponse({"num_of_packs": packs_status})
