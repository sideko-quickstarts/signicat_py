import pydantic
import typing_extensions


class SessionDocument(typing_extensions.TypedDict):
    """
    SessionDocument
    """

    action: typing_extensions.Required[typing_extensions.Literal["SIGN", "VIEW"]]

    document_collection_id: typing_extensions.Required[str]

    document_id: typing_extensions.Required[str]


class _SerializerSessionDocument(pydantic.BaseModel):
    """
    Serializer for SessionDocument handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    action: typing_extensions.Literal["SIGN", "VIEW"] = pydantic.Field(
        alias="action",
    )
    document_collection_id: str = pydantic.Field(
        alias="documentCollectionId",
    )
    document_id: str = pydantic.Field(
        alias="documentId",
    )
