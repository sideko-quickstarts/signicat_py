import pydantic
import typing_extensions


class IdentityProvider(typing_extensions.TypedDict):
    """
    IdentityProvider
    """

    idp_name: typing_extensions.Required[str]


class _SerializerIdentityProvider(pydantic.BaseModel):
    """
    Serializer for IdentityProvider handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    idp_name: str = pydantic.Field(
        alias="idpName",
    )
