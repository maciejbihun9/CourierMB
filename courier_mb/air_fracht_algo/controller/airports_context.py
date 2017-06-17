
from courier_mb.models import Airport
# from courier_mb.air_fracht_algo.model.airport import Airport
from courier_mb.air_fracht_algo.controller.package_creator import PackageCreator
from courier_mb.air_fracht_algo.utils.utils import Utils
from numpy import *

# VERIFIED
class AirportContext:

    airports = []
    packages_to_send = 0

    @staticmethod
    def add_airport(airport: Airport):
        AirportContext.airports.append(airport)

    @staticmethod
    def get_airport_by_name(name: str):
        """
        :param name: passed airport name
        :return: airport object that matches given name
        """
        return [airport for airport in AirportContext.airports if airport.get_name() == name]

    @staticmethod
    def get_airport_at_index(index: int):
        """
        :param index:
        :return: Airport at specific position
        """
        try:
            return AirportContext.airports[index]
        except IndexError("Index out of airports range"):
            print("Try to use index between range: {} and {}".format(0, len(AirportContext.airports)))

    @staticmethod
    def init_airports_context(airports):
        """
        Init context with default airports with their credentials
        :return: None
        """
        for airport in airports:
            AirportContext.add_airport(airport)

    @staticmethod
    def get_amount_of_packages(num_of_packages: int):
        """
        :param num_of_packages: number of packages to create
        :return: random list of packages
        """
        return PackageCreator.create_random_packages(AirportContext.airports, num_of_packages)

    @staticmethod
    def init_airports_with_packages(packages: list):
        """
        :param num_of_packages: Amount of packages to create
        :return: None
        """
        number_of_packages_fetched = 0
        for airport in AirportContext.airports:
            print("Delivered packages packages : {}".format(number_of_packages_fetched))
            for package in packages:
                number_of_packages_fetched += 1
                if airport.get_name() == package.get_post().get_name():
                    AirportContext.packages_to_send += 1
                    airport.add_package(package)

    @staticmethod
    def get_airports() -> list:
        """
        :return: List of airports from main application context
        """
        return AirportContext.airports

    @staticmethod
    def airports_contain_packages() -> bool:
        """
        :return: True if airports from Context still contains packages to send
        """
        for airport in AirportContext.get_airports():
            if airport.contain_packages():
                return True
        return False

    @staticmethod
    def get_airports_status() -> int:
        """
        :return: How many packages to send left in all airports
        """
        packages_to_send = 0
        for airport in AirportContext.get_airports():
            packages_to_send += len(airport.get_packages())
        return packages_to_send

    @staticmethod
    def get_trip_price(packages: list):
        """
        :param packages: input list of packages to send
        :return: None
        """
        prices = 0
        for package in packages:
            pack_price = Utils.compute_pack_price(package)
            prices += pack_price
        return prices

    @staticmethod
    def get_airport_context_status():
        """
        :return: Number of packages for company left to send .
        """
        return AirportContext.packages_to_send








