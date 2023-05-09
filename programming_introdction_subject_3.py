import divide_rectangle_module as drm


if __name__ == "__main__":
    w, h = input("직사각형의 가로와 세로를 입력해주세요 : ").split()
    drm.get_square_area(int(w), int(h))
