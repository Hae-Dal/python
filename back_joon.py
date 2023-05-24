def centers_distance(numbers: list):
    x1 = numbers[0]
    y1 = numbers[1]
    x2 = numbers[3]
    y2 = numbers[4]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

test_num = int(input())

test_cases = []
answer = []

'''
1. 입력은 어떻게 들어오지?
2. 어떻게 입력 받지?
'''
for i in range(test_num):
    numbers = input().split()
    numbers_list = [int(num) for num in numbers]

    test_cases.append(numbers_list)

# 입력 완료 =======================================

for tc in test_cases:
    '''
    1. 어떻게 출력 값이 나올까? -> 문제를 해결하기 위해 어떻게 접근해야할까?
    2. 두 터렛에서 계산한 길이를 반지름으로한 두 원의 교점을 확인해보자!
    3. 류재명이 있을 수 있는 좌표의 수는 두 원의 교점의 수이다. 따라서 좌표의 수는 -1,0,1,2 뿐이다. 
    4. if문으로 분기별 답을 추가한 후 마지막에 출력하자
    '''
    d = centers_distance(tc)
    x1 = tc[0]
    y1 = tc[1]
    x2 = tc[3]
    y2 = tc[4]
    r1 = tc[2]
    r2 = tc[5]

    if d == 0.0:
        if r1 == r2:
            answer.append(-1)
        else:
            answer.append(0)
    else:
    # 두 원의 원점이 다를 때
        if d == r1 + r2 or d == abs(r1 - r2):
            # 두 원의 교점이 1개일 때
            answer.append(1)
        elif r1 + r2 > d > abs(r1 - r2):
            # 두 원의 교점이 2개일 때
            answer.append(2)
        else :
            # 두 원의 교점이 0개일 때
            answer.append(0)


[print(n) for n in answer]
