from web3 import Web3
from web3.contract import Contract
from decouple import config
from abi.multicall.makerdao_multicall import (
    MAKERDAO_MULTICALL_ABI,
    MAKERDAO_MULTICALL_ADDRESS,
)

from utils.constants.addresses import addresses


class MulticallWrite:
    def __init__(self, w3: Web3, chain="mainnet", custom_address=None, custom_abi=None):
        if custom_address:
            address = Web3.toChecksumAddress(custom_address)
        else:
            try:
                address = Web3.toChecksumAddress(MAKERDAO_MULTICALL_ADDRESS[chain])
            except (Exception):
                print("Chain name key not in default dictionary")
                return

        abi = MAKERDAO_MULTICALL_ABI

        if custom_abi:
            abi = custom_abi
        self.w3 = w3
        self.multicall = w3.eth.contract(address=address, abi=abi)

    def call(self, calls: list) -> list:
        txn = self.multicall.functions.aggregate(calls).buildTransaction(
            {
                "chainId": 43113,
                "gas": 8000000,
                # "maxFeePerGas": int(20e11),
                # "maxPriorityFeePerGas": int(20e11),
                "nonce": self.w3.eth.getTransactionCount(addresses["user_1"]),
            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(
            txn, private_key=config("PRIVATE_KEY")
        )
        result = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return result

    def create_call(self, contract: Contract, fn_name: str, args: list) -> tuple:
        return (contract.address, contract.encodeABI(fn_name=fn_name, args=args))
