from domain.electricity_reading import ElectricityReading


class ElectricityReadingService:
    def __init__(self, repository):
        self.electricity_reading_repository = repository
        return

    def store_reading(self, json):
        readings = list(map(lambda x: ElectricityReading(x), json['electricityReadings']))
        return self.electricity_reading_repository.store(json['smartMeterId'], readings)
