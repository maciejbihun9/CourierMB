from courier_mb.air_fracht_algo.enums.fuel_cons import FuelConsumption
from courier_mb.models import Package
from courier_mb.air_fracht_algo.controller.airports_context import AirportContext

class Aircraft(object):
    """
    Aircraft specification:
    * name,
    * max fuel limit (l),
    * max loading capacity(kg)
    * avg. speed(km/h),
    * Fuel consumption coefficient
    """

    def __init__(self, name: str, self_weight: float, max_fuel_limit: int, load_cap: int, avg_speed: float, fuel_cons_level: FuelConsumption):
        self.name = name
        self.self_weight = self_weight
        self.max_fuel_limit = max_fuel_limit
        self.load_cap = load_cap
        self.avg_speed = avg_speed
        self.fuel_cons_level = fuel_cons_level
        self.number_of_packages = 0
        # counted in kilos
        self.total_packages_weight = 0
        self.packs_dest = {}

    def get_name(self) -> str:
        return self.name

    def get_self_weight(self) -> float:
        return self.self_weight

    def get_total_weight(self) -> float:
        return self.self_weight + self.total_packages_weight

    def get_fuel_cons(self) -> FuelConsumption:
        return self.fuel_cons_level

    def get_load_cap(self) -> float:
        return self.load_cap

    def contains_packages_for_airport(self, airport) -> bool:
        if self.packs_dest[airport.get_name()] != 0:
            return True
        else:
            return False


    def load_package(self, package: Package) -> bool:
        new_pack_weight = package.get_weight()
        if self.total_packages_weight + new_pack_weight < self.load_cap:
            if package.get_dest().get_name() in self.packs_dest:
                self.packs_dest[package.get_dest().get_name()] = self.packs_dest[package.get_dest().get_name()] + 1
            else:
                self.packs_dest[package.get_dest().get_name()] = 1
            package.set_status(Package.LOADED)
            self.total_packages_weight += new_pack_weight
            self.number_of_packages += 1
            return True
        else:
            return False

    def get_packages_weight(self) -> float:
        return self.total_packages_weight

    def get_packages_weight_for_dest(self, airport):
        """
        :param airport: Airport
        :return: Total weight of all packages that goes to the airport object
        """
        airport_dest_packages = [pack for pack in self.get_packages() if pack.get_dest().get_name() == airport.get_name()]
        total_weight = 0
        for package in airport_dest_packages:
            total_weight += package.get_dest()
        return total_weight


    def get_packages(self) -> list:
        """
        If package status from AirportContext is LOADED that means this package is on aircraft board
        :return: Packages from airport context which status is LOADED
        """
        return [package for package in AirportContext.get_packages() if package.get_status() == Package.LOADED]

    def load_packages(self, airport):
        """
        Load city dest packages until aircraft is full
        :param packages: Packages to load
        :return: None
        """
        print("Packages loading...")
        for package in airport.get_packages():
            if package.get_status() == Package.WAITING:
                loaded = self.load_package(package)
                if loaded == False:
                    break
        print("Done loading...")



    def reload_packages(self, airport):
        """
        Reload packages which destination point is this airport
        :param airport: Current airport
        :return: None
        """
        # decrease total packages weight
        for package in self.get_packages():
            if package.get_dest().get_name() == airport.get_name():
                self.total_packages_weight -= package.get_weight()
                package.set_status(Package.DELIVERED)
                self.number_of_packages -= 1
        self.packs_dest[airport.get_name()] = 0

    def get_magazine_status(self):
        """
        :return: Dict with loaded packages number for each airport destination
        """
        return self.packs_dest

    def clear_aircraft(self):
        """
        Remove all transport from aircraft
        :return: None
        """
        for package in AirportContext.get_packages():
            package.set_status(Package.WAITING)

    def get_number_of_packages(self):
        return self.number_of_packages
