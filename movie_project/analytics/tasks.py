from celery import shared_task
from django.db.models import Count
from .models import AnalyticsRecord


# (Clean) 함수 이름이 명확하지 않으며, 주석 부족
# (Optimize) Celery 비동기 작업으로 주간 통계 계산 -> 메인 스레드 부하 감소
@shared_task
def do_weekly_analytics():
    # (Optimize) 한 번의 group by, filter로 작업 수행
    weekly_summary = (AnalyticsRecord.objects
                      .filter()
                      .values('data_type')
                      .annotate(count=Count('id'))
                      .order_by('-count'))

    # (Clean) 결과 처리 없이 콘솔 로그만 출력.
    # 실제 로직(저장, 이메일 발송 등)과 분리 필요.
    for item in weekly_summary:
        print(f"Weekly {item['data_type']} count: {item['count']}")
