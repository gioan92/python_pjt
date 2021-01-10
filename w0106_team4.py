# 항공권 예매 시스템

#항공권 예약, 예약내역 확인, 예약 취소, 포인트 적립 밎 조회 가능한 시스템

# 예약하기
    #     예약 가능한 항공권의 항공번호, 날짜, 출발/도착지(종류는 서울->제주로 고정), 좌석종류(이코노미: 50,000원/비즈니스: 100,000원/퍼스트: 200,000원)별 가격 출력
    #     항공번호, 인원수, 좌석종류(이코노미/비즈니스/퍼스트) 선택
    #     결제창이동
        #     총 결제 금액 출력(총 금액 = 좌석 종류별 가격 * 인원수)
        #     while 예약완료 == False
            #     결제 방법 선택(포인트/돈)
            #     결제 방법으로 포인트를 선택한 경우
            #          총 결제 금액이 포인트 보유량 보다 크면
            #                 포인트 사용 불가 메시지 출력
            #                 결제 방법 선택으로 돌아가기(continue)
            #          총 결제 금액이 포인트 보유량 보다 작거나 같으면
            #               포인트 차감
            #               예약 완료
            #     결제 방법으로 돈을 선택한 경우
            #           포인트 적립(총 금액의 10%)
            #           결제 됐다고 출력
            #           예약 완료
# 예약확인
        #           여태까지 예약한 항공편 리스트 출력
        #           항공번호, 날짜, 인원수, 출발지/도착지, 좌석종류 출력
        #           ex) k1111, 2021년 1월 6일, 2명, 서울/제주, 이코노미
        #               k2222, 2021년 1월 10일, 1명, 서울/제주, 비즈니스
# 포인트확인
        #           누적 포인트 출력
# 예약취소
        #           여태까지 예약한 항공편 리스트 출력(예약확인 함수 재활용)
        #           취소할 항공번호 입력 받기(ex)k1111)
        #           항공편 리스트에 입력받은 항공번호가 존재하면
        #               해당 예약편 리스트에서 삭제
        #           항공편 리스트에 입력받은 항공번호가 존재하지 않으면
        #               해당 항공편이 예매내역에 없습니다 출력
# 시스템 종료( 'q' )

airinfo = ( {'항공번호':'k1111', '날짜':'2021년 1월 6일', '출발/도착지':'서울/제주'},
            {'항공번호':'k2222', '날짜':'2021년 1월 7일', '출발/도착지':'서울/제주'},
            {'항공번호':'k3333', '날짜':'2021년 1월 7일', '출발/도착지':'서울/제주'},
            {'항공번호':'k4444', '날짜':'2021년 1월 7일', '출발/도착지':'서울/제주'},
            {'항공번호':'k5555', '날짜':'2021년 1월 8일', '출발/도착지':'서울/제주'},
            {'항공번호':'k6776', '날짜':'2021년 1월 8일', '출발/도착지':'서울/제주'},
            {'항공번호':'k7777', '날짜':'2021년 1월 8일', '출발/도착지':'서울/제주'},
            {'항공번호':'k8888', '날짜':'2021년 1월 9일', '출발/도착지':'서울/제주'},
            {'항공번호':'k9999', '날짜':'2021년 1월 9일', '출발/도착지':'서울/제주'},
            {'항공번호':'k1010', '날짜':'2021년 1월 9일', '출발/도착지':'서울/제주'},
            {'항공번호':'k1212', '날짜':'2021년 1월 9일', '출발/도착지':'서울/제주'},
            {'항공번호':'k1313', '날짜':'2021년 1월 10일', '출발/도착지':'서울/제주'})

def userinsert():
    print('------------\n'
          '<메뉴를 선택하세요>\n'
          '1. 예약하기\n'
          '2. 예약확인\n'
          '3. 포인트확인\n'
          '4. 예약취소\n'
          '   종료(q)\n'
          '------------\n');
    while True:
        # 1/2/3/4/q 입력을 받는다.
        select = input('>> ');
        try:
            # 숫자가 아니면 에러발생, 1~4가 아니면 에러발생
            if int(select) not in range(1,5):
                raise ValueError;
            else:
                # 1~4의 숫자이면 str->int 변경 후 return
                select = int(select);
                return select;
        except:
            # 숫자 검증 단계에서 에러 발생 시 알파벳인지 한번 더 확인
            if select.isalpha():
                # 알파벳이면 소문자로 변경 후 'q'인지 확인
                select = select.lower();
                if select == 'q':
                    # 'q'이면 return
                    return select;
                else:
                    print('잘못된 입력입니다. 다시 입력하세요.');
            else:
                print('잘못된 입력입니다. 다시 입력하세요.');

def reservation(userinfo, point):
    for info in airinfo:
    # 항공기 정보 가격별 출력
        print('%s %13s %s\t\t' % (info['항공번호'], info['날짜'], info['출발/도착지']), end='' );
        print('Economy: 50,000원 / Business: 100,000원 / First: 200,000원');

    temp = [];
    # 항공기 정보 튜플에서 항공기 번호만 가져온다. (각 항공기 별 정보는 딕셔너리로 되어있음)
    for i in airinfo:
        temp.append(i['항공번호']);

    while True:
    # 항공기번호 입력
        airnum = input('항공번호를 입력하세요. > ');
        if airnum in temp:
        # 유효한 항공편이면 while문 탈출
            break;
        else:
            print('유효하지 않은 항공편 입니다. 다시 입력하세요.');

    while True:
    # 인원수 입력
        p = input('인원수를 입력하세요. > ');
        try:
            p = int(p);
            break;
        except:
            print('잘못된 입력입니다. 다시 입력하세요.');

    while True:
    # 좌석종류 입력
        seat = input('좌석종류를 입력하세요. > ');
        if seat.isalpha():
            seat = seat.lower();
            if seat in ['economy', 'business', 'first']:
            # 유효한 입력이면 while문 탈출
                break;
            else:
                print('잘못된 입력입니다. 다시 입력하세요.');
        else:
            print('잘못된 입력입니다. 다시 입력하세요.');

    # 사용자의 구매예정인 임시 데이터를 만든다.
    # 해당 항공편 정보에 인원수, 좌석종류 추가하여 usertemp 임시 저장
    usertemp = airinfo[temp.index(airnum)];
    usertemp['인원수'] = p;
    usertemp['좌석종류'] = seat;

    # 임시 저장한 usertemp의 결제를 위해 pay함수를 호출한다. 결제완료시 항공편 데이터가 저장될 최종 사용자정보 userinfo가 인수로 포함된다.
    pay(userinfo,usertemp, point);

def pay(userinfo,usertemp, point):
    # 티켓 구매 완료시 True가 될 변수, 구매 완료 시 while문 탈출
    confirmreservation = False;

    pricetable = {'economy': 50000, 'business': 100000, 'first':200000};
    price = pricetable[usertemp['좌석종류']];

    while confirmreservation == False:
        wayofpayment = input('결제 방법을 입력하세요. (포인트/돈) > ');
        if wayofpayment not in ['포인트', '돈']:
            print('잘못된 입력입니다. 다시 입력하세요.');
            continue;
        if wayofpayment == '포인트':
            if point == list() or point[0] < price:
                print('포인트가 부족합니다.');
                continue;
            else:
                point[0] -= price;
                usertemp['earn point'] = 0;
                print('포인트를 사용하여 결제 완료되었습니다.');
                break;
        else:
            if point == list():
                point.append(price * 0.1);
            else:
                point[0] += price * 0.1;
            usertemp['earn point'] = price * 0.1;
            print('카드/현금을 사용하여 결제 완료되었습니다.');
            confirmreservation = True;

    userinfo.append(usertemp);
    print(userinfo, point);

def yourreservation(userinfo):
    # 예약된 항공편 리스트 출력
    if userinfo == list():
    # 예약 내역이 비었을 경우
        print('예약 내역이 없습니다.');
        return;
    for i in userinfo:
        # 항공번호, 날짜, 인원수, 출발지/도착지, 좌석종류 출력
        print('%s, %s, %s명, %s, %s, earn pts: %s' % ( i['항공번호'], i['날짜'], i['인원수'], i['출발/도착지'], i['좌석종류'], i['earn point']) );
    print();
        # ex) k1111, 2021년 1월 6일, 2명, 서울/제주, 이코노미
        #     k2222, 2021년 1월 10일, 1명, 서울/제주, 비즈니스
        # + earn point 추가함
        #     k3333, 2021년 1월 10일, 2명, 서울/제주, business, earn pts: 5000

def yourpoint(point):
    # 누적 포인트 출력
    if point == list():
        print('항공사 포인트 0 p 보유 중 입니다.\n');
    else:
        print('항공사 포인트 %s p 보유 중 입니다.\n' %(point[0]));
        # 포인트 누적하여 결제 및 추후 돈으로 결제한 항공편 예약 취소 시 패널티로 '-'포인트 적용
        if point[0] < 0:
            print('포인트로 결제한 항공편 및 타 항공편 취소로 패널티 적용 중 입니다.')

def canclereservation(userinfo, point):
    # 예약된 항공편 리스트 출력(예약확인 함수 재활용)
    yourreservation(userinfo);
    temp = [];
    # 리스트 temp에 userinfo key(항공번호)의 value를 삽입한다.
    for i in range(len(userinfo)):                  # 인덱스를 사용하지 않고 바로 for i in userinfo:에서 temp.append(i['항공번호']) 해도 됩니다.
        temp.append(userinfo[i]['항공번호']);
    # 예약내역이 비었을 경우 에러 메세지 출력 및 메뉴선택으로 되돌아감
    if temp == list():
        print('항공편을 먼저 예약하세요.\n');
        return;

    # 취소할 항공번호 입력 받기(ex)k1111)
    airnum = input('취소할 항공번호를 입력하세요. > ');
    if airnum in temp:
        # 항공편 리스트에 입력받은 항공번호가 존재하면
        #   해당 예약편 리스트에서 삭제[0] -= userinfo[temp.index(airnum)]['earn point'];
        #         userinfo.remove(userinfo[temp.index(airnum)]);
        #         print('해당 항공편이 예약 취소되었습니다.\n');
        #     else:
        #         # 항공편 리스트에 입력받은 항공번호가 존재하지 않으면
        #         #   해당 항공편이 예매내역에 없습니다 출력
        point
        print('해당 항공편이 예약 내역에 없습니다.\n');

point = [];
# 보유 포인트
# point = [35000];
# 음수인 경우가 발생하는데, 이는 포인트 누적 후 사용한 뒤 돈으로 결제한 다른 항공편을 취소했을때 발생합니다.
# 이 경우 패널티 적용으로 '-' 포인트 그대로 적용하였습니다.
userinfo = [];
# 사용자 정보
# ex) k1111, 2021년 1월 6일, 2명, 서울/제주, 이코노미, earn point(취소 시 point 복구를 위해 추가했습니다.)
# userinfo = [{'항공번호':'k1111', '날짜':'2021년 1월 6일', '인원수':4, '출발/도착지':'서울/제주', '좌석종류':'Economy', 'earn point':5000},
#             {'항공번호':'k8888', '날짜':'2021년 1월 9일', '인원수':2, '출발/도착지':'서울/제주', '좌석종류':'Business', 'earn point':10000},
#             {'항공번호':'k9999', '날짜':'2021년 1월 9일', '인원수':1, '출발/도착지':'서울/제주', '좌석종류':'First', 'earn point':20000}];

print('저희 항공사를 찾아주셔서 감사합니다.');
while True:
    # 유저insert()
    select = userinsert();
    if select == 'q':
        break;
    elif select == 1:
        reservation(userinfo, point);
    elif select == 2:
        yourreservation(userinfo);
    elif select == 3:
        yourpoint(point);
    else:
        canclereservation(userinfo, point);

print('이용해주셔서 감사합니다.');

