words = {
    "apple": "사과",
    "chair": "의자",
    "doll": "인형",
    "book": "책",
    "piano": "피아노"
}


def transKor(ekey: str):
    global words
    print(f"{ekey}:{words.get(ekey)}")
