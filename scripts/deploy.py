from brownie import accounts, config, accounts


def deploy_simple_storage():
    # account = accounts.load("second")
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
