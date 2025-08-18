import pydantic
import typing
import typing_extensions


class DocumentHash(pydantic.BaseModel):
    """
    DocumentHash
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hash: typing.Optional[str] = pydantic.Field(alias="hash", default=None)
    hash_algorithm: typing.Optional[typing_extensions.Literal["SHA256"]] = (
        pydantic.Field(alias="hashAlgorithm", default=None)
    )
