import time

from django_ethereum_events.tasks import event_listener


def run_listener():
    event_listener()
    # time.sleep(30)
    # event_listener()
