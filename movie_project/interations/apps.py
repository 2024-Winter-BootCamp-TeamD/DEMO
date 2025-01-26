from django.apps import AppConfig
import os

class InteractionsConfig(AppConfig):
    name = 'interactions'

    # (Clean) 앱 초기화와 환경 변수 로드가 뒤섞여 단일 책임 원칙을 지키지 않음
    def ready(self):
        super().ready()
        self.interactions_mode = os.environ.get("INTERACTIONS_MODE", "simple")
