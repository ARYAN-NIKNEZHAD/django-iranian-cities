from django.core.checks import Error, register
from typing import List, Dict, Any

from iranian_cities.conf import sage_iranian_cities_settings
from iranian_cities.exc import (
    IranianCitiesConfigurationError,
)


@register()
def check_iranian_cities_config(app_configs: Dict[str, Any], **kwargs: Any) -> List[Error]:
    """
    Check the Iranian Cities configuration for the application.

    This function verifies that all required Iranian Cities settings are present and ensure the settings are correct.
    Any errors encountered during these checks are returned.

    Parameters
    ----------
    app_configs : dict
        The application configurations.
    **kwargs
        Additional keyword arguments.

    Returns
    -------
    list of Error
        A list of Error objects representing any configuration errors found.

    Raises
    ------
    IranianCitiesConfigurationError
        If any required Iranian Cities configuration settings are missing.

    Examples
    --------
    >>> errors = check_iranian_cities_config(app_configs)
    >>> if errors:
    ...     for error in errors:
    ...         print(error)
    """
    errors: List[Error] = []

    def get_iranian_cities_settings() -> Dict[str, Any]:
        return {
            "ADMIN_CAN_ADD": sage_iranian_cities_settings.ADMIN_CAN_ADD,
            "ADMIN_CAN_DELETE": sage_iranian_cities_settings.ADMIN_CAN_DELETE,
            "ADMIN_CAN_CHANGE": sage_iranian_cities_settings.ADMIN_CAN_CHANGE,
        }


    def check_missing_configs(settings: Dict[str, Any]) -> None:
        missing: List[str] = [key for key, value in settings.items() if not value]
        if missing:
            raise IranianCitiesConfigurationError(
                f"Iranian Cities configuration settings are missing: {', '.join(missing)}."
            )

    try:
        iranian_cities_settings_dict: Dict[str, Any] = get_iranian_cities_settings()
        check_missing_configs(iranian_cities_settings_dict)
    except IranianCitiesConfigurationError as e:
        id = "sage_integration.E004"
        error_message = str(e)
        errors.append(
            Error(
                error_message,
                id=id,
            )
        )
    
    return errors
