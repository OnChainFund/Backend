from utils.utils import get_provider


def manage_liquidity(target_asset: str, denominated_asset: str, ftx_trading_pair: str):
    # 用 ftx api 獲取價格資料
    ftx_price = get_price_from_ftx(ftx_trading_pair)
    # 從 pangolin swap 獲取流動性資料
    # 獲取 pair address(pangolinFactory.getPair)
    w3 = get_provider()
    pangolin_factory = w3.eth.contract(
        # Addresses["pangolinFactory"], abi=PangolinFactory
        Addresses["pangolin"]["FactoryMy"],
        abi=PangolinFactory,
    )
    pangolin_router = w3.eth.contract(
        Addresses["pangolin"]["Router"], abi=PangolinRouter
    )
    target_asset_contract = w3.eth.contract(target_asset, abi=ERC20)
    denominated_asset_contract = w3.eth.contract(denominated_asset, abi=ERC20)

    pair = pangolin_factory.functions.getPair(target_asset, denominated_asset).call()
    # 獲取流動性對的剩餘量

    target_asset_reserve = target_asset_contract.functions.balanceOf(pair).call()
    denominated_asset_reserve = denominated_asset_contract.functions.balanceOf(
        pair
    ).call()

    # 計算出價格
    pangolin_price = denominated_asset_reserve / target_asset_reserve
    # 差距小於 1% 不調倉
    if pangolin_price < ftx_price:
        amount = (
            math.sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price)
            - denominated_asset_reserve
        )
        path = [denominated_asset, target_asset]
    else:
        print("sell target")
        print(math.sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price))
        print(target_asset_reserve)
        amount = denominated_asset_reserve - math.sqrt(
            target_asset_reserve * denominated_asset_reserve * ftx_price
        )
        path = [target_asset, denominated_asset]

    # 計算 swap input,output
    # swap

    txn = pangolin_router.functions.swapExactTokensForTokens(
        int(abs(amount)),
        1,
        path,
        Addresses["user_1"],
        1758392484,
    ).buildTransaction(
        {
            "chainId": 43113,
            "gas": 7900000,
            "maxFeePerGas": w3.toWei("30", "gwei"),
            "maxPriorityFeePerGas": w3.toWei("1", "gwei"),
            "nonce": w3.eth.getTransactionCount(Addresses["user_1"]),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=config("PRIVATE_KEY"))
    w3.eth.sendRawTransaction(signed_txn.rawTransaction)