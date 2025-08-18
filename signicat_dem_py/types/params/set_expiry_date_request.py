import pydantic
import typing_extensions


class SetExpiryDateRequest(typing_extensions.TypedDict):
    """
    Object that controls which fields are allowed in a patch request to change the Time to Live (TTL) of a record.
    """

    ttl: typing_extensions.Required[int]


class _SerializerSetExpiryDateRequest(pydantic.BaseModel):
    """
    Serializer for SetExpiryDateRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ttl: int = pydantic.Field(
        alias="ttl",
    )
