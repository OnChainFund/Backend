from ast import Add
from datetime import timezone
import math
from decouple import config
import binascii
import struct
from utils.data_source.ftx.client import FtxClient
from utils.utils import get_provider
from contract.contracts.deployment.others.PangolinFactory import PangolinFactory
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from contract.contracts.deployment.others.FundValueCalculator import FundValueCalculator
from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.ERC20 import ERC20


def get_price(vault_proxy: str, quote_asset: str):
    w3 = get_provider()
    tx = w3.eth.call(
        {
            "value": 0,
            "gas": 7900000,
            "maxFeePerGas": w3.toWei("30", "gwei"),
            "maxPriorityFeePerGas": 1000000000,
            "to": "0x8a479C366EE7E51eF0Bc2c496b9707CEF0aC610c",
            "data": "0x56cff99f",
        }
    )
    print(str(tx))
    reverseBytes = tx[::-1]
    print("[11]: %s" % reverseBytes)

    bytesToHex = binascii.b2a_hex(reverseBytes)
    print("[14]: %s" % bytesToHex)

    bytesHexToASCII = bytesToHex.decode('ascii')
    print("[17]: %s" % bytesHexToASCII)

    unpackFromhex = struct.unpack('l', bytes.fromhex(bytesHexToASCII))[0]
    print("[20]: %s" % unpackFromhex)

    unpackBytes = struct.unpack('f', b'\x91\xfc\xb6C')[0]
    print("[23]: %s" % unpackBytes)
    # txn = fund_value_calculator.functions.calcGavInAsset(
    #    vault_proxy,
    #    quote_asset,
    # ).transact()

# vault proxy
get_price(
    "0x02b7a6d41F929a2d09D6dd8aF5537c1d1fe2E678",
    "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
)
