from django.apps import AppConfig
import os

class accountsApp(AppConfig):
    name = 'accounts'

    # (Clean) 앱 설정과 비즈니스 로직(환경 변수 로드)이 뒤섞여 있음
    def ready(self):
        super().ready()
        # 변수명 모호: 어떤 용도인지 명확히 드러나지 않음
        self.tokSp = os.environ.get("ACCOUNT_SPECIAL_TOKEN", "default_token")
        print("accountsApp ready with token:", self.tokSp)
        # 여기서 다른 비즈니스 로직도 섞어서 처리 가능
        # (SRP 위배 예시)
