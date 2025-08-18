import pydantic
import typing
import typing_extensions


class SessionSignature(pydantic.BaseModel):
    """
    SessionSignature
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    document_collection_id: typing.Optional[str] = pydantic.Field(
        alias="documentCollectionId", default=None
    )
    original_document_id: typing.Optional[str] = pydantic.Field(
        alias="originalDocumentId", default=None
    )
    result_document_id: str = pydantic.Field(
        alias="resultDocumentId",
    )
    signature_type: typing_extensions.Literal["PADES", "XADES"] = pydantic.Field(
        alias="signatureType",
    )
