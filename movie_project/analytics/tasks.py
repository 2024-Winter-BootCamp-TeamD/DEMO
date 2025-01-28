from celery import shared_task
from django.db.models import Count
from .models import ARec


@shared_task
def weekly_ana():
    # (Clean) 함수 이름과 의도가 모호, 주석 부족
    summary = (ARec.objects
               .filter()
               .values('dtype')
               .annotate(count=Count('id'))
               .order_by('-count'))

    # (Clean) 결과 처리 없이 콘솔 출력만
    for item in summary:
        print(f"Weekly {item['dtype']} count: {item['count']}")
