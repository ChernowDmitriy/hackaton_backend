import taskiq_fastapi

from taskiq_aio_pika import AioPikaBroker

from core.settings import get_settings

settings = get_settings()

# TODO: Add the broker to the application environment
broker = AioPikaBroker(
    str(settings.rabbit_url),
)

taskiq_fastapi.init(
    broker,
    "core.application:get_app",
)
