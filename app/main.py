class Car:
    def __init__(self, comfort: int, clean : int, brand: str):
        self.comfort = comfort
        self.clean = clean
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_center: int, power: int,
                 avr_rating: int, count_of_ratings: int):
        self.distance_center = distance_center
        self.power = power
        self.avr_rating = avr_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        income = 0
        for car in cars:
            income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, auto: Car) -> float:
        return round(auto.comfort * (self.power - auto.clean)
                     * (self.avr_rating / self.distance_center),
                     1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean < self.power:
            price = self.calculate_washing_price(car)
            car.clean = self.power
            return price
        return 0

    def rate_service(self, mark: int) -> None:
        self.avr_rating = round((self.avr_rating
                                * self.count_of_ratings + mark)
                                / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
