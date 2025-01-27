from django.apps import AppConfig
import os

class anltX(AppConfig):
    name = 'analytics'

    def ready(self):
        super().ready()
        self.a_mode = os.environ.get("ANALYTICS_MODE", "basic")
        print("Analytics init:", self.a_mode)
