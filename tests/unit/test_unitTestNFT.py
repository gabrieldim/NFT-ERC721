from brownie import network
import pytest
from scripts.helpful_scripts import local_blockchain_env, get_account
from scripts.deployNFT import main


def test_can_create_NFT():
    if network.show_active not in local_blockchain_env:
        pytest.skip()
    NFT_token_test = main()
    assert NFT_token_test.ownerOf(0) == get_account()
