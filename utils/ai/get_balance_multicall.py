# pyright: strict
from eth_typing.evm import Address
from eth_utils.address import to_canonical_address
from pydantic import BaseModel
from utils.ai.get_weighted_positions import assets
from web3.contract import Contract
from utils.utils import get_provider
from utils.multicall.multicall import Multicall, Call, CallResult
from abi.others.ERC20 import ERC20 as ERC20_ABI


class TokenBalance(BaseModel):
    address: Address
    balance: int


def get_balance_multicall(fund_address: str) -> list[TokenBalance]:
    w3 = get_provider()
    multicall = Multicall(w3, "fuji")
    token_balance_call: list[Call] = []
    address_list: list[Address] = []

    for i in range(len(assets)):
        positive_address: Address = to_canonical_address(
            assets[i]["positive"]["address"]
        )
        negitive_address: Address = to_canonical_address(
            assets[i]["negitive"]["address"]
        )
        target_asset_positive: Contract = w3.eth.contract(
            address=positive_address, abi=ERC20_ABI
        )
        target_asset_negitive: Contract = w3.eth.contract(
            address=negitive_address, abi=ERC20_ABI
        )
        token_balance_call.extend(
            [
                multicall.create_call(
                    target_asset_positive,
                    "balanceOf",
                    [fund_address],
                ),
                multicall.create_call(
                    target_asset_negitive,
                    "balanceOf",
                    [fund_address],
                ),
            ]
        )
        address_list.extend([positive_address, negitive_address])

    results: CallResult = multicall.call(token_balance_call)

    datas: list[TokenBalance] = []
    for i in range(0, len(results[1])):
        balance = int(results[1][i].hex(), 16)
        datas.append(TokenBalance(balance=balance, address=address_list[i]))
    return datas
