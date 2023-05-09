import random

music = [
        'Dynamite.mp3',
        '다시 여기 바닷가.mp3',
        '마리아 (Maria).mp3',
        'When We Disco.mp3',
        'How You Like That.mp3',
        '눈누난나.mp3',
        '그 여름을 틀어줘.mp3',
        '아리랑~.mp3'
]


def add_music(new):
        global music
        music.append(new + ".mp3")


def del_music(delite:str):
        global music
        music.remove(delite + ".mp3")


def music_list():
        global music
        print(music)


def music_play():
        global music
        print(music)
        print('음악이 재생됩니다.')

def music_shuffle():
        global music
        random.shuffle(music)
        print(music)
        print('음악이 재생됩니다.')
