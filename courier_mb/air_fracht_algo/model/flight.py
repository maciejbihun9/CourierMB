from courier_mb.air_fracht_algo.model.aircraft import Aircraft
from courier_mb.air_fracht_algo.utils.utils import Utils
from courier_mb.models import Airport


class Flight(object):
    """
    Flight is defined as transport between two cities.
    * Aircraft is tanked in the first city,
    * start and noise price are taken from company,
    * land and noise price are taken from land airport,
    * possible parking price is added here

    FLIGHT COST FUNCTION

    """

    def __init__(self, aircraft: Aircraft, airport_start: Airport, airport_dest: Airport):
        self.aircraft = aircraft
        self.airport_start = airport_start
        self.airport_dest = airport_dest
        self.dist = Utils.compute_dist(airport_start, airport_dest)


    # here define our cost function
    def get_flight_cost(self):
        return self.get_fuel_cost() + self.airport_start.get_start_land_price() + self.airport_dest.get_start_land_price()

    def get_needed_fuel(self):
        """
        :return: Much needed flight fuel in litres.
        """
        fuel_param = (self.get_dist() / 100) * (self.aircraft.get_total_weight() / 92)
        needed_fuel = 0
        if self.get_dist() < 1200:
            needed_fuel = self.aircraft.get_fuel_cons()[0] * fuel_param
        elif self.get_dist() > 1200 and self.get_dist() < 2000:
            needed_fuel = self.aircraft.get_fuel_cons()[1] * fuel_param
        else:
            needed_fuel = self.aircraft.get_fuel_cons()[2] * fuel_param
        return needed_fuel

    def get_fuel_cost(self):
        """
        :return: Fuel costs much needed for flight
        """
        return self.get_needed_fuel() * self.airport_start.get_fuel_price()

    def get_dist(self):
        """
        :return: Distance between airports
        """
        return self.dist

    def get_flight_transport(self):
        return self.aircraft.get_magazine_status()



