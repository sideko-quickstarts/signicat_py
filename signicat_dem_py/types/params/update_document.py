import pydantic
import typing
import typing_extensions

from .document_hash import DocumentHash, _SerializerDocumentHash


class UpdateDocument(typing_extensions.TypedDict):
    """
    UpdateDocument
    """

    created_at: typing_extensions.NotRequired[str]

    description: typing_extensions.NotRequired[str]
    """
    A description of the document for display purposes. Optional metadata about the stored document which the customer can supply.
    """

    document_hash: typing_extensions.NotRequired[DocumentHash]

    filename: typing_extensions.NotRequired[str]
    """
    A name to use if the document is to be stored as a file. Optional metadata about the stored document which the customer can supply.
    """

    mime_type: typing_extensions.NotRequired[str]

    title: typing_extensions.NotRequired[str]
    """
    A title of the document for display purposes. Optional metadata about the stored document which the customer can supply.
    """


class _SerializerUpdateDocument(pydantic.BaseModel):
    """
    Serializer for UpdateDocument handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="createdAt", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    document_hash: typing.Optional[_SerializerDocumentHash] = pydantic.Field(
        alias="documentHash", default=None
    )
    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
    mime_type: typing.Optional[str] = pydantic.Field(alias="mimeType", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
