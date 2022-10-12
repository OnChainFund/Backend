from django.core.management.base import BaseCommand, CommandError
from fund.models import Fund
from management.management.commands.event_async import listen_to_event


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        print("start listen to events...")
        listen_to_event()
