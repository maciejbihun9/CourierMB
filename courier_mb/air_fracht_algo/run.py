
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
    def run_algo(airports, packages):
        # init context airports
        AirportContext.init_airports_context(airports)

        # max payload - 27 000 kg, 3057 km
        # spalanie - 2.4l/ 100 km na każde 90kg
        # max. ilość paliwa - 43 000 l
        # fuel efficency: https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft
        boeing_757 = Aircraft("boeing 757", 57840, 43000, 27000, 850, FuelConsumption.BOEING_757)

        # get only one day packages
        # load it
        # create simulated annealing algorithm for that one day packages.
        trip_cost = 0
        # simulated annealing params
        temp = 1000

        cool_rate = 0.003

        # create init tour
        best_tour = None
        """ num_of_packages = int(random.normal(10000, 3000, 1)[0])
                    while num_of_packages < 5000 and num_of_packages > 15000:
                        num_of_packages = int(random.normal(10000, 3000, 1)[0])

                    packages = AirportContext.get_amount_of_packages(num_of_packages)
                    AirportContext.init_airports_with_packages(packages)
                    """
        while temp > 200:
            # generate random number of packages between given range
            AirportContext.init_airports_with_packages(packages)
            airports = AirportContext.get_airports()
            start_airport = AirportContext.get_airports()[0]
            boeing_757.load_packages(start_airport)
            current_airport = start_airport
            total_trip_costs = 0

            # create new tour
            first_tour = None
            # best_tour = None
            new_tour = Tour()
            while AirportContext.airports_contain_packages():
                # print("Packages to send status : {}".format(AirportContext.get_airports_status()))
                # print("Aircraft status: {}".format(boeing_757.get_magazine_status()))
                current_airport_dests = current_airport.get_airport_dests()
                # get random dest point
                rand_dest = randint(0, len(airports) - 1)
                next_airport = airports[rand_dest]
                while not next_airport.contain_packages():
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
                boeing_757.load_packages(next_airport)
                current_airport = next_airport
                # print("start from {}".format(current_airport.get_name()))


            airports_status = AirportContext.get_airports()
            # after all packages has been delivered
            # take one additional flight back to the base
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
            print("Current best tour: {}".format(best_tour.get_tour_cost()))

        print(" THE ALGORITHM RESULTS ")
        # print("first result number of flights taken : {}".format(first_tour.get_number_of_flights()))

        print("best result cost : {}".format(best_tour.get_tour_cost()))
        print("first result number of flights taken : {}".format(best_tour.get_number_of_flights()))

        print("The best tour : {}".format(best_tour.get_tour_cost()))
        return round(total_trip_costs, 2)














