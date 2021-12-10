from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expect = 0
    # Assert
    assert starting_value == expect


def test_update_storage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    expect = 10
    simple_storage.store(expect, {"from": account})
    # Assert
    assert simple_storage.retrieve() == expect
