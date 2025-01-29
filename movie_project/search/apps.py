from django.apps import AppConfig
import os

class srchX(AppConfig):
    name = 'search'

    def ready(self):
        super().ready()
        self.modeFlag = os.environ.get("SEARCH_MODE", "basic")
        print("Search readiness check with mode:", self.modeFlag)
