import pydantic
import typing
import typing_extensions


class SessionSignature(typing_extensions.TypedDict):
    """
    SessionSignature
    """

    document_collection_id: typing_extensions.NotRequired[str]

    original_document_id: typing_extensions.NotRequired[str]

    result_document_id: typing_extensions.Required[str]

    signature_type: typing_extensions.Required[
        typing_extensions.Literal["PADES", "XADES"]
    ]


class _SerializerSessionSignature(pydantic.BaseModel):
    """
    Serializer for SessionSignature handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
