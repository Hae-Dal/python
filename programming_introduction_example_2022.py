import dict as d


def programming_6():
    temp = int(input("화씨입력"))

    c = (temp - 32) * 5 / 9
    f = c * 9 / 5 + 32

    print(f"섭씨: {c}")
    print(f"화씨: {f}")


def programming_7():
    birth_year = int(input("출생 연도 끝자리 입력:"))
    ages = int(input("만 나이 입력:"))

    if ages >= 65:
        print("언제든지 구매 가능")
    else:
        if birth_year == 1 or birth_year == 6:
            print("월요일 구매 가능")
        elif birth_year == 2 or birth_year == 7:
            print("화요일 구매 가능")
        elif birth_year == 3 or birth_year == 8:
            print("수요일 구매 가능")
        elif birth_year == 4 or birth_year == 9:
            print("목요일 구매 가능")
        elif birth_year == 5 or birth_year == 0:
            print("금요일 구매 가능")


def programming_8():
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()


def programming_9():
    width = 1
    height = 1
    arr = []

    while True:
        area = width * height
        if area > 150:
            print(f"가장 작은 사각형의 넓이 : {arr[0]}")
            print(f"가장 큰 사각형의 넓이 : {area}")
        print(f"사각형의 넓이 : {area}")
        arr.append(area)
        width *= 2
        height *= 3


def programming_10():
    score = []

    count = 0
    for s in score:
        if s < 40:
            count += 1

    sum_score = 0
    for s in score:
        sum_score += s

    ave = sum_score / len(score)

    print(f"40점 미만 과목 수: {count}")
    print(f"평균 점수: {ave}")
    if count == 0 and ave >= 60:
        print("합격")
    else:
        print("불합격")


def programming_11():
    blood_list = [0, 0, 0, 0]

    for i in range(0, 10):
        blood = input("혈액형 입력\n"
                      "A,B,O,AB:")
        if blood is 'A':
            blood_list[0] += 1
        elif blood is 'B':
            blood_list[1] += 1
        elif blood is 'O':
            blood_list[2] += 1
        elif blood is 'AB':
            blood_list[3] += 1

    blood_type(blood_list)


def blood_type(bloods):
    print(f"A형 {bloods[0]}")
    print(f"B형 {bloods[1]}")
    print(f"O형 {bloods[2]}")
    print(f"AB형 {bloods[3]}")


def programming_12():
    eword = input("영어단어 입력")
    d.transKor(eword)

if __name__ == "__main__":
    programming_6()
    programming_7()
    programming_8()
    programming_9()
