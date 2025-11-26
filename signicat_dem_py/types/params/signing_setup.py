import pydantic
import typing
import typing_extensions

from .identity_provider import IdentityProvider, _SerializerIdentityProvider


class SigningSetup(typing_extensions.TypedDict):
    """
    What IdPs are available to the end-user and what type of signing flow should take place.
    """

    additional_parameters: typing_extensions.NotRequired[
        typing.Optional[typing.Dict[str, str]]
    ]
    """
    Additional parameters that modify the authentication flow. Depends on selected IdP. See <a href="https://developer.signicat.com/identity-methods/">developer documentation</a> for details.
    
    """

    identity_providers: typing_extensions.Required[typing.List[IdentityProvider]]

    signing_flow: typing_extensions.Required[
        typing_extensions.Literal["AUTHENTICATION_BASED", "PKISIGNING"]
    ]

    vendor: typing_extensions.NotRequired[
        typing_extensions.Literal["AUDKENNI", "BUYPASS", "SBID"]
    ]


class _SerializerSigningSetup(pydantic.BaseModel):
    """
    Serializer for SigningSetup handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_parameters: typing.Optional[typing.Dict[str, str]] = pydantic.Field(
        alias="additionalParameters", default=None
    )
    identity_providers: typing.List[_SerializerIdentityProvider] = pydantic.Field(
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
