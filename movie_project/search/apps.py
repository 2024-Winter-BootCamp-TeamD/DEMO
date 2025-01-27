from django.apps import AppConfig
import os

class searchingStuff(AppConfig):
    name = 'search'

    # (Clean) 앱 초기화 + 환경 변수 로드가 뒤섞여, 단일 책임 미흡
    def ready(self):
        super().ready()
        self.s_mode = os.environ.get("SEARCH_MODE", "basic")
        print("Search mode is:", self.s_mode)
