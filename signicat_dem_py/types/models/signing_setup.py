import pydantic
import typing
import typing_extensions

from .identity_provider import IdentityProvider
from .signing_setup_additional_parameters import SigningSetupAdditionalParameters


class SigningSetup(pydantic.BaseModel):
    """
    What IdPs are available to the end-user and what type of signing flow should take place.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    additional_parameters: typing.Optional[SigningSetupAdditionalParameters] = (
        pydantic.Field(alias="additionalParameters", default=None)
    )
    """
    Additional parameters that modify the authentication flow. Depends on selected IdP. See <a href="https://developer.signicat.com/identity-methods/">developer documentation</a> for details.
    
    """
    identity_providers: typing.List[IdentityProvider] = pydantic.Field(
        alias="identityProviders",
    )
    signing_flow: typing_extensions.Literal["AUTHENTICATION_BASED", "PKISIGNING"] = (
        pydantic.Field(
            alias="signingFlow",
        )
    )
    vendor: typing.Optional[
        typing_extensions.Literal["AUDKENNI", "BUYPASS", "SBID"]
    ] = pydantic.Field(alias="vendor", default=None)
