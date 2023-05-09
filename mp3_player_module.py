"""
mp3 플레이어 모듈을 만드시오. 일반 재생 모드
선택시 곡 리스트를 출력하고, 셔플 재생 모드 선택시 랜덤하게 리스트를 섞은
곡 리스트를 출력한다.
"""
import copy
import random

music_list: list[str] = []


# 곡 추가
def add_music(music_name: str):
    global music_list

    if not music_name.endswith(".mp3"):
        music_name += ".mp3"

    if music_name in music_list:
        print("해당 곡이 이미 곡 리스트에 존재합니다.")
    else:
        music_list.append(music_name)
        print("-" * 5, f"곡 추가 : {music_name}", "-" * 5)


# 곡 제거
def del_music(music_name: str):
    global music_list

    if not music_name.endswith(".mp3"):
        music_name += ".mp3"

    if music_name in music_list:
        music_list.remove(music_name)
        print("-" * 5, f"곡 삭제 : {music_name}", "-" * 5)
    else:
        print("해당 곡이 리스트에 없습니다.")


# 곡 리스트 출력
def print_music():
    global music_list

    print("-" * 5, "곡 리스트 출력", "-" * 5)

    for item in music_list:
        print(item)


# 일반 재생 모드
def general_play_mode():
    print("-" * 5, "일반 재생 모드", "-" * 5)

    print_music()


# 셔플 재생 모드
def shuffle_play_mode():
    global music_list
    copy_list = copy.deepcopy(music_list)
    random.shuffle(copy_list)

    print("-" * 5, "셔플 재생 모드", "-" * 5)

    print("-" * 5, "곡 리스트 출력", "-" * 5)
    for item in copy_list:
        print(item)
