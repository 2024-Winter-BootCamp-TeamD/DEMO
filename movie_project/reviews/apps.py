from django.apps import AppConfig
import os

class revX(AppConfig):
    name = 'review'

    def ready(self):
        super().ready()
        self.rev_key = os.environ.get('SPECIAL_REVIEW_KEY', 'def_key')
        print("Review App init with key:", self.rev_key)
