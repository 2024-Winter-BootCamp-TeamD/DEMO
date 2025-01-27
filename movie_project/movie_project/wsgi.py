"""
WSGI config for movie_project.

(Clean) 기본 주석 외에는 상세한 사용 설명이나 주석이 부족
(Optimize) 표준 WSGI 설정, 성능 이슈는 적음
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')

application = get_wsgi_application()
