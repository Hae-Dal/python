"""
가로가 32m, 세로가 48m인 직사각형의 밭을 똑같은 크기의 정사각형으로
분할하여 나누어 주려고 한다. 정사각형의 크기를 가장 크게 했을 때 정사각형의
넓이를 구하는 모듈을 만들어 구현하시오. hint: 최대공약수
"""
import math


def _gcd(a: int, b: int):
    if a < b:
        a, b = b, a

    while b != 0:
        r = a % b
        a, b = b, r

    return a


def get_square_area(width: int, height: int):
    print(f"정사각형 한 변의 길이 : {_gcd(width, height)}")
    print(f"정사각형 한 개 면적 : {int(math.pow(_gcd(width, height), 2))}")
    print(f"정사각형 개수 : {(width*height)/math.pow(_gcd(width, height), 2)}")
