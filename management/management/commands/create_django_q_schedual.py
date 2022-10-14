from django.core.management import BaseCommand
from django_ethereum_events.models import Daemon, FailedEventLog, MonitoredEvent
from django_q.models import Schedule


class Command(BaseCommand):
    """Use only for development!"""

    def handle(self, *args, **options):
        Schedule.objects.create(
            func="fund.tasks.update_funds_price",
            name="Update Fund Price",
            repeats=-1,
            schedule_type=Schedule.HOURLY,
        )

        Schedule.objects.create(
            func="management.tasks.multicall_price_feed.manage_price_feed",
            name="Management Price Feed",
            repeats=-1,
            schedule_type=Schedule.HOURLY,
        )
        Schedule.objects.create(
            func="django_ethereum_events.tasks.event_listener",
            name="Listening Events",
            repeats=-1,
            schedule_type=Schedule.MINUTES,
        )
