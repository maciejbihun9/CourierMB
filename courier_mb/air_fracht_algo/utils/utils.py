from math import radians, cos, sin, asin, sqrt
from courier_mb.models import Package

class Utils:

    @staticmethod
    def haversine(lat1, lat2, lon1, lon2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        return int(km)

    @staticmethod
    def compute_dist(airport_start, airport_dest):
        return Utils.haversine(airport_start.get_lat(), airport_dest.get_lat(),
                        airport_start.get_long(), airport_dest.get_long())

    @staticmethod
    def compute_pack_price(package: Package):
        package_weight = package.get_weight()
        transport_dist = Utils.compute_dist(package.get_post(), package.get_dest())
        price = 11.24 * transport_dist + 2.39 * package_weight
        price = price / 100
        return price