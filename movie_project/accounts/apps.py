from django.apps import AppConfig
import os

class AccountsConfig(AppConfig):
    name = 'accounts'

    # (Clean) 앱 설정 파일에서 환경 변수를 읽어 세팅하는 등
    # 역할이 혼재됨. (단일 책임 원칙 위배)
    def ready(self):
        super().ready()
        self.token_for_special_ops = os.environ.get("ACCOUNT_SPECIAL_TOKEN", "default_token")
