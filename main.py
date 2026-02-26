import random
money = 1000
current_round = 1

backpack = {"A": 0, "B": 0}
prices = {"A": 0, "B": 0}

while current_round <= 5:
    prices["A"] = random.randint(100, 200)
    prices["B"] = random.randint(100, 200)
    
    print(f"ROUND: {current_round}")
    print(f"今日市價: {prices}")
    print(f"剩餘資金: {money}  目前背包: {backpack}")

    action = input("(1)買入 (2)賣出 (3)跳過: ")
    
    if action == "3":
        current_round += 1
        continue 

    target = input("請輸入貨物名稱 (A/B): ").upper()

    if target in backpack:
        num = int(input(f"多少個 {target}？: "))
        
        if action == "1":  
            cost = num * prices[target] 
            if cost <= money:
                money -= cost
                backpack[target] += num
                print(f"成功買入 {num} 個 {target}")
            else:
                print("餘額不足！")

        elif action == "2":
            if num <= backpack[target]:
                money += num * prices[target]
                backpack[target] -= num
                print(f"成功賣出 {num} 個 {target}")
            else:
                print("庫存不足！")
    else:
        print("沒有這種東西！")

    current_round += 1