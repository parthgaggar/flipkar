import uuid


class Car(object):

    def __init__(self, make, location, price, travelled, start_time=None, end_time=None):
        self.car = dict()
        self.car['make'] = make
        self.car['location'] = location
        self.car['price'] = price
        self.car['travelled'] = travelled
        self.car['start_time'] = start_time
        self.car['end_time'] = end_time


class Inventory(object):

    def __init__(self, inventory_json):
        self.inventory_list = {}

        for car in inventory_json['cars']:
            self.inventory_list[str(uuid.uuid1())] = Car(car["car_make"], car["car_location"], car["car_price"],
                                                    car["travelled"])
