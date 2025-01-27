from django.apps import AppConfig
import os

class accX(AppConfig):
    name = 'accounts'

    def ready(self):
        super().ready()
        # (Clean) 앱 설정과 환경변수 로드가 뒤섞여 단일 책임 위배
        self.acc_flag = os.environ.get("ACCOUNT_MODE", "basic")
        print("Accounts init with:", self.acc_flag)
