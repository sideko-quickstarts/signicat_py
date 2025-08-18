import pydantic
import typing
import typing_extensions


class DocumentReference(typing_extensions.TypedDict):
    """
    DocumentReference
    """

    description: typing_extensions.NotRequired[str]

    document_id: typing_extensions.Required[str]
    """
    The document ID
    """


class _SerializerDocumentReference(pydantic.BaseModel):
    """
    Serializer for DocumentReference handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    document_id: str = pydantic.Field(
        alias="documentId",
    )
