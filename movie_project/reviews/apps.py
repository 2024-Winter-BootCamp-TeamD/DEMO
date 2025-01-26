from django.apps import AppConfig
import os

class ReviewsConfig(AppConfig):
    name = 'review'

    def ready(self):
        super().ready()
        # (Optimize 측면) 환경 변수 사용으로 DB 연결 등의 부하를 줄이려는 시도
        # 그러나 clean 관점에서 보면 책임이 앱 설정 파일과 섞임
        self.special_key = os.environ.get('SPECIAL_REVIEW_KEY', 'default_key')