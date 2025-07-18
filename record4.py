四、簡化 Python 程式範例（模擬核心）
python
複製
# 編輯
# oracle_fetcher.py
def get_chainlink_price():
    import requests
    response = requests.get('https://api.chain.link/v1/feeds/ETH-USD')
    return float(response.json()['price'])

# binance_fetcher.py
def get_binance_price():
    import requests
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
    return float(response.json()['price'])

# main.py
from oracle_fetcher import get_chainlink_price
from binance_fetcher import get_binance_price

def main():
    threshold = 0.005  # 0.5%
    oracle_price = get_chainlink_price()
    cex_price = get_binance_price()
    diff = abs(oracle_price - cex_price) / oracle_price

    print(f"Oracle: {oracle_price} | CEX: {cex_price} | Diff: {diff:.4%}")
    if diff > threshold:
        if oracle_price > cex_price:
            print("Execute arbitrage: Sell on-chain, Buy on Binance")
        else:
            print("Execute arbitrage: Buy on-chain, Sell on Binance")

if __name__ == "__main__":
    main()
📉 風險提醒
