class Cryptography:
    crypto = {
        "_|": "ㄱ", "|_|": "ㅂ", "|_": "ㄹ",
        "=|": "ㅅ", "|=|": "ㄴ", "|=": "ㅈ",
        "-|": "ㅁ", "|-|": "ㅇ", "|-": "ㄷ",

        "•_|": "ㅊ", "|_•|": " ", "|_•": "ㅍ",
        "•=|": "?", "|=•|": "ㅋ", "|=•": "ㅣ",
        "•-|": "ㅎ", "|-•|": "!", "|-•": "ㅌ",

        ":_|": "ㅏ", "|_:|": "ㅛ", "|_:": "ㅕ",
        ":=|": "ㅜ", "|=:|": "ㅑ", "|=:": "ㅡ",
        ":-|": "ㅗ", "|-:|": "ㅠ", "|-:": "ㅓ",

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

    def __init__(self, sentence: str):
        self.s = sentence
        if self.__is_korean():
            self.__separate_sentence()


    def __separate_sentence(self):

        chosungs = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        jungsungs = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        jongsungs = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

        result = []

        for char in self.s:
            if '가' <= char <= '힣':
                code = ord(char) - 44032
                jong = code % 28
                jung = ((code - jong) // 28) % 21
                cho = (((code - jong) // 28) - jung) // 21

                result.append(chosungs[cho])
                result.append(jungsungs[jung])
                result.append(jongsungs[jong])
            else:
                result.append(char)

        return result

    # 한글인지 아닌지 판별
    def __is_korean(self):
        for char in self.s:
            if '가' <= char <= '힣':
                return True
        return False
