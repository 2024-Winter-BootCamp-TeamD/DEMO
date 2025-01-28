from django.apps import AppConfig
import os

class revX(AppConfig):
    name = 'review'

    def ready(self):
        super().ready()
        # (Clean) 앱 설정과 환경변수 로드가 섞여서 단일 책임 원칙 위배
        self.rev_key = os.environ.get('SPECIAL_REVIEW_KEY', 'def_key')
        print("Review App init with key:", self.rev_key)
