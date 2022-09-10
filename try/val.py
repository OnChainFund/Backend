from ast import Add
from datetime import timezone
import math
import struct
from decouple import config

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
    print(tx)
    print(type(tx))
    print(dir(tx))
    print((tx.hex()))
    logdata_hex = tx

    logdata_hex_wo_0x =  tx.hex()[2:]
    print(logdata_hex_wo_0x)
    print(len(logdata_hex_wo_0x))
    print(type(logdata_hex_wo_0x))



    # Trim '0x' from beginning of string
    hexdataTrimed = tx.hex()[2:]

    # Split trimmed string every 64 characters
    n = 64
    dataSplit = [hexdataTrimed[i:i+n] for i in range(0, len(hexdataTrimed), n)]

    # Fill new list with converted decimal values
    data = []
    for val in range(len(dataSplit)):
        toDec = int(dataSplit[val], 16)
        data.append(toDec)

    print(data)
    #logdata = logdata_hex_wo_0x.decode('hex')
    #print(logdata)

    #import ethereum.abi
    #data_dec = ethereum.abi.decode_abi(["address", "address", "uint256"], logdata)
    #print; pprint (data_dec)
    
    #print(bytes.fromhex(tx.hex()).decode('utf-8'))
    # print((tx.title))
    # print(struct.unpack(">h",tx) )
    fund_value_calculator = w3.eth.contract(
        Addresses["ocf"]["FundValueCalculator"], abi=FundValueCalculator
    )
    # txn = fund_value_calculator.functions.calcGavInAsset(
    #    vault_proxy,
    #    quote_asset,
    # ).transact()


# vault proxy: 0x02b7a6d41F929a2d09D6dd8aF5537c1d1fe2E678
get_price(
    "0x02b7a6d41F929a2d09D6dd8aF5537c1d1fe2E678",
    "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
)
