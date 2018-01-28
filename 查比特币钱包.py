# python 3.6
from bit import Key,PrivateKeyTestnet

def 查钱包金额(私钥集合):
    for 私钥 in 私钥集合:
        print("私钥：%s"%私钥)
        my_key=Key(私钥)
        print("余额：%s"%my_key.get_balance('btc'))
        
def 付款(私钥, 比特地址集):
    my_key=Key(私钥)
    my_key.send(比特地址集)
    
if __name__ == "__main__":
    
    私钥集合=[
        '5KRxPEKay5TDyR4YnopPkWm4nKsGbH8aM8uAtSW6EkQVRQPGAYe',
        '5JnMrQzjWgp4LMAVMARUvnYN49EML6GsABbVVFkGyncMMdyPfkT',
        '5JVo8ajwoYePzCniCajfNJWPMRrpE5JtYZfxkH3rx9eUawKkTu6',
        '5JX3JccLrxS8hEkNGvxHSFMt6BRJ2TfPf8eDo7mLpecZLuoPSXr',
        '5KHjYnerfEzoExmiLqf2REmCbibvzmGGaQXJKnP3BF3KbeNnH5P'
          ]
    私钥集合2=[
        '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAnchuDf',
        '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAvUcVfH',
        '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreB1FQ8BZ',
        '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreB4AD8Yi'
          ]
        
    比特地址集=[
        ('13kU8WqdKqFTL6fmrx2efx2R2GYPftGBLT', 0.0035, 'btc'),
        ('1K5SSdCHKSomqE4bu7uCBhZpGSLPt199tF', 190, 'jpy'),
        ('1CyFjdXy9UVMGj3ExGWFo7GzZs7QXi43Q2', 3, 'eur'),
        ('1GiA2xyfdUwVKWpfEyyhrEFHT4EjRD1nrH', 0.0035, 'btc')
        ]
    比特币=[
        ('13kU8WqdKqFTL6fmrx2efx2R2GYPftGBLT', 0.000002, 'btc')
        ]
    查钱包金额(私钥集合2)
    #key = PrivateKeyTestnet('cU6s7jckL3bZUUkb3Q2CD9vNu8F1o58K5R5a3JFtidoccMbhEGKZ')
    #key.transactions
    #key.get_transactions()
    #key.balance
    #key.get_balance('btc')
