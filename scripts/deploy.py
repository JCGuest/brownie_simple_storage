from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(f"Stored value: {stored_value}")
    transaction = simple_storage.store(42, {"from": account})
    transaction.wait(1)
    new_value = simple_storage.retrieve()
    print(f"New value: {new_value}")


def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
