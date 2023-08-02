def main():
    global center, half, screen, count
    center = [40, 30, 20]  # center of cube
    half = 39 / 2  # half-length of cube
    screen = []
    count = 0

    for i in range(1, 101):
        screen.append([])
        for j in range(1, 151):
            count = 0
            face = ""
            for m in (0.125, 0.375, 0.625, 0.875):
                for n in (0.125, 0.375, 0.625, 0.875):
                    current = [j + m, i + n, 1]  # the node ray goes through
                    l = ((i + n + 0.5) ** 2 + (j + m + 0.5) ** 2 + 1) ** 0.5
                    d = [current[0] / l, current[1] / l, current[2] / l]  # normalise
                    if intersect(d, 2, -1):
                        face = "f"
                    elif intersect(d, 0, -1):
                        face = "l"
                    elif intersect(d, 1, -1):
                        face = "d"  # down
                    elif intersect(d, 2, 1):
                        face = "b"
                    elif intersect(d, 0, 1):
                        face = "r"
                    elif intersect(d, 1, 1):
                        face = "t"
                    else:
                        face = "n"

            coefficient = count / 16

            num = str(int(255 * coefficient))
            if num != "0" and num != "255":
                print(num)
            if face == "f":
                screen[i - 1].append(num + " " + num + " " + num)  # front
            if face == "l":
                screen[i - 1].append(num + " 0 0")  # left
            if face == "d":
                screen[i - 1].append(num + " 0 " + num)  # bottom
            if face == "b":
                screen[i - 1].append(num + " " + num + " 0")  # back
            if face == "r":
                screen[i - 1].append("0 0 " + num)  # right
            if face == "t":
                screen[i - 1].append("0 " + num + " 0")  # top
            if face == "n":
                screen[i - 1].append("0 0 0")

    create_file()


def intersect(d, a, sign):
    global count
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
        count += 1
        return True
    return False


def create_file():
    f = open("cube_16.ppm", "w", encoding="ASCII")
    f.write("P3\n")
    f.write("150 100\n")
    f.write("255\n")
    for y in range(99, -1, -1):
        for x in range(0, 150):
            f.write("" + screen[y][x] + "\n")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
