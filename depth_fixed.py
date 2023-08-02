import random


def main():
    global center, half, screen, count, face
    center = [40, 30, 20]  # center of cube
    half = 39 / 2  # half-length of cube
    screen = []
    face = ""
    count = 0
    focus = 20

    for i in range(1, 101):
        screen.append([])
        for j in range(1, 151):
            count = 0
            face = ""
            for k in range(0, 100):
                rnumx = random.uniform(-0.02, 0.02)
                rnumy = random.uniform(-0.02, 0.02)

                current = [j + 0.5, i + 0.5, 1]  # the node ray goes through
                camera = [current[0] + rnumx, current[1] + rnumy, 1]  # random point next to the center of current pixel

                l = (current[0] ** 2 + current[1] ** 2 + 1) ** 0.5  # length between center of current pixel to camera
                focuspoint = [current[0] * focus / l, current[1] * focus / l, current[2] * focus / l]

                direction = [focuspoint[0] - camera[0], focuspoint[1] - camera[1], focuspoint[2] - 1]
                l = (direction[0] ** 2 + direction[1] ** 2 + direction[2] ** 2) ** 0.5
                normalised = [direction[0] / l, direction[1] / l, direction[2] / l]

                check_face(normalised, camera)

            coefficient = count / 100
            num = str(int(255 * coefficient))

            paint_screen(face, i, num)

    create_file()


def intersect(d, a, sign, camera):
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

    t = (center[a] + sign * half - camera[a]) / d[a]
    ra = camera[b] + t * d[b]
    rb = camera[c] + t * d[c]
    if ((center[b] - half) < ra < (center[b] + half) and (center[c] - half) < rb < (center[c] + half)):
        count += 1
        return True
    return False


def check_face(normalised, camera):
    global face

    if intersect(normalised, 2, -1, camera):
        face = "f"
    elif intersect(normalised, 0, -1, camera):
        face = "l"
    elif intersect(normalised, 1, -1, camera):
        face = "d"  # down
    elif intersect(normalised, 2, 1, camera):
        face = "b"
    elif intersect(normalised, 0, 1, camera):
        face = "r"
    elif intersect(normalised, 1, 1, camera):
        face = "t"
    else:
        face = "n"


def paint_screen(face, i, num):
    global screen

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


def create_file():
    global screen

    f = open("cube_depth_fixed.ppm", "w", encoding="ASCII")
    f.write("P3\n")
    f.write("150 100\n")
    f.write("255\n")
    for y in range(99, -1, -1):
        for x in range(0, 150):
            f.write("" + screen[y][x] + "\n")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
