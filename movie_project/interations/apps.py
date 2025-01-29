from django.apps import AppConfig
import os


class interX(AppConfig):
    name = 'interactions'

    def ready(self):
        super().ready()
        self.i_flag = os.environ.get("INTERACTIONS_MODE", "simple")
        print("Interactions init:", self.i_flag)
