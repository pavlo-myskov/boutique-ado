from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    AppConfig for the checkout app.

    This class defines the configuration for the checkout app,
    including the default auto field and the name of the app.
    It also imports the signals module to ensure that
    the signals are registered when the app is ready.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "checkout"

    def ready(self) -> None:
        import checkout.signals  # noqa
