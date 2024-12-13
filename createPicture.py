from PIL import Image, ImageDraw


def createPicture(pattern, quantity):

    im = Image.new(mode="L",size=(1000,1000), color="white")
    dr = ImageDraw.Draw(im)
    CDIRW, CDIRB, MOVEW, MOVEB, COLORW, COLORB = pattern
    direction = "forward"
    count = 0
    x, y = (int(im.width/2), int(im.height/2))

    MT = {
        "qW": {
            "forward": {"1": ["right", MOVEW, 0, COLORW],    "-1": ["left", "-"+MOVEW, 0, COLORW]}, 
            "backward":{"1": ["left", "-"+MOVEW, 0, COLORW],    "-1": ["right", MOVEW, 0, COLORW]},
            "right":   {"1": ["backward", 0, "-"+MOVEW, COLORW], "-1": ["forward", 0, MOVEW, COLORW]},
            "left":    {"1": ["forward", 0, MOVEW, COLORW], "-1": ["backward", 0, "-"+MOVEW, COLORW]}},
        "qB": {
            "forward": {"1": ["right", MOVEB, 0, COLORB],    "-1": ["left", "-"+MOVEB, 0, COLORB]}, 
            "backward":{"1": ["left", "-"+MOVEB, 0, COLORB],    "-1": ["right", MOVEB, 0, COLORB]},
            "right":   {"1": ["backward", 0, "-"+MOVEB, COLORB], "-1": ["forward", 0, MOVEB, COLORB]},
            "left":    {"1": ["forward", 0, MOVEB, COLORB], "-1": ["backward", 0, "-"+MOVEB, COLORB]}}
        }
    while count < quantity:
        state = "qW"
        if im.getpixel((x, y)) == 0:
            state = "qB"

        if state == "qW":
            direction, addx, addy, color = MT[state][direction][CDIRW]
            if color == "1":
                dr.point((x, y), 0)
            x += int(addx)
            y += int(addy)
        else:
            direction, addx, addy, color = MT[state][direction][CDIRB]
            if color == "1":
                dr.point((x, y), 255)
            x += int(addx)
            y += int(addy)
        count += 1
        
    im.show()

# createPicture(['1', '-1', '1', '1', '1', '1'], 11000)