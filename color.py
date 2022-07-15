from PIL import Image
from urllib.request import urlopen
import io

def extract_color(image_file, resize=150):
    # Resize image to speed up processing
    img = Image.open(image_file)
    img = img.copy()
    img.thumbnail((resize, resize))

    # Reduce to palette
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=1)

    # Find dominant colors
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]
    dominant_color = palette[palette_index*3:palette_index*3+3]
    

    return tuple(dominant_color)
    
def url_to_image(url):
    fd = urlopen(url)
    f = io.BytesIO(fd.read())
    
    return f

def color_from_image(url):
    image = url_to_image(url)
    color = extract_color(image)
    
    return '#%02x%02x%02x' % color

    
    