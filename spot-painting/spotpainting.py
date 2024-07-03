import colorgram as cg
rgb_colours= []
colours = cg.extract('python-mini-games/spot-painting/img.jpg',36)
for c in colours:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_colour = (r,g,b)
    rgb_colours.append(new_colour)

print(rgb_colours)

