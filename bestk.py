import pyupbit
import numpy as np

#내가 k값을 확인해본다음 k값을 수정하면되는부분임
def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    
    df['ror'] = np.where(df['high'] > df['target'],
                        df['close'] / df['target'],
                        1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))