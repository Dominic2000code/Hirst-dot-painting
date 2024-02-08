import colorgram

colors = colorgram.extract('image.jpg', 30)
color_bank = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_bank.append((r, g, b))

print(color_bank)
