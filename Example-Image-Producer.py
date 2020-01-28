from PIL import Image, ImageFont, ImageDraw

def add_time():
    img = Image.open("blank.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 52)
    test = "Sample Text"
    draw.text((50, 50), test, (0), font=font)
    img.convert('L')
    img.save("out.png")

add_time()
