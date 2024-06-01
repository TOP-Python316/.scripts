from abc import ABC, abstractmethod


class WeatherStation:

    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def set_measurements(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity
        self.notify()

    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity


class Observer(ABC):

    @abstractmethod
    def update(self, weather_station):
        pass


class Display(Observer):

    def __init__(self, weather_station):
        self._weather_station = weather_station
        self._weather_station.attach(self)

    def update(self, weather_station):
        if weather_station == self._weather_station:
            t = self._weather_station.get_temperature()
            h = self._weather_station.get_humidity()
            print(f'Display: Temperature: {t}, Humidity: {h}')


class Statistician(Observer):

    def __init__(self, weather_station):
        self._weather_station = weather_station
        self._temperature_sum = 0
        self._temperature_count = 0
        self._weather_station.attach(self)

    def update(self, weather_station):
        if weather_station == self._weather_station:
            self._temperature_sum += self._weather_station.get_temperature()
            self._temperature_count += 1
            avg_t = self._temperature_sum / self._temperature_count
            print(f'Statistician: Average temperature: {avg_t}')


if __name__ == '__main__':
    weather_station = WeatherStation()
    display = Display(weather_station)
    statistician = Statistician(weather_station)
    weather_station.set_measurements(20, 60)
    weather_station.set_measurements(22, 55)
    weather_station.set_measurements(25, 45)