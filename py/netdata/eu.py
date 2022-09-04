import screen.screen as screen

png_bytes = screen.screen_cap_from_phone()
print(len(png_bytes))
win_array = bytearray(png_bytes)
f = open('test.png', 'rb')
linux_bytes = f.read()
f.close()
print(linux_bytes)
print(len(linux_bytes))
linux_bytes_array = bytearray(linux_bytes)
for i in range(0, len(linux_bytes_array)):
    # print(win_array[i])
    if linux_bytes_array[i] != win_array[i]:
        print("i={} \t linux_byte={},win_byte={}".format(i, linux_bytes_array[i], win_array[i]))
print(win_array[1983])
print(win_array[1984])
