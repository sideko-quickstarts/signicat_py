import pydantic
import typing
import typing_extensions


class Signer(typing_extensions.TypedDict):
    """
    Signer
    """

    email: typing_extensions.NotRequired[str]

    mobile: typing_extensions.NotRequired[str]

    national_identification_number: typing_extensions.NotRequired[str]

    validations: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["NATIONAL_IDENTIFICATION_NUMBER"]]
    ]


class _SerializerSigner(pydantic.BaseModel):
    """
    Serializer for Signer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    mobile: typing.Optional[str] = pydantic.Field(alias="mobile", default=None)
    national_identification_number: typing.Optional[str] = pydantic.Field(
        alias="nationalIdentificationNumber", default=None
    )
    validations: typing.Optional[
        typing.List[typing_extensions.Literal["NATIONAL_IDENTIFICATION_NUMBER"]]
    ] = pydantic.Field(alias="validations", default=None)
