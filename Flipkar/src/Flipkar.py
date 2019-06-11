from utils.utils import get_inventory_details_from_file
from model.inventory import Inventory

class Flipkar(object):

    def __init__(self):
        initial_inventory = get_inventory_details_from_file()
        self.inventory_list = Inventory(initial_inventory).inventory_list

    def get_available_cars(self, start_time, end_time):

        available_cars = []
        for car_id in self.inventory_list:
            car = self.inventory_list[car_id]
            car = car.car
            start = car['start_time']
            end = car['end_time']
            if start is None or end is None:
                available_cars.append((car_id, car))
            else:
                if start <= start_time <= end:
                    pass
                else:
                    available_cars.append((car_id, car))
        return available_cars

    def print_available_cars(self, start_time, end_time):

        available_cars = self.get_available_cars(start_time, end_time)

        for each_car in available_cars:
            print(each_car[1])

    def filter_by_parameters(self, start_time, end_time, make=None, location=None, price=None, travelled=None):

        available_cars = self.get_available_cars(start_time, end_time)

        if make is not None:
            available_cars = [car for car in available_cars if car[1]['make'] == make]

        if location is not None:
            available_cars = [car for car in available_cars if car[1]['location'] == location]

        if price is not None:
            available_cars = [car for car in available_cars if car[1]['price'] <= price]

        if travelled is not None:
            available_cars = [car for car in available_cars if car[1]['travelled'] <= travelled]

        if len(available_cars) == 0:
            return None
        return available_cars

    def print_filter_by_parameters(self, start_time, end_time, make=None, location=None, price=None, travelled=None):

        available_cars = self.filter_by_parameters(start_time, end_time, make, location, price, travelled)

        for each_car in available_cars:
            print(each_car[1])

    def book_car(self, start_time, end_time, make=None, location=None, price=None):

        available_cars = self.filter_by_parameters(start_time, end_time, make, location, price)

        if available_cars is None:
            return None
        else:
            car_id = available_cars[0][0]
            self.inventory_list[car_id].car["start_time"] = start_time
            self.inventory_list[car_id].car["end_time"] = end_time
            return car_id




    def cancel_booking(self, car_id):

        if car_id in self.inventory_list:
            self.inventory_list[car_id].car["start_time"] = None
            self.inventory_list[car_id].car["end_time"] = None
            return "SUCCESS"
        else:
            return "FAILED"


if __name__ == '__main__':

    flipkar = Flipkar()

    # getting available cars based on start and end time
    print("Available cars from 0hrs to 10hrs")
    flipkar.print_available_cars(0, 10)
    print("=================")
    # filter by parameters
    print("Available cars from 0hrs to 10hrs with make Honda")
    flipkar.print_filter_by_parameters(0, 10, make='Honda')
    print("=================")
    # book car
    print("Book honda cars from 0hrs to 10hrs")
    booking_id = flipkar.book_car(0, 10, make='Honda')
    print("Booking id:", booking_id)
    print("=================")
    # check available cars from 0 to 10
    print("Available cars from 20hrs to 30hrs")
    flipkar.print_available_cars(0, 10)
    print("=================")
    # check available cars from 20 to 30
    print("Available cars from 20hrs to 30hrs")
    flipkar.print_available_cars(20, 30)
    print("=================")
    print("Cancel booked car by booking id", booking_id)
    # cancel booking
    status = flipkar.cancel_booking(booking_id)
    print(status)
    print("=================")
    # check available cars
    print("Available cars from 0hrs to 10hrs")
    flipkar.print_available_cars(0, 10)
    print("=================")








