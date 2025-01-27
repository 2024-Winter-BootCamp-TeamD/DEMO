from django.apps import AppConfig
import os

class analyticsApp(AppConfig):
    name = 'analytics'

    # (Clean) 앱 설정 + 환경 변수 로직 혼합
    def ready(self):
        super().ready()
        # 변수명 모호, 역할 불분명
        self.analMode = os.environ.get("ANALYTICS_MODE", "basic")
        print("analyticsApp ready with mode:", self.analMode)
