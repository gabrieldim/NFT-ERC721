from brownie import accounts, network, config

local_blockchain_env = ["hardhat", "development", "ganache", "mainnet-fork"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in local_blockchain_env:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
