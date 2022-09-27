from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.chain_link.MockV3Aggregator import (
    MockV3Aggregator,
)
from utils.utils import get_provider
from decouple import config
from typing import Union, List
from utils.multicall import Call, Multicall

Num = Union[int, float]


def update_oracle_answer(ansir: int, mock_v3_aggregator_address: str):
    w3 = get_provider()
    mock_v3_aggregator = w3.eth.contract(
        mock_v3_aggregator_address,
        abi=MockV3Aggregator,
    )
    txn = mock_v3_aggregator.functions.updateAnswer(ansir).buildTransaction(
        {
            "chainId": 43113,
            "gas": 8000000,
            "maxFeePerGas": int(20e11),
            "maxPriorityFeePerGas": int(20e11),
            "nonce": w3.eth.getTransactionCount(Addresses["user_1"]),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=config("PRIVATE_KEY"))
    w3.eth.sendRawTransaction(signed_txn.rawTransaction)


def get_token_price_multicall():
    pass


def get_token_price_multicall():
    pass


def update_oracle_answer_multicall(
    ansirs: List[Num], mock_v3_aggregator_addresses: List[str]
):
    pass


