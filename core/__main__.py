import uvicorn

from core.gunicorn_runner import GunicornApplication
from core.settings import get_settings


def main() -> None:
    """Entrypoint of the application."""
    settings = get_settings()
    if settings.RELOAD:
        uvicorn.run(
            "core.application:get_app",
            workers=settings.WORKERS,
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.RELOAD,
            factory=True,
        )
    else:
        GunicornApplication(
            "core.application:get_app",
            host=settings.HOST,
            port=settings.PORT,
            workers=settings.WORKERS,
            factory=True,
            accesslog="-",
            access_log_format='%r "-" %s "-" %Tf',  # noqa: WPS323
        ).run()


if __name__ == "__main__":
    main()
