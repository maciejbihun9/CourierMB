
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

"""
        Airport details:
        * airport name,
        * landing/take-off price,
        * noise price,
        * parking price(after free time, per 12 hours),
        * fuel cost: price/1l,
        * cargo price: price/1kg
        """
class Airport(models.Model):
    """
        def __init__(self, name: str, lat: float, long:  float, land_take_off_price, noise_price, park_price, fuel_cost, cargo_price, *args, **kwargs):
            self.name = name
            self.lat = lat
            self.long = long
            self.land_take_off_price = land_take_off_price
            self.noise_price = noise_price
            self.park_price = park_price
            self.fuel_cost = fuel_cost
            self.cargo_price = cargo_price
            self.airport_dests = []
            self.packages = []
            self.packs_dest = {}
    """

    name = models.CharField(max_length=25)
    lat = models.FloatField()
    long = models.FloatField()
    land_take_off_price = models.FloatField()
    noise_price = models.FloatField()
    park_price = models.FloatField()
    fuel_cost = models.FloatField()
    cargo_price = models.FloatField()


    def __init__(self,id, name: str, lat: float, long:  float, land_take_off_price, noise_price,
                 park_price, fuel_cost, cargo_price, *args, **kwargs):

        super(Airport, self).__init__(*args, **kwargs)
        self.id = id
        self.name = name
        self.lat = lat
        self.long = long
        self.land_take_off_price = land_take_off_price
        self.noise_price = noise_price
        self.park_price = park_price
        self.fuel_cost = fuel_cost
        self.cargo_price = cargo_price
        self.airport_dests = []
        self.packages = []
        self.packs_dest = {}

    def remove_packages(self, loaded_packs_from_airport: list):
        self.packages = [pack for pack in self.packages if pack not in loaded_packs_from_airport]
        for package in loaded_packs_from_airport:
            if package.get_dest().get_name() in self.packs_dest:
                self.packs_dest[package.get_dest().get_name()] = self.packs_dest[package.get_dest().get_name()] - 1

    def get_name(self):
        return self.name

    def add_package(self, package):
        """
        If destination points of that airport are not defined
        then add them to that list
        :param package: package to add to the airport
        :return: None
        """
        if package.get_dest() not in self.airport_dests:
            self.airport_dests.append(package.get_dest())
        if package.get_dest().get_name() in self.packs_dest:
            self.packs_dest[package.get_dest().get_name()] = self.packs_dest[package.get_dest().get_name()] + 1
        else:
            self.packs_dest[package.get_dest().get_name()] = 1
        self.packages.append(package)

    # get methods
    def get_start_land_price(self):
        """
        :return: take-off price + loud price
        """
        return self.land_take_off_price + self.noise_price

    def get_fuel_price(self):
        """
        :return: fuel price for 1 l
        """
        return self.fuel_cost

    def get_lat(self):
        return self.lat

    def get_long(self):
        return self.long

    def get_packages_weight(self):
        packages_weight = 0
        for package in self.packages:
            packages_weight += package.get_weight()
        return packages_weight

    def contain_packages(self):
        return len(self.packages) != 0

    def get_packages(self):
        return self.packages

    # get random packages
    def get_random_packages(self, packages_weight):
        packs_to_load = []
        loaded_packs_weight = 0
        while loaded_packs_weight < packages_weight:
            first_package = self.packages.pop()
            loaded_packs_weight += first_package.get_weight()
            packs_to_load.append(first_package)
        return packs_to_load

    def get_airport_dests(self):
        return self.airport_dests

    def get_pack_dests(self):
        return self.packs_dest


class PackageType(models.Model):
    package_type = models.CharField(max_length=10)

    def get_package_type(self):
        return self.package_type


class Package(models.Model):
    weight = models.FloatField(max_length=250)
    post_air_port = models.ForeignKey(Airport, related_name='post_air_port', default=None)
    dest_air_port = models.ForeignKey(Airport, related_name='est_air_port', default=None)
    contents = models.CharField(max_length=250)
    package_type = models.ForeignKey(PackageType)

    DELIVERED = 'DE'
    WAITING = 'WAIT'
    ON_THE_WAY = 'OTW'
    STATUSES = (
        (DELIVERED, 'Delivered'),
        (WAITING, 'Waiting'),
        (ON_THE_WAY, 'On the way'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default=WAITING,
    )

    def get_status(self):
        return self.status

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def get_dest(self) -> Airport:
        return self.dest_air_port

    def get_post(self) -> Airport:
        return self.post_air_port

    def get_weight(self) -> float:
        return self.weight











