# pyright: strict:5

from typing import Any


ComptrollerLib: list[Any] = [
    {
        "inputs": [
            {"internalType": "address", "name": "_dispatcher", "type": "address"},
            {
                "internalType": "address",
                "name": "_protocolFeeReserve",
                "type": "address",
            },
            {"internalType": "address", "name": "_fundDeployer", "type": "address"},
            {"internalType": "address", "name": "_valueInterpreter", "type": "address"},
            {
                "internalType": "address",
                "name": "_externalPositionManager",
                "type": "address",
            },
            {"internalType": "address", "name": "_feeManager", "type": "address"},
            {
                "internalType": "address",
                "name": "_integrationManager",
                "type": "address",
            },
            {"internalType": "address", "name": "_policyManager", "type": "address"},
            {
                "internalType": "address",
                "name": "_gasRelayPaymasterFactory",
                "type": "address",
            },
            {"internalType": "address", "name": "_mlnToken", "type": "address"},
            {"internalType": "address", "name": "_wethToken", "type": "address"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bool",
                "name": "autoProtocolFeeSharesBuyback",
                "type": "bool",
            }
        ],
        "name": "AutoProtocolFeeSharesBuybackSet",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes",
                "name": "failureReturnData",
                "type": "bytes",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "sharesAmount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "buybackValueInMln",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "gav",
                "type": "uint256",
            },
        ],
        "name": "BuyBackMaxProtocolFeeSharesFailed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "DeactivateFeeManagerFailed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "gasRelayPaymaster",
                "type": "address",
            }
        ],
        "name": "GasRelayPaymasterSet",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "sharesDue",
                "type": "uint256",
            }
        ],
        "name": "MigratedSharesDuePaid",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "PayProtocolFeeDuringDestructFailed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "bytes",
                "name": "failureReturnData",
                "type": "bytes",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "redeemer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "sharesAmount",
                "type": "uint256",
            },
        ],
        "name": "PreRedeemSharesHookFailed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "RedeemSharesInKindCalcGavFailed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "buyer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "investmentAmount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "sharesIssued",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "sharesReceived",
                "type": "uint256",
            },
        ],
        "name": "SharesBought",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "redeemer",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "recipient",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "sharesAmount",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address[]",
                "name": "receivedAssets",
                "type": "address[]",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "receivedAssetAmounts",
                "type": "uint256[]",
            },
        ],
        "name": "SharesRedeemed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "vaultProxy",
                "type": "address",
            }
        ],
        "name": "VaultProxySet",
        "type": "event",
    },
    {
        "inputs": [{"internalType": "bool", "name": "_isMigration", "type": "bool"}],
        "name": "activate",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_sharesAmount", "type": "uint256"}
        ],
        "name": "buyBackProtocolFeeShares",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_investmentAmount", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_minSharesQuantity",
                "type": "uint256",
            },
        ],
        "name": "buyShares",
        "outputs": [
            {"internalType": "uint256", "name": "sharesReceived_", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_buyer", "type": "address"},
            {"internalType": "uint256", "name": "_investmentAmount", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "_minSharesQuantity",
                "type": "uint256",
            },
        ],
        "name": "buySharesOnBehalf",
        "outputs": [
            {"internalType": "uint256", "name": "sharesReceived_", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "calcGav",
        "outputs": [{"internalType": "uint256", "name": "gav_", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "calcGrossShareValue",
        "outputs": [
            {"internalType": "uint256", "name": "grossShareValue_", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_extension", "type": "address"},
            {"internalType": "uint256", "name": "_actionId", "type": "uint256"},
            {"internalType": "bytes", "name": "_callArgs", "type": "bytes"},
        ],
        "name": "callOnExtension",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "deployGasRelayPaymaster",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "depositToGasRelayPaymaster",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_deactivateFeeManagerGasLimit",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "_payProtocolFeeGasLimit",
                "type": "uint256",
            },
        ],
        "name": "destructActivated",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "destructUnactivated",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "doesAutoProtocolFeeSharesBuyback",
        "outputs": [
            {"internalType": "bool", "name": "doesAutoBuyback_", "type": "bool"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDenominationAsset",
        "outputs": [
            {"internalType": "address", "name": "denominationAsset_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDispatcher",
        "outputs": [
            {"internalType": "address", "name": "dispatcher_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getExternalPositionManager",
        "outputs": [
            {
                "internalType": "address",
                "name": "externalPositionManager_",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getFeeManager",
        "outputs": [
            {"internalType": "address", "name": "feeManager_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getFundDeployer",
        "outputs": [
            {"internalType": "address", "name": "fundDeployer_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getGasRelayPaymaster",
        "outputs": [
            {"internalType": "address", "name": "gasRelayPaymaster_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getGasRelayPaymasterFactory",
        "outputs": [
            {
                "internalType": "address",
                "name": "gasRelayPaymasterFactory_",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getGasRelayTrustedForwarder",
        "outputs": [
            {"internalType": "address", "name": "trustedForwarder_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getIntegrationManager",
        "outputs": [
            {
                "internalType": "address",
                "name": "integrationManager_",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_who", "type": "address"}],
        "name": "getLastSharesBoughtTimestampForAccount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "lastSharesBoughtTimestamp_",
                "type": "uint256",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getMlnToken",
        "outputs": [
            {"internalType": "address", "name": "mlnToken_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPolicyManager",
        "outputs": [
            {"internalType": "address", "name": "policyManager_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getProtocolFeeReserve",
        "outputs": [
            {
                "internalType": "address",
                "name": "protocolFeeReserve_",
                "type": "address",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getSharesActionTimelock",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "sharesActionTimelock_",
                "type": "uint256",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getValueInterpreter",
        "outputs": [
            {"internalType": "address", "name": "valueInterpreter_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getVaultProxy",
        "outputs": [
            {"internalType": "address", "name": "vaultProxy_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getWethToken",
        "outputs": [
            {"internalType": "address", "name": "wethToken_", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_denominationAsset",
                "type": "address",
            },
            {
                "internalType": "uint256",
                "name": "_sharesActionTimelock",
                "type": "uint256",
            },
        ],
        "name": "init",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "enum IVault.VaultAction",
                "name": "_action",
                "type": "uint8",
            },
            {"internalType": "bytes", "name": "_actionData", "type": "bytes"},
        ],
        "name": "permissionedVaultAction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_sender", "type": "address"},
            {"internalType": "address", "name": "_recipient", "type": "address"},
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
        ],
        "name": "preTransferSharesHook",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_sender", "type": "address"}],
        "name": "preTransferSharesHookFreelyTransferable",
        "outputs": [],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_amount", "type": "uint256"}],
        "name": "pullWethForGasRelayer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_recipient", "type": "address"},
            {"internalType": "uint256", "name": "_sharesQuantity", "type": "uint256"},
            {"internalType": "address[]", "name": "_payoutAssets", "type": "address[]"},
            {
                "internalType": "uint256[]",
                "name": "_payoutAssetPercentages",
                "type": "uint256[]",
            },
        ],
        "name": "redeemSharesForSpecificAssets",
        "outputs": [
            {"internalType": "uint256[]", "name": "payoutAmounts_", "type": "uint256[]"}
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_recipient", "type": "address"},
            {"internalType": "uint256", "name": "_sharesQuantity", "type": "uint256"},
            {
                "internalType": "address[]",
                "name": "_additionalAssets",
                "type": "address[]",
            },
            {"internalType": "address[]", "name": "_assetsToSkip", "type": "address[]"},
        ],
        "name": "redeemSharesInKind",
        "outputs": [
            {"internalType": "address[]", "name": "payoutAssets_", "type": "address[]"},
            {
                "internalType": "uint256[]",
                "name": "payoutAmounts_",
                "type": "uint256[]",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "_nextAutoProtocolFeeSharesBuyback",
                "type": "bool",
            }
        ],
        "name": "setAutoProtocolFeeSharesBuyback",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_nextGasRelayPaymaster",
                "type": "address",
            }
        ],
        "name": "setGasRelayPaymaster",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_vaultProxy", "type": "address"}
        ],
        "name": "setVaultProxy",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "shutdownGasRelayPaymaster",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_contract", "type": "address"},
            {"internalType": "bytes4", "name": "_selector", "type": "bytes4"},
            {"internalType": "bytes", "name": "_encodedArgs", "type": "bytes"},
        ],
        "name": "vaultCallOnContract",
        "outputs": [{"internalType": "bytes", "name": "returnData_", "type": "bytes"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
