import random


def init():
    game_data = {
    "current_round": 1,
    "money": 1000 ,
    "item": ["A", "B"] ,
    "backpack": [0, 0],
    "prices": [0,0]
    }
    print("遊戲已重置！")
    return game_data

def buy(target: str, num: int, game_data: dict)  -> str:
    cost = num * game_data["prices"][game_data["item"].index(target)]
    if cost <= game_data["money"]:
        game_data["money"] -= cost
        game_data["backpack"][game_data["item"].index(target)] += num
        return f"成功買入 {num} 個 {target}"          
    else:
        return "餘額不足！"

def sell(target: str, num: int, game_data: dict)  -> str:
    cost = num * game_data["prices"][game_data["item"].index(target)]
    if num <= game_data["backpack"][game_data["item"].index(target)]:
        game_data["money"] += cost
        game_data["backpack"][game_data["item"].index(target)] -= num
        return f"成功賣出 {num} 個 {target}"          
    else:
        return "存貨不足！"


def game_loop(game_data: dict) -> str:
    while game_data["current_round"] <= 5:
        game_data["prices"] = [ random.randint(100, 200), random.randint(100, 200) ]
        
        while True:
            print(f"\nROUND: {game_data['current_round']}")
            print(f"今日市價: {game_data['prices']}")
            print(f"剩餘資金: {game_data['money']}  目前背包: {game_data['backpack']}")

            action = input("(1)買入 (2)賣出 (3)結束這回合: ")
            
            if action == "1":
                target = input("請輸入貨物名稱 (A/B): ").upper()
                if target not in game_data['item']:
                    print("無效貨物名稱！")
                    continue
                num = int(input(f"想要買多少個 {target}？: "))
                print(buy(target, num, game_data))
            elif action == "2":
                target = input("請輸入貨物名稱 (A/B): ").upper()
                if target not in game_data['item']:
                    print("無效貨物名稱！")
                    continue
                num = int(input(f"想要賣多少個 {target}？: "))
                print(sell(target, num, game_data))
            elif action == "3":
                game_data["current_round"] += 1
                break
            else:
                print("無效指令")
                continue

        
    
    return"\n遊戲結束！" f"最終資產: {game_data['money']}"   

if __name__ == "__main__":
    game_data_now = init()
    game_loop(game_data_now)