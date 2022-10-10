from django_ethereum_events.chainevents import AbstractEventReceiver
from django_ethereum_events.models import MonitoredEvent 
contract_abi = """
The whole contract abi goes here
"""

event = "MyEvent"  # the emitted event name
event_receiver = "myapp.event_receivers.CustomEventReceiver"
contract_address = "0x10f683d9acc908cA6b7A34726271229B846b0292"  # the address of the contract emitting the event

MonitoredEvent.object.register_event(
    event_name=event,
    contract_address=contract_address,
    contract_abi=contract_abi,
    event_receiver=event_receiver
)