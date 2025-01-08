
# while 문을 이용해서 입금 출금 영수증 보기 종료라는 버튼을 누르기 전까지 계속해서 

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
        print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')