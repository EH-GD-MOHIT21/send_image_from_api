import requests
import PIL
from PIL import Image
import io
def my_image():
    response = requests.get("https://source.unsplash.com/1600x900/?lord,hanuman.png")   #here you can request any img type available on unplash.com
    image_bytes = io.BytesIO(response.content)
    img = PIL.Image.open(image_bytes)
    img.save(fp="mohit.png")
    # img.show()
    return (image_bytes,img)