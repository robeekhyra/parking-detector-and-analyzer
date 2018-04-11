from django.apps import AppConfig


class ParkingConfig(AppConfig):
    name = 'parking'

    def ready(self):
        from . import mosquitto
        mosquitto.client.loop_start()
