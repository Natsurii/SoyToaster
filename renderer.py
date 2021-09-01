import requests
from PIL import Image
from io import BytesIO

def soyImpose(image_url) -> str:

    splitted_url = "".join(image_url.split("_normal"))
    filename = "".join(splitted_url[35:-4].split("/"))
    location = "temp/" + filename + ".png"
    response = requests.get(splitted_url)
    print("image received.")

    with Image.new("RGB", (500,500)) as image:
        with Image.open("soypoint.png") as soypoint:
            with Image.open(BytesIO(response.content)) as pfp:
                pfp = pfp.resize((500,500), resample=Image.BICUBIC)
                image.paste(pfp, (0,0))
                image.paste(soypoint, (0,0), soypoint)
                print("image pasted.")
        image.save(location, "PNG")
    return location