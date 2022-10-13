event_signature_hash = web3.keccak(text="eventName(uint32)").hex()
event_filter = web3.eth.filter({
    "address": myContract_address,
    "topics": [event_signature_hash,
               "0x000000000000000000000000000000000000000000000000000000000000000a"],
    })