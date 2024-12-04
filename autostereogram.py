from PIL import Image

def create_autostereogram(depth_map, pattern_image):
    width, height = depth_map.size

    # Create a new image for the autostereogram
    autostereogram = Image.new('RGB', (width, height))

    # Tile the pattern image horizontally and vertically
    pattern_width, pattern_height = pattern_image.size
    for x in range(width):
        for y in range(height):
            # Calculate the shift based on depth map
            shift = int(depth_map.getpixel((x, y)) / 255 * pattern_width)

            # Wrap around the pattern image
            pattern_x = (x + shift) % pattern_width
            pattern_y = y % pattern_height  # Wrap vertically to stay within bounds

            autostereogram.putpixel((x, y), pattern_image.getpixel((pattern_x, pattern_y)))

    return autostereogram

# Load the depth map (grayscale image where white is closest, black is farthest)
depth_map = Image.open("/home/fjiwad/vision/Vision-Autosterogram/input/bird.png").convert("L") 

# Load or create the pattern image
pattern_image = Image.open("./patterns/base_pattern_vertical.png")

# Generate the autostereogram
autostereogram = create_autostereogram(depth_map, pattern_image)

# Save or display the autostereogram
autostereogram.save("autostereogram1.png")
autostereogram.show()
