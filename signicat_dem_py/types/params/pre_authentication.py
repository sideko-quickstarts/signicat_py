import pydantic
import typing_extensions


class PreAuthentication(typing_extensions.TypedDict):
    """
    PreAuthentication
    """

    enabled: typing_extensions.Required[bool]


class _SerializerPreAuthentication(pydantic.BaseModel):
    """
    Serializer for PreAuthentication handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
