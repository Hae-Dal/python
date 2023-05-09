import mp3_player_module as mp3


def menu():
    print("*" * 25)
    print("1. 곡 추가")
    print("2. 곡 제거")
    print("3. 곡 리스트 출력")
    print("4. 일반 재생 모드")
    print("5. 셔플 재생 모드")
    print("6. 종료")
    print("*" * 25)


if __name__ == "__main__":
    while True:
        menu()
        op = int(input(""))

        if op == 1:
            music_name = input("추가할 곡을 입력해주세요: ")
            mp3.add_music(music_name)

        elif op == 2:
            music_name = input("제거할 곡을 입력해주세요: ")
            mp3.del_music(music_name)

        elif op == 3:
            mp3.print_music()

        elif op == 4:
            mp3.general_play_mode()

        elif op == 5:
            mp3.shuffle_play_mode()

        else:
            print("프로그램을 종료합니다.")
            break
