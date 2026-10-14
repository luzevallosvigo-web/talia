# Creates the three Talia app icons (needs: pip install pillow)
from PIL import Image, ImageDraw, ImageFont

def font(size):
    for f in ["DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"]:
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default()

def icon(size, maskable, path):
    im = Image.new("RGB", (size, size), "#D12A20")          # Milan Metro M1 red
    d = ImageDraw.Draw(im)
    inset = size * (0.2 if maskable else 0.11)
    d.rectangle([inset, inset, size - inset, size - inset], outline="#FFFFFF", width=max(2, int(size * 0.025)))
    d.text((size / 2, size / 2 + size * 0.01), "T", font=font(int(size * (0.42 if maskable else 0.55))), fill="#FFFFFF", anchor="mm")
    im.save(path)

icon(192, False, "icon-192.png")
icon(512, False, "icon-512.png")
icon(512, True, "icon-maskable-512.png")
