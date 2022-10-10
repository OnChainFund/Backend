from django_q.models import Schedule

Schedule.objects.create(
    func="fund.tasks.update_funds_price",
    name="Update Fund Price",
    repeats=-1,
    schedule_type=Schedule.HOURLY,
)
