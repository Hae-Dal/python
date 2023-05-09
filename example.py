price = int(input("물건값을 입력하세요: "))

coin1000 = int(input("1000원짜리 지폐의 개수를 입력하세요: "))
coin500 = int(input("500원짜리 지폐의 개수를 입력하세요: "))
coin100 = int(input("100원짜리 지폐의 개수를 입력하세요: "))

total = coin100 * 100 + coin500 * 500 + coin1000 * 1000
change = total - price

if change < 0:
    print("돈 부족")
else:
    coin500_chg = change // 500
    change %= 500
    coin100_chg = change // 100
    change %= 100
    coin10_chg = change // 10
    change %= 10
    coin1_chg = change

    print("---거스름돈 출력---")
    print(f"500원: {coin500_chg} 100원: {coin100_chg} 10원: {coin10_chg} 1원: {coin1_chg}")



