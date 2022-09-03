from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}" 
sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

def main():
    account = get_account()
    
    NFT_token = SimpleCollectible.deploy({"from" : account})
    
    transaction = NFT_token.createCollectible(sample_token_uri, {"from" : account})
    
    transaction.wait(1)
    
    print("Uspeshno kreiran NFT na platformata OpenSea! \n")

    print(f"NFT tokenot e dostapen na sledniov link: \n {OPENSEA_URL.format(NFT_token.address, NFT_token.tokenCounter()-1 )} \n")

    print("Pojasnuvanje: Dokolku metapodatocite ne se vchitaat vednash, napravete refresh na linkot posle nekolku minuti. \n\n")

    return NFT_token