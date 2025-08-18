import pydantic
import typing


class SigningSetupAdditionalParameters(pydantic.BaseModel):
    """
    Additional parameters that modify the authentication flow. Depends on selected IdP. See <a href="https://developer.signicat.com/identity-methods/">developer documentation</a> for details.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, str]
