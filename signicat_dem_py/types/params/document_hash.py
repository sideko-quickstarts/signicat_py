import pydantic
import typing
import typing_extensions


class DocumentHash(typing_extensions.TypedDict):
    """
    DocumentHash
    """

    hash: typing_extensions.NotRequired[str]

    hash_algorithm: typing_extensions.NotRequired[typing_extensions.Literal["SHA256"]]


class _SerializerDocumentHash(pydantic.BaseModel):
    """
    Serializer for DocumentHash handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    hash: typing.Optional[str] = pydantic.Field(alias="hash", default=None)
    hash_algorithm: typing.Optional[typing_extensions.Literal["SHA256"]] = (
        pydantic.Field(alias="hashAlgorithm", default=None)
    )
