from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(f"Stored value: {stored_value}")
    transaction = simple_storage.store(42, {"from": account})
    transaction.wait(1)
    new_value = simple_storage.retrieve()
    print(f"New value: {new_value}")


def main():
    deploy_simple_storage()
