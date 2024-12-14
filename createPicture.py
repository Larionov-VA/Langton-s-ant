from PIL import Image, ImageDraw


def createPicture(pattern, quantity):

    im = Image.new(mode="RGB",size=(800,600), color="white")
    dr = ImageDraw.Draw(im)
    dr.rectangle([(5,5), (int(im.width)-5, int(im.height)-5)], width=5, outline="red")
    dr.rectangle([(int(im.width/6), int(im.height/6)), (int(im.width/6)+int(im.width/6), int(im.height/6)+int(im.height/6))], width=5, outline="black")
    dr.rectangle([(int(im.width/6)*4, int(im.height/6)*4), ((int(im.width/6)*4+int(im.width/6)), (int(im.height/6)*4+int(im.height/6)))], width=5, outline="black")
    dr.rectangle([(int(im.width/6)*4, int(im.height/6)), ((int(im.width/6)*4+int(im.width/6)), (int(im.height/6)+int(im.height/6)))], width=5, outline="black")
    dr.rectangle([(int(im.width/6), int(im.height/6)*4), ((int(im.width/6)+int(im.width/6)), (int(im.height/6)*4+int(im.height/6)))], width=5, outline="black")
    CDIRW, CDIRB, MOVEW, MOVEB, COLORW, COLORB = pattern
    direction = "forward"
    count = 0
    x, y = (int(im.width/2), int(im.height/2))
    # print(im.getpixel((x, y)))
    MT = {
        "qW": {
            "forward": {"1": ["right", MOVEW, 0, COLORW],    "-1": ["left", "-"+MOVEW, 0, COLORW],    "0": ["forward", 0, MOVEW, COLORW]}, 
            "backward":{"1": ["left", "-"+MOVEW, 0, COLORW],    "-1": ["right", MOVEW, 0, COLORW],    "0": ["backward", 0, "-"+MOVEW, COLORW]},
            "right":   {"1": ["backward", 0, "-"+MOVEW, COLORW], "-1": ["forward", 0, MOVEW, COLORW],    "0": ["right", MOVEW, 0, COLORW]},
            "left":    {"1": ["forward", 0, MOVEW, COLORW], "-1": ["backward", 0, "-"+MOVEW, COLORW],    "0": ["left", "-"+MOVEW, 0, COLORW]}},
        "qB": {
            "forward": {"1": ["right", MOVEB, 0, COLORB],    "-1": ["left", "-"+MOVEB, 0, COLORB],    "0": ["forward", 0, MOVEW, COLORW]}, 
            "backward":{"1": ["left", "-"+MOVEB, 0, COLORB],    "-1": ["right", MOVEB, 0, COLORB],    "0": ["backward", 0, "-"+MOVEW, COLORW]},
            "right":   {"1": ["backward", 0, "-"+MOVEB, COLORB], "-1": ["forward", 0, MOVEB, COLORB],    "0": ["right", MOVEW, 0, COLORW]},
            "left":    {"1": ["forward", 0, MOVEB, COLORB], "-1": ["backward", 0, "-"+MOVEB, COLORB],    "0": ["left", "-"+MOVEW, 0, COLORW]}}
        }
    while count < quantity:
        if im.getpixel((x, y)) == (255, 0, 0):
            break
        state = "qW"
        if im.getpixel((x, y)) == (0, 0, 0):
            state = "qB"

        if state == "qW":
            direction, addx, addy, color = MT[state][direction][CDIRW]
            if color == "1":
                dr.point((x, y), (0, 0, 0))
            x += int(addx)*2
            y += int(addy)*2
        else:
            direction, addx, addy, color = MT[state][direction][CDIRB]
            if color == "1":
                dr.point((x, y), (255, 255, 255))
            x += int(addx)*2
            y += int(addy)*2
        count += 1
        
        # print(im.getpixel((x, y)))
        
    im.show()
    # im.save("a.png")

# createPicture(['1', '-1', '1', '1', '1', '1'], 1000000)
# createPicture(['1', '1', '1', '2', '1', '0'], 1000000) #РОООООООМБ
# createPicture(['-1', '1', '1', '3', '1', '1'], 100000000000000) #Красивая фигура
# createPicture(['1', '1', '4', '1', '1', '1'], 1000000) #Красивая фигура 2
