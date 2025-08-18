import pydantic
import typing_extensions


class RedirectSettings(typing_extensions.TypedDict):
    """
    RedirectSettings
    """

    cancel: typing_extensions.Required[str]

    error: typing_extensions.Required[str]

    success: typing_extensions.Required[str]


class _SerializerRedirectSettings(pydantic.BaseModel):
    """
    Serializer for RedirectSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cancel: str = pydantic.Field(
        alias="cancel",
    )
    error: str = pydantic.Field(
        alias="error",
    )
    success: str = pydantic.Field(
        alias="success",
    )
