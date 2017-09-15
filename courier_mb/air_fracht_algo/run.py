
from courier_mb.air_fracht_algo.controller.airports_context import AirportContext
from courier_mb.air_fracht_algo.controller.package_creator import PackageCreator
from courier_mb.air_fracht_algo.model.aircraft import Aircraft
from courier_mb.air_fracht_algo.model.flight import Flight
from courier_mb.air_fracht_algo.enums.fuel_cons import FuelConsumption
from courier_mb.air_fracht_algo.model.tour import Tour
import math
from numpy import *
from random import randint
import copy

class Run:

    @staticmethod
    def run_algo(packages):
        # init airports with packages
        AirportContext.init_airports_with_packages(packages)

        # max payload - 27 000 kg, 3057 km
        # spalanie - 2.4l/ 100 km na każde 90kg
        # max. ilość paliwa - 43 000 l
        # fuel efficency: https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft
        boeing_757 = Aircraft("boeing 757", 57840, 43000, 27000, 850, FuelConsumption.BOEING_757)

        # simulated annealing procces stemp
        temp = 1000

        # simulated annealing cooling rate
        cool_rate = 0.003

        # create init tour
        best_tour = None

        airports = AirportContext.get_airports()
        start_airport = AirportContext.get_airports()[0]
        while temp > 900:
            # generate random number of packages between given range
            boeing_757.load_packages(start_airport)
            current_airport = start_airport
            total_trip_costs = 0
            new_tour = Tour()
            # we travel until our aircraft contains packages
            while boeing_757.get_number_of_packages():
                rand_dest = randint(0, len(airports) - 1)
                next_airport = airports[rand_dest]

                # If we have airports that have packages to send...
                if AirportContext.airports_contain_packages():
                    # get airport that contains packages to send...
                    while not next_airport.contain_packages() or next_airport.get_name() == current_airport.get_name():
                        rand_dest = randint(0, len(airports) - 1)
                        next_airport = airports[rand_dest]
                # create flight for those two cities
                flight = Flight(boeing_757, current_airport, next_airport)
                new_tour.add_flight(flight)

                flight_cost = flight.get_flight_cost()
                total_trip_costs += flight_cost
                # reload packages for that dest point
                boeing_757.reload_packages(next_airport)
                mag_status = boeing_757.get_magazine_status()
                print("mag status : {}".format(mag_status))
                # load destination packages from this airport
                if next_airport.contain_packages:
                    boeing_757.load_packages(next_airport)
                current_airport = next_airport
                # print("start from {}".format(current_airport.get_name()))

            AirportContext.reload_packages()
            back_to_the_base_flight = Flight(boeing_757, current_airport, start_airport)
            total_trip_costs += back_to_the_base_flight.get_flight_cost()
            new_tour.set_tour_cost(total_trip_costs)
            if best_tour == None:
                best_tour = copy.deepcopy(new_tour)
                first_tour = copy.deepcopy(new_tour)
            else:
                if new_tour.get_tour_cost() < best_tour.get_tour_cost():
                    best_tour = copy.deepcopy(new_tour)
                else:
                    propability = math.exp((best_tour.get_tour_cost() - new_tour.get_tour_cost()) / temp)
                    r = random.random_sample()
                    if propability > r:
                        best_tour = copy.deepcopy(new_tour)
            temp -= temp * cool_rate
            print("current temp : {}".format(temp))
            print("Trip costs : {}".format(total_trip_costs))
            print("Current best tour: {}".format(new_tour.get_tour_cost()))

        print(" THE ALGORITHM RESULTS ")
        print("best result cost : {}".format(best_tour.get_tour_cost()))
        print("best result number of flights taken : {}".format(best_tour.get_number_of_flights()))

        print("The best tour : {}".format(best_tour.get_tour_cost()))
        return best_tour














