# 잔고 조회
import pyupbit

access_key = "57xwiVxqYFHuqoiwR5MIZAPZEXF67RxJO6mMZ0Yg" # 개인 openAPI입력
secret_key = "ZIrW1DpUliu295b7xqlC6CbhIG2K4xak4PEihyt3" # 개인 openAPI입력

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balance())