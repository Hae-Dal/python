"""
아래의 실행 결과를 참고하여 단어장에서 무작위로 출력되는 영어 단어를
맞추는 게임을 만드시오. (사용하는 단어장은 아래 예시와 같다)
"""
import random

words = {"Football": "축구", "Car": "자동차", "Pencil": "연필", "Doll": "인형", "Eraser": "지우개", "Clock": "시계"}

while True:
    problem = random.choice(list(words.keys()))
    print(f"영어 입력 : {problem}")

    while True:
        answer = input("한글 입력 : ")

        if words[problem] == answer:
            print("정답입니다!")
            break
        else:
            print("틀렸습니다!!")
