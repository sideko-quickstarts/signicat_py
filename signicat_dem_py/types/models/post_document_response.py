import pydantic
import typing

from .document_hash import DocumentHash


class PostDocumentResponse(pydantic.BaseModel):
    """
    PostDocumentResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="createdAt", default=None)
    """
    The date and time when the document was uploaded.
    """
    document_hash: typing.Optional[DocumentHash] = pydantic.Field(
        alias="documentHash", default=None
    )
    document_id: typing.Optional[str] = pydantic.Field(alias="documentId", default=None)
    """
    A unique reference to the uploaded document.
    """
    mime_type: typing.Optional[str] = pydantic.Field(alias="mimeType", default=None)
    """
    The MIME type of the uploaded document. Supported types are text/plain and application/pdf.
    """
