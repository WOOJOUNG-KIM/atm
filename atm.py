
receipts = []
balance = 3000 #기본 금액

while True:
        num = input("사용하실 기능을 선택해주세요 (1:입금,2번:출금,3번:영수증 보기,4:종료)")
        if num == '4':
            break
        if num == "1":
            deposit_amount = int(input("입금액:"))
            balance += deposit_amount
            receipts.append(("입금",deposit_amount,balance))
            print(f"입금하신 금액은 {deposit_amount} 현재잔액은 {balance}원 입니다")
        if num == "2":
            withdraw_amount = int(input("출금할 금액을 입력하세요: "))
        if  balance >= withdraw_amount:
            balance -= withdraw_amount
            receipts.append((-withdraw_amount, balance))
            print(f"{withdraw_amount}원이 출급 되었습니다.")
        else:
            print("잔액이 부족합니다")

        print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')