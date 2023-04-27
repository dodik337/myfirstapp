import eel
import pyowm

owm = pyowm.OWM("fa93075e9e2d4a82aef6ff80d81b38fb")

@eel.expose
def get_weather(place):
    mrg = owm.weather_manager()

    observation = mrg.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return 'В городе ' + place + " сейчас " + str(temp) + " градусов!"

eel.init('web')
eel.start('main.html', size=(700, 700))