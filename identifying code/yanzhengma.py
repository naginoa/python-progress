from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母、汉字和数字
def rndChar():
    # 随机数字
    numChr = str(random.randint(0, 9))
    # 随机字母
    letterChr = chr(random.randint(65, 116))
    # 随机汉字
    cnChr = random.choice('我是中文汉字')
    return random.choice((numChr, letterChr, cnChr))

# 随机颜色1
def rndColor():
    return (random.randint(125, 255), random.randint(125, 255), random.randint(125, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 124), random.randint(32, 124), random.randint(32, 124))

# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象，正确显示中文则选择合适的字体（此处选择的是宋体）
font = ImageFont.truetype('C:\simsun.ttc', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor())
# 输出文字
for t in range(4):
    draw.multiline_text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())
# 模糊
image = image.filter(ImageFilter.MinFilter(3))
fileName = 'code.jpg'
image.save(fileName, 'jpeg')
print('save', fileName, 'successfully...')
image.show()