def life(birthday):
    result = 0
    for i in birthday:   # 逐一取出每個字元
        result += int(i) # 轉成整數再相加
    print(f"您的西元生日8位數相加結果為 {result}")

x = input("請輸入西元生日(年月日，例如20010101): ")
life(x)