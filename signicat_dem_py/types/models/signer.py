import pydantic
import typing
import typing_extensions


class Signer(pydantic.BaseModel):
    """
    Signer
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
