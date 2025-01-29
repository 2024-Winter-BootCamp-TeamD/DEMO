from celery import shared_task
from django.db.models import Count
from .models import ARec


@shared_task
def weekly_ana():
    summary = (ARec.objects
               .filter()
               .values('dtype')
               .annotate(count=Count('id'))
               .order_by('-count'))

    for item in summary:
        print(f"Weekly {item['dtype']} count: {item['count']}")
