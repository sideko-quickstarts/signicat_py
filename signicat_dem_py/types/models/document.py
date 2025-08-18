import pydantic
import typing

from .document_hash import DocumentHash


class Document(pydantic.BaseModel):
    """
    Document
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="createdAt", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    A description of the document for display purposes. Optional metadata about the stored document which the customer can supply.
    """
    document_hash: typing.Optional[DocumentHash] = pydantic.Field(
        alias="documentHash", default=None
    )
    document_id: typing.Optional[str] = pydantic.Field(alias="documentId", default=None)
    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
    """
    A name to use if the document is to be stored as a file. Optional metadata about the stored document which the customer can supply.
    """
    mime_type: typing.Optional[str] = pydantic.Field(alias="mimeType", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    """
    A title of the document for display purposes. Optional metadata about the stored document which the customer can supply.
    """
