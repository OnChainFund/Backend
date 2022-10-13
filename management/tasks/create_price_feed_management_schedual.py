from django_q.models import Schedule

Schedule.objects.create(
    func="management.tasks.multicall_price_feed.manage_price_feed",
    name="Management Price Feed",
    repeats=-1,
    schedule_type=Schedule.HOURLY,
)
