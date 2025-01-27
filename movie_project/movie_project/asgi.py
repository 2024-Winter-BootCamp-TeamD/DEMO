"""
ASGI config for movie_project.

(Clean) 주석은 달았지만 상세 설명 부족
(Optimize) 표준 ASGI 설정으로 성능 관련 문제는 거의 없음
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')

application = get_asgi_application()
