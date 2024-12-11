from PIL import Image, ImageDraw, ImageFont
import os

symbols = ["∧", "∨", "∃", "⊂", "⊃"]

fonts = [
    "D:\Downloads\\fonts\dejavu-fonts-ttf-2.37\dejavu-fonts-ttf-2.37\\ttf\DejaVuSans.ttf",
    "D:\Downloads\\fonts\dejavu-fonts-ttf-2.37\dejavu-fonts-ttf-2.37\\ttf\DejaVuSansMono-BoldOblique.ttf",
    "D:\Downloads\\fonts\dejavu-fonts-ttf-2.37\dejavu-fonts-ttf-2.37\\ttf\DejaVuSerifCondensed.ttf",
    "D:\Downloads\\fonts\\freeserif\FreeSerif\FreeSerif.ttf"
]

width = 100
height = 100
output_dir = "dataset"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_image(symbol, font_path, file_path):
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font_path, size=50)

    bbox = draw.textbbox((0, 0), symbol, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(position, symbol, font=font, fill=(0, 0, 0))

    img.save(file_path)

for symbol in symbols:
    for i, font_path in enumerate(fonts):
        file_name = f"{symbol}_{i+1}.png"
        file_path = os.path.join(output_dir, file_name)
        generate_image(symbol, font_path, file_path)
        print(f"Generated {file_path}")