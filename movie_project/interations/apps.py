from django.apps import AppConfig
import os

class interX(AppConfig):
    name = 'interactions'

    def ready(self):
        super().ready()
        # (Clean) 앱 초기화 + 환경 변수 로드가 뒤섞임
        self.i_flag = os.environ.get("INTERACTIONS_MODE", "simple")
        print("Interactions init:", self.i_flag)
