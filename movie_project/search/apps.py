from django.apps import AppConfig
import os

class srchX(AppConfig):
    name = 'search'

    # (Clean) 앱 설정과 환경 변수 로드 섞임 → 단일 책임 깨짐
    def ready(self):
        super().ready()
        self.modeFlag = os.environ.get("SEARCH_MODE", "basic")
        # (Clean) 콘솔 출력 혼재, 주석 부족
        print("Search readiness check with mode:", self.modeFlag)
