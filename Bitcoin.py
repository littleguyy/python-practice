# import bitcoin
from bitcoin import *
'''
def bitcoin生成(私钥地址):
    my_public_key=privtopub(私钥地址)
    return(pubtoaddr(my_public_key))

def 比特币随机生成():
    my_private_key=random_key()
    print("随机生成的私钥： %s"%my_private_key)
    my_public_key=privtopub(my_private_key)
    return(pubtoaddr(my_public_key))


def my_multi_address():
    # Create Private Keys
    my_private_key1=random_key()
    my_private_key2=random_key()
    my_private_key3=random_key()
    # Create Public keys
    public_key1=privtopub(my_private_key1)
    public_key2=privtopub(my_private_key2)
    public_key3=privtopub(my_private_key3)
    #Create Multi-signature address
    my_multi_sig=mk_multisig_script(public_key1,public_key2,public_key3,2,3)
    my_multi_address=scriptaddr(my_multi_sig)
    print("my multi address: %s"%my_multi_address)

def 查比特币交易记录(地址):
    # 比特币地址='1PcnuUY46FBqbK8KBWHc1TS2QV3dxT4jXX'
    return(history(地址))
    #print("该Bitcoin交易记录: %s"%history(地址))
'''
if __name__=="__main__":
    #print("私钥生成比特币地址%s"%bitcoin生成("5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAnchuDf"))
    #print("Bitcoin地址：%s"%比特币随机生成())
    #my_multi_address()
    #if not 查比特币交易记录('1Xr22A41TBoniKYyrxpUVaMRbf6xw5L93'):
    print(history('1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm﻿'))
    #print("比特币地址： %s"%比特币随机生成())
