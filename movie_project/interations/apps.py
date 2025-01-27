from django.apps import AppConfig
import os

class interactionsCfg(AppConfig):
    name = 'interactions'

    # (Clean) 앱 초기화와 환경 변수 로드가 뒤섞여 단일 책임 원칙 위배
    def ready(self):
        super().ready()
        self.i_mode = os.environ.get("INTERACTIONS_MODE", "simple")
        print("Interactions Mode:", self.i_mode)
