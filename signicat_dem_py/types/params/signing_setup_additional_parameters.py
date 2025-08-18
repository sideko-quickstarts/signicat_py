import pydantic
import typing
import typing_extensions


class SigningSetupAdditionalParameters(typing_extensions.TypedDict, total=False):
    """
    Additional parameters that modify the authentication flow. Depends on selected IdP. See <a href="https://developer.signicat.com/identity-methods/">developer documentation</a> for details.

    """


class _SerializerSigningSetupAdditionalParameters(pydantic.BaseModel):
    """
    Serializer for SigningSetupAdditionalParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
