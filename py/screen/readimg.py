import cv2


def main():
    f = open('pikaqiu.png')
    img = cv2.imread('pikaqiu.png')
    print(f)
    print(img.shape)
    print(img.size)
    print(img.dtype)
    print(img[10, 10])
    print(img.item(10, 10, 0))
    # for i in range(0, 3):
    #     img.itemset((10, 10, i), 0)
    # print(img[10, 10])

    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 3):
                img.itemset((i, j, k), 0)

    cv2.imshow("Display window", img)
    k = cv2.waitKey(0)


if __name__ == '__main__':
    main()
