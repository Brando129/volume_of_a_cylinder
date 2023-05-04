# Create a function that is able to tell what the voulme of a cylinder would be

def get_volume(radius, height):
    pie = 3.14
    radius = radius * radius
    height = height
    volume = round(pie * radius * height)

    return volume

print(get_volume(5, 20))