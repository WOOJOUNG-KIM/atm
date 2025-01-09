#입력 검증 및 에러 처리 추가
#잘못된 입력 값(숫자가 아닌값, 음수 값 등)을 처리하도록 기능 추가
#유효하지 않은 메뉴 선택 시 경고 메시지 또는 사용방범 재안내를 해주세요


receipts = []
balance = 3000 #기본 금액

while True:
        num = input("사용하실 기능을 선택해주세요 (1:입금,2번:출금,3번:영수증 보기,4:종료)")
        if num == '4':
            break
        if num == "1":
            deposit_amount = input("입금액:")
            if deposit_amount.isdigit() and int(deposit_amount) > 0:
                balance += int(deposit_amount)
                receipts.append(("입금",deposit_amount,balance))
                print(f"입금하신 금액은 {deposit_amount} 현재잔액은 {balance}원 입니다")
            else:
                print("입금한 금액을 숫자 형태와 음수가 아닌값을 입력해주세요")
        if num == "2":
            withdraw_amount = int(input("출금할 금액을 입력하세요: "))
            if  balance >= withdraw_amount:
                balance -= withdraw_amount
                receipts.append((-withdraw_amount, balance))
                print(f"{withdraw_amount}원이 출급 되었습니다.")   
        if num == "3":
            if not receipts:
                print("=== 영수증 ===")
            for i in receipts:
                print(f'{i[0]}:{i[1]} 원 | 잔액{i[2]}원')
        else:
            print("영수증 내역이 없습니다.")

print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')