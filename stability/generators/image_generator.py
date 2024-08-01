import requests
from django.conf import settings
from stability.models import GeneratedImage
from django.core.files.base import ContentFile


class ImageGenerator:
    def generate(
        self,
        prompt: str,
    ):
        response = requests.post(
            settings.URL,
            headers={
                "authorization": f"Bearer " + settings.TOKEN,
                "accept": "image/*",
            },
            files={"none": ""},
            data={
                "prompt": prompt,
                "output_format": "jpeg",
            },
        )

        if response.status_code == 200:
            generated_image = GeneratedImage(prompt=prompt)
            image_name = prompt.replace(" ", "")
            generated_image.image_url.save(
                image_name + (".jpeg"), ContentFile(response.content), save=True
            )
        else:
            raise Exception(str(response.json()))
