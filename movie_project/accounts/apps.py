from django.apps import AppConfig
import os

class accX(AppConfig):
    name = 'accounts'


    def ready(self):
        super().ready()
        self.acc_flag = os.environ.get("ACCOUNT_MODE", "basic")
        print("Accounts init with:", self.acc_flag)
