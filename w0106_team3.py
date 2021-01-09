# 1. 프로그램 기획
# -> 카드 전용 자판기 구현

# 2. 시나리오
# 1) 카드 투입, 잔액 입력
# 2) 메뉴 선택. 메뉴가 품절일 경우 품절 안내 문구 출력
# 3) 잔액이 모자를 경우 메뉴 선택 단계로 다시 이동
# 4) 잔액이 충족되면 물건 제공

# 3. 프로세스
# 0. 카드에 충전할 금액 입력 input -> int(정상 카드) / char(이상한 카드)
# 1. 카드 투입 시 -> 이상한거, 잘못 넣은 카드는 반환
# 2. 메뉴: 과자5개, 수량 랜덤(0~5개), 가격(랜덤 1~50하고 *100 아래 단위 없애기)
# 메뉴 = dict, 하위에 이름, 수량, 가격
# 3. 매진 메뉴 선택 시 예외처리(다른 것 선택하라는 문구 뜨게)
# 메뉴.수량 ==0 ~~
# 4. 카드 잔액과 메뉴 가격 비교: 적으면 [잔액부족] 문장 출력+ 메뉴 선택 단계로. 아니면 물건 제공
# 메뉴.가격 <, > 비교해서

import random;
# 과자 리스트
snack = ['칙촉', '포카칩', '오감자', '자갈치','건빵'];
# 과자 정보
menu = {};
# 가진 돈
money = [0];

def InputMoney():
    while True:
        try:
        # 0. 카드에 충전할 금액 입력
            money = int(input('카드에 충전할 금액을 입력하세요: '));
            return money;
        except:
        # 1. char 입력 시 에러메세지 출력 후 재입력
            print('잘못된 입력입니다. 다시 입력하세요.');
            continue;

def MakeMenu():
    for i in range(5):
    # 2. 메뉴: 과자5개, 수량 랜덤(0~5개), 가격(랜덤 1~50하고 *100)
        amount = random.randint(0,5);
        price = random.randint(1,50) * 100;

        a = dict();
        a['재고'] = amount;
        a['가격'] = price;
        menu[snack[i]] = a;

def ShowMenu():
    for i in range(5):
        print('[%d] %s \t' %(i+1, snack[i]), end='');
        print('재고:', menu[snack[i]]['재고'], '가격:', menu[snack[i]]['가격'], 'won');

def balance(select):
    # 선택한 메뉴의 가격보다 잔액이 부족한지 확인 후 결제
    if money[0] > menu[snack[select]]['가격']:
        # 정상 결제 시 재고와 가격을 업데이트한다.
        menu[snack[select]]['재고'] -= 1;
        money[0] -= menu[snack[select]]['가격'];
        print('결제되었습니다.\n');
    else:
        print('잔액이 부족합니다. 다른 카드를 삽입하세요.\n');

def pay():
    while True:
        try:
            # 선택할 메뉴를 고른다. 선택 번호가 정수가 아닌 경우 에러 발생
            select = int(input('메뉴를 선택하세요 (1 ~ 5): '));
            if select not in range(1,6):
                # 선택한 번호가 1~5가 아닌 경우 에러 발생
                raise ValueError;
            break;
        except:
            # 에러 발생 시 에러메세지 출력 후 재입력
            print('잘못된 입력입니다. 다시 입력하세요.');
            continue;

    if menu[snack[select-1]]['재고'] != 0:
        # 재고가 있는 상품의 경우 결제
        balance(select-1);
    else:
        print('%s 재고가 부족합니다. 다른 상품을 선택하세요.\n' %(snack[select-1]) );



print('Program Start\n');
# 2. 메뉴: 과자5개, 수량 랜덤(0~5개), 가격(랜덤 1~50하고 *100 아래 단위 없애기)
MakeMenu();
while True:
    # 0, 1 카드 투입 및 금액 충전
    money[0] = InputMoney();

    while True:
        # 카드 잔액 출력 및 메뉴 선택 (개수, 가격 표시 / 메뉴 = dict, 하위에 이름, 수량, 가격)
        ShowMenu();
        print('잔액: %d 원' %(money[0]));

        # 구매의사 질문 (메뉴 선택 및 카드 투입)
        while True:
            temp = input('구매하시겠습니까? (y/n): ');
            if temp.isalpha():
                temp = temp.lower();
                if temp == 'y' or temp == 'n':
                    break;
                else:
                    print('잘못된 입력입니다. 다시 입력하세요.');
            else:
                print('잘못된 입력입니다. 다시 입력하세요.');

        if temp == 'y':
            # 매진 메뉴 선택 및 카드 잔액 부족 시 예외처리 -> 에러메세지 발생 후 다른 카드 투입
            pay();
        else:
            print('구매를 취소합니다.');
            break;


    while True:
        # (y/n)을 입력받는다. 대소문자 구분 X
        temp = input('다른 카드를 투입하시겠습니까? (y/n): ');
        if temp.isalpha():
            # 알파벳인 경우 소문자로 바꿔준다.
            temp = temp.lower();
            # (y/n)의 경우 while문 탈출
            if temp == 'y' or temp == 'n':
                break;
            else:
                print('잘못된 입력입니다. 다시 입력하세요.');
        else:
            print('잘못된 입력입니다. 다시 입력하세요.');
            continue;
    # y의 경우 카드 잔액을 입력하는 것 부터 새로 시작
    if temp == 'y':
        continue;
    # n의 경우 프로그램 종료
    else:
        break;

print('\nProgram End');