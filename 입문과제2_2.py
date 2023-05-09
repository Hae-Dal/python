import random
import music_module as mm


choice = 1

while choice > 0 and choice < 6:
    choice = int(input("1.곡 추가 2.곡 제거 3.곡 리스트 출력 4.일반 재생 모드 5.셔플 재생 모드 기능선택:"))

    if choice == 1:
        new = input("추가할 노래:")
        mm.add_music(new)

    elif choice == 2:
        delite = input("삭제할 노래:")
        mm.del_music(delite)

    elif choice == 3:
        mm.music_list()

    elif choice == 4:
        mm.music_play()

    elif choice == 5:
        mm.music_shuffle()