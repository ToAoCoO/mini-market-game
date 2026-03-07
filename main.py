import random

current_round = {"round": 0}
money = {"money": 0}
backpack = {"A": 0, "B": 0}
prices = {"A": 0, "B": 0}



def init():
    current_round["round"] = 1
    money["money"] = 1000
    backpack["A"] = 0
    backpack["B"] = 0
    prices["A"] = 0
    prices["B"] = 0
    print("遊戲已重置！")

def buy(target: str, num: int)  -> str:
    cost = num * prices[target]
    if cost <= money["money"]:
        money["money"] -= cost
        backpack[target] += num
        return f"成功買入 {num} 個 {target}"          
    else:
        return "餘額不足！"

def sell(target: str, num: int)  -> str:
    cost = num * prices[target]
    if num <= backpack[target]:
        money["money"] += cost
        backpack[target] -= num
        return f"成功賣出 {num} 個 {target}"          
    else:
        return "存貨不足！"


def game_loop():
    while current_round["round"] <= 5:
        prices["A"] = random.randint(100, 200)
        prices["B"] = random.randint(100, 200)
        while True:
            print(f"\nROUND: {current_round}")
            print(f"今日市價: {prices}")
            print(f"剩餘資金: {money['money']}  目前背包: {backpack}")

            action = input("(1)買入 (2)賣出 (3)結束這回合: ")
            
            if action == "1":
                target = input("請輸入貨物名稱 (A/B): ").upper()
                if target not in prices:
                    print("無效貨物名稱！")
                    continue
                num = int(input(f"想要買多少個 {target}？: "))
                print(buy(target, num))
            elif action == "2":
                target = input("請輸入貨物名稱 (A/B): ").upper()
                if target not in prices:
                    print("無效貨物名稱！")
                    continue
                num = int(input(f"想要賣多少個 {target}？: "))
                print(sell(target, num))
            elif action == "3":
                current_round["round"] += 1
                break
            else:
                print("無效指令")
                continue

        
    
    return"\n遊戲結束！" f"最終資產: {money['money']}"   

if __name__ == "__main__":
    init()
    game_loop()