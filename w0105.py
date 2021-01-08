import random;

def makeNum(lottoNum, bonusNum):
    # 1~45의 수 중 로또 번호와 보너스 번호를 랜덤 생성한다.
    # 1부터 45의 랜덤 넘버 6개 생성
    for i in range(1, 7):
        while True:
            if lottoNum == list():                      # 1번 숫자 생성할때.. 리스트가 비었는지 확인
                lottoNum += [random.randint(1, 45)];    # 빈 리스트면 하나 만들어서 넣고 while탈출
                break;
            else:
                temp = random.randint(1, 45);           # 2~6번 숫자 생성할때..
                if temp in lottoNum:                    # temp에 임시 생성된 숫자가 이미 리스트에 존재하는지 확인
                    continue;                           # 이미 존재하면 랜덤수 다시 생성
                else:                                   # 리스트에 없는 숫자면 리스트에 넣고 while탈출
                    lottoNum += [temp];
                    break;
    # 1부터 45의 보너스 넘버 1개 생성
    while True:
        temp = random.randint(1, 45);                   # 임시 보너스 숫자 생성
        if temp in lottoNum:                            # 생성된 숫자가 리스트 lottoNum에 있는지 확인
            continue;
        else:
            bonusNum += [temp];
            break;

def makeUserNum(arg):
    # 사용자 입력 Num
    # int형 List에 복권 번호 순으로 dictionary 변수 userNum을 만든다.
    for i in range(1, 6):                               # 5천원짜리 복권 한장에는 5세트의 로또 수 조합이 있다.
        num = input('%d번째 복권 번호 입력 (1~45, 6개): ' % (i));
        num = num.split(' ');
        for j in range(0, 6):
            num[j] = int(num[j]);                       # 복권 번호를 int형으로 바꿔준다.
        userNum[str(i) + '번'] = num;                   # 구분이 용이하도록 사전 형식으로 만들어준다.

def calCnt(lottoNum, bonusNum, userNum):
    # userNum 예시: {'1번':[12, 37, 43, 10, 34, 30, '1등'], '2번':[~], ~}
    # 사용자 입력 Num에서 로또번호, 보너스번호 몇개씩 맞았는지 카운트 후 등수를 List에 삽입
    for j in range(1, 6):
        lcnt = 0;
        blcnt = 0;
        if bonusNum[0] in userNum[str(j) + '번']:    # 보너스 번호가 맞았는지 카운트
            blcnt += 1;
        for i in lottoNum:                          # 로또 번호 몇개 맞았는지 카운트
            if i in userNum[str(j) + '번']:
                lcnt += 1;
        if lcnt == 6:                               # userNum 딕셔너리에 맞춘 수와 일치하는 등수 입력
            userNum[str(j) + '번'] += ['1등'];
        elif lcnt == 5:
            if blcnt == 1:
                userNum[str(j) + '번'] += ['2등'];
            else:
                userNum[str(j) + '번'] += ['3등'];
        elif lcnt == 4:
            userNum[str(j) + '번'] += ['4등'];
        elif lcnt == 3:
            userNum[str(j) + '번'] += ['5등'];
        else:
            userNum[str(j) + '번'] += ['꽝'];

def makePrize(userNum):
    # 2020년 기준 로또는 매주 9백억원 가량 판매되며 판매액의 50%가 당첨금으로 지급된다.
    # 1등 = 당첨금의 75% / 2등 = 12.5% / 3등 = 12.5% / 4등 = 50000원 / 5등 5000원
    temp = random.randint(700,1000) / 2;
    prize = {'1등':temp*0.75, '2등':temp*0.125, '3등':temp*0.125, '4등':50000, '5등':5000};
    return prize;

def showPrize(userNum):
    # 당첨금액을 복권 순서대로 보여준다.
    # userNum 예시: {'1번':[12, 37, 43, 10, 34, 30, '1등'], '2번':[~], ~}
    for i in userNum.keys():
        if userNum[i][-1] == '꽝':
            continue;
        elif userNum[i][-1] == '4등' or userNum[i][-1] == '5등':
            print('%s 복권 ' %(i), end='');
            print('%10d 원' %(prize[userNum[i][-1]]) );
        else:
            print('%s 복권 ' %(i), end='');
            print('%10.3f 억 원' %(prize[userNum[i][-1]]) );



while True:
    temp = input('Y: 시작, Q: 종료 > ');
    temp = temp.lower();
    if  temp == 'y':
        print('Start Lotto Game');

        lottoNum = [];
        bonusNum = [];
        userNum = {};
        prize = {};

        makeNum(lottoNum, bonusNum);
        prize = makePrize(userNum);
        print(prize);
#        print(lottoNum);
#        print(bonusNum);

        makeUserNum(userNum);
        calCnt(lottoNum, bonusNum, userNum);

        showPrize(userNum);

        print('The End');
    elif temp == 'q':
        break;
print('프로그램 종료');