import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    # Application
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 1
    RELOAD: bool = True
    ENVIRONMENT: str = "dev"
    API_PREFIX: str = "/api/v1"

    # Database
    DB_HOST: str = "213.171.28.212"
    DB_PORT: int = 15432
    DB_USER: str = "notAdmin3287111"
    DB_PASS: str = "KamxnJAnmxiiiiUIUUU"
    DB_BASE: str = "hackaton_hackaton"
    DB_ECHO: bool = False

    # RABBITMQ
    RABBIT_HOST: str = "rabbitmq"
    RABBIT_PORT: int = "5672"
    RABBIT_USER: str = "friendly_user"
    RABBIT_PASS: str = "123456Aa"
    RABBIT_VHOST: str = '/'
    rabbit_pool_size: int = 10
    rabbit_channel_pool_size: int = 10


    # Auth
    ACCESS_TOKEN_EXPIRE: int = 5
    REFRESH_TOKEN_EXPIRE: int = 60 * 24 * 30  # 30 days

    # Security
    JWT_SECRET_KEY: str = "1234567890wsdefghjk"

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            password=self.DB_PASS,
            path=f"/{self.DB_BASE}",
        )

    @property
    def db_url_sync(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql",
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            password=self.DB_PASS,
            path=f"/{self.DB_BASE}",
        )

    @property
    def rabbit_url(self) -> URL:
        """
        Assemble RabbitMQ URL from settings.

        :return: rabbit URL.
        """
        return URL.build(
            scheme="amqp",
            host=self.RABBIT_HOST,
            port=self.RABBIT_PORT,
            user=self.RABBIT_USER,
            password=self.RABBIT_PASS,
            # path=self.RABBIT_VHOST,
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


def get_settings():
    return Settings()
