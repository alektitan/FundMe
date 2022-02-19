from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account,deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    # if we are on a peersistent network like ropsten testnet, use the associated address otherwise, deploy mocks
    network_type = config['networks'][network.show_active()]
    
    print(f"This account has a balance of {account.balance() / 10**18} ether")
    
    # pass the price feed address to our fundme contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = network_type['eth_usd_price_feed']
    else:
        price_feed_address = deploy_mocks()
        
        
    fund_me = FundMe.deploy(price_feed_address,{'from':account}, publish_source=network_type.get('verify')) 
        
    print(f'Contract deployed to {fund_me.address}')
    return fund_me

def main():
    deploy_fund_me() 
    