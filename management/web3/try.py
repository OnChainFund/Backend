from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.chain_link.MockV3Aggregator import (
    MockV3Aggregator,
)
from management.tasks import manage_pangolin_liquidity
from utils.utils import get_provider
from decouple import config
from typing import Union, List
from utils.multicall import Call, Multicall
import statistics

Num = Union[int, float]


def update_oracle_answer(ansir: float, mock_v3_aggregator_address: str):
    w3 = get_provider()
    mock_v3_aggregator = w3.eth.contract(
        mock_v3_aggregator_address,
        abi=MockV3Aggregator,
    )
    txn = mock_v3_aggregator.functions.updateAnswer(int(ansir * 1e8)).buildTransaction(
        {
            "chainId": 43113,
            # "gas": 8000000,
            # "maxFeePerGas": int(20e11),
            # "maxPriorityFeePerGas": int(20e11),
            "nonce": w3.eth.getTransactionCount(Addresses["user_1"]),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=config("PRIVATE_KEY"))
    w3.eth.sendRawTransaction(signed_txn.rawTransaction)

manage_pangolin_liquidity(
    "0x9Bb8F40d53DA2796F34d85f5bf27C475Df03E70C","0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4", 76.07
)
#update_oracle_answer(76.07, "0x15fE0276686097996D6c4724762E8D1BF74E9471")
