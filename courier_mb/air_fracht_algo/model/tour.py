
from courier_mb.air_fracht_algo.model.flight import Flight

"""
Show statistics of the searching process.
* how much fuel we used,
* how many flights
* how many landing/start on different airports
"""
class Tour(object):
    """
    Tour can contain different number of airports
    * Before tour is defined we have to know the full number of airports with (1)
    * sum (1) packages weights
    * compute weight left
    """

    def __init__(self):
        self.flights = []
        self.tour_cost = 0

    def __str__(self):
        return

    def show_tour_process(self):
        for flight in self.flights:
            print (flight)

    def get_flights(self):
        return self.flights

    def add_flight(self, flight: Flight):
        self.flights.append(flight)

    def set_tour_cost(self, tour_cost: float):
        self.tour_cost = tour_cost

    def get_tour_cost(self):
        return self.tour_cost

    def get_tour_stats(self):
        used_fuel = 0
        tour_transport_history = []
        for flight in self.flights:
            used_fuel += flight.get_needed_fuel()
            tour_transport_history += flight.get_flight_transport()
        return used_fuel, tour_transport_history

    def get_number_of_flights(self):
        return len(self.flights)



