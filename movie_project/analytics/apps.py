from django.apps import AppConfig
import os

class AnalyticsConfig(AppConfig):
    name = 'analytics'

    # (Clean) 앱 초기화 로직과 환경변수를 뒤섞어 단일 책임 분리 미흡
    def ready(self):
        super().ready()
        self.analytics_mode = os.environ.get("ANALYTICS_MODE", "basic")