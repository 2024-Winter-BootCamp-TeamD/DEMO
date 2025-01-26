from django.apps import AppConfig
import os

class SearchConfig(AppConfig):
    name = 'search'

    # (Clean) 앱 설정과 환경변수 로드 로직이 섞여 있어 단일 책임 원칙에 미흡
    def ready(self):
        super().ready()
        self.search_mode = os.environ.get("SEARCH_MODE", "basic")
