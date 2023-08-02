def main():
    global center, half, screen
    center = [40, 30, 20]  # center of cube
    half = 39 / 2  # half-length of cube
    screen = []

    for i in range(1, 101):
        screen.append([])
        for j in range(1, 151):
            current = [j + 0.5, i + 0.5, 1]  # the node ray goes through
            l = ((i + 0.5) ** 2 + (j + 0.5) ** 2 + 1) ** 0.5
            d = [current[0] / l, current[1] / l, current[2] / l]  # normalise
            if intersect(d, 2, -1):
                screen[i - 1].append("255 255 255")  # front
            elif intersect(d, 0, -1):
                screen[i - 1].append("255 0 0")  # left
            elif intersect(d, 1, -1):
                screen[i - 1].append("255 0 255")  # bottom
            elif intersect(d, 2, 1):
                screen[i - 1].append("255 255 0")  # back
            elif intersect(d, 0, 1):
                screen[i - 1].append("0 0 255")  # right
            elif intersect(d, 1, 1):
                screen[i - 1].append("0 255 0")  # top
            else:
                screen[i - 1].append("0 0 0")

    create_file()


def intersect(d, a, sign):
    if (a == 0):
        b = 1
        c = 2
    if (a == 1):
        b = 0
        c = 2
    if (a == 2):
        b = 0
        c = 1

    t = (center[a] + sign * half) / d[a]
    ra = t * d[b]
    rb = t * d[c]
    if ((center[b] - half) < ra < (center[b] + half) and (center[c] - half) < rb < (center[c] + half)):
        return True
    return False


def create_file():
    f = open("cube.ppm", "w", encoding="ASCII")
    f.write("P3\n")
    f.write("150 100\n")
    f.write("255\n")
    for y in range(99, -1, -1):
        for x in range(0, 150):
            f.write("" + screen[y][x] + "\n")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
