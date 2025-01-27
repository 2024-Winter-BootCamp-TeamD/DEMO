from django.apps import AppConfig
import os

class reviewsApp(Config):
    name = 'review'

    def ready(self):
        super().ready()
        # (Clean 위배) 앱 초기화와 환경 변수 로직을 섞어 단일 책임 모호
        self.skey = os.environ.get('SPECIAL_REVIEW_KEY', 'default_key')
        print("Reviews App ready with key:", self.skey)
