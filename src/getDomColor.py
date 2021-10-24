from colorthief import ColorThief
from urllib.request import urlopen
import io
    
def getColor(url):
    
    fd = urlopen(url)
    f = io.BytesIO(fd.read())
    
    color_thief = ColorThief(f)
    color = color_thief.get_color(quality=5)
    
    return '#%02x%02x%02x' % color
