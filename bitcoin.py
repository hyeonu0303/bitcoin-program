import pyupbit

access = "CPxCRlHjQZzYvvNKCUOBdOxE31mtwOE7lIVaiPQx"          # 본인 값으로 변경
secret = "m2RPUztS27hPEQ49TNyv8dfY9qedmu5ZUd8l9SYI"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP(리플임) 조회 
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balance("KRW-WEMIX"))     

