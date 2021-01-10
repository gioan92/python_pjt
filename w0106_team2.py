# < 2조 현관문 도어락 프로그램 >

# 1. 프로그램 기획
# - 4자리 비밀번호의 현관문 도어락 프로세스 구현.

# 2. 시나리오
# 1) 도어락을 열기위해 사용자가 숫자 4개 입력,
# 2) 미리 정해진 비밀번호 4자리와 일치하면 문이 열린다.
# 3) 불일치하면 경고음이 울린다. 재시도 가능.
# 4) 시도 가능 횟수 4번 중 모두 불일치 하는 경우, 1분간 재시도 불가.

# 3. 프로세스
# 0) 도어락 '관리자'가 비밀번호를 설정한다.(입력 받는다.)
# 1) 일반 사용자로부터 4자리 숫자를 입력 받도록 대기한다.
# 2) 사용자가 숫자 입력한다. 시도한다.
# 3) 비밀번호와 사용자 입력 값의 일치 여부 확인
# 3-1) 숫자의 값과 순서가 일치 한다면, - 4)로 진행
# 3-2) 불일치 한다면, ('비밀번호가 잘못되었습니다.')
#      3-2-1) 시도횟수가 3번 이하 일 때, 1)로 돌아간다
#      3-2-2) 시도횟수가 4번 이상 일 때,
#               재시도가 불가능한 잠금상태가 된다.
#               1분 카운트다운이 다되면 1로 돌아간다
# 4) 문이 열린다. ('삐리릭~ 문이 열렸습니다.')
# 5) 위의 절차를 계속 반복한다.
import time;
import sys;
password = [];
# 초기 비밀번호는 전역변수

def makepw():
# 초기 비밀번호 설정
    pwcomplete = False;
    while pwcomplete == False:
    # 비밀번호 설정이 완료되면 while문 탈출
        print('비밀번호 설정')
        sys.stdout.flush();
        # 입력 전 버퍼를 비워준다. 개행문자(enter)를 강제로 여러번 입력했을 경우 의도하지 않은 숫자가 입력될 수 있음
        for i in range(4):
            try:
                # 중간에 문자를 입력하거나 두자리수 이상이면 에러, 처음부터 다시 입력
                temp = int(input());
                if temp not in range(10):
                    raise ValueError;
                else:
                    password.append(temp);
                    if i == 3:
                        # 비밀번호 설정 완료
                        pwcomplete = True;
            except:
                print('처음부터 다시 입력하세요.');
                # 재입력 시 리스트를 클리어해준다.
                password.clear();
                break;

def userpwinsert():
# 사용자 비밀번호 입력
    pwcomplete = False;
    userpw = [];
    # 사용자 비밀번호를 저장할 리스트
    while pwcomplete == False:
    # 비밀번호 입력 완료 시 while문 탈출
        print('비밀번호 입력')
        sys.stdout.flush();
        for i in range(4):
            try:
                temp = int(input());
                if temp not in range(10):
                    raise ValueError;
                else:
                    userpw.append(temp);
                    if i == 3:
                        pwcomplete = True;
            except:
                print('처음부터 다시 입력하세요.');
                userpw.clear();
                break;
    return userpw;
    # while문을 정상 탈출하면 사용자 비밀번호를 리턴

def comppw(userpw):
# 비밀번호 비교 함수
    for i in range(4):
        if userpw[i] == password[i]:
            continue;
        else:
        # 한 자리라도 다르면 False 리턴
            return False;
    # for문을 정상적으로 마치면 True 리턴
    return True;



while True:
    # 사용하는 변수들 초기화
    dooropen = False;
    trynum = 0;
    makepw();
    # 초기 비밀번호 설정
# 설정 비밀번호를 보고싶으면 아래 for문 주석을 지우면 된다.
#    for p in password:
#        print(p, end='');
    print();
    while dooropen == False:
        userpw = [];
        # 사용자 입력 비밀번호 초기화
        userpw = userpwinsert();
        dooropen = comppw(userpw);
        # 비밀번호 비교 후 결과 리턴

# 사용자 입력 비밀번호를 보고싶으면 아래 for문 주석을 지우면 된다.
#        for p in userpw:
#            print(p, end = '');
        print();
        if dooropen == False:
            print('비밀번호가 잘못되었습니다.');
            trynum += 1;
            # 비밀번호 1회 오류 시 try횟수 1 증가
        if trynum >= 4:
            # try횟수 4회 시 0으로 되돌리고, x초 기다림
            trynum = 0;
            print('로그인 시도 4회 초과입니다. 10초 기다리십시오.')
            for i in range(11,0,-1):
            # 기다리는 동안 화면에 카운트다운 출력
                print(i-1);
                time.sleep(1);

        if dooropen:
        # dooropen이 True이면 while문 탈출하고, 초기 비밀번호 설정부터 다시 시작.
            print('삐리릭~ 문이 열렸습니다.');