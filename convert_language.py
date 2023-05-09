def convert_korean_to_special(text):
    korean_dict = {
        'ㄱ': '_|', 'ㅂ': '|_|', 'ㄹ': '|_',
        'ㅅ': '=|', 'ㄴ': '|=|', 'ㅈ': '|=',
        'ㅁ': '-|', 'ㅇ': '|-|', 'ㄷ': '|-',

        'ㅊ': '•_|', ' ': '|_•|', 'ㅍ': '|_•',
        '?': '•=|', 'ㅋ': '|=•|', 'ㅣ': '|=•',
        'ㅎ': '•-|', '!': '|-•|', 'ㅌ': '|-•',

        'ㅏ': ':_|', 'ㅛ': '|_:|', 'ㅕ': '|_:',
        'ㅜ': ':=|', 'ㅑ': '|=:|', 'ㅡ': '|=:',
        'ㅗ': ':-|', 'ㅠ': '|-:|', 'ㅓ': '|-:'
    }

    # 초성, 중성, 종성 자음 리스트
    CHO = [chr(code) for code in range(0x1100, 0x1113)]
    JUNG = [chr(code) for code in range(0x1161, 0x1176)]
    JONG = [chr(code) for code in range(0x11A8, 0x11C3)]

    result = []

    for s in text:
        # 한글 유니코드 범위 내의 문자에 대해서만 분리
        if '가' <= s <= '힣':
            # 유니코드 상에서 한글 자소 분리
            char_code = ord(s) - 44032
            char_first = int(char_code / 588)
            char_second = int((char_code - (588 * char_first)) / 28)
            char_last = int(char_code % 28)

            # 초성 중성 종성 조합으로 구성된 문자열 생성
            result.append(chr(char_first + 0x1100))
            result.append(chr(char_second + 0x1161))
            if char_last != 0:
                result.append(chr(char_last + 0x11A7))
        else:
            result.append(s)

    print(result)

    return result


input_string = input("문자열을 입력하세요: ")
converted_string = convert_korean_to_special(input_string)
print("변환된 문자열: ", converted_string)
