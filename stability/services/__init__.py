import os
from utils.constants import GENERATORS
from celery import shared_task


@shared_task
def _parallelize(
    data: dict[str, str],
):
    prompt = data.get("prompt", "")
    generator = data.get("generator", "image")

    GENERATORS[generator]().generate(
        prompt=prompt,
    )


class StabilityAiService:

    def generate(
        self,
        data: dict[str, str],
    ):

        if os.environ.get("PARALLELIZE", "1") == "1":
            _parallelize.delay(
                data=data,
            )

        else:
            _parallelize(
                data=data,
            )
