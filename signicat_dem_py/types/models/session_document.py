import pydantic
import typing_extensions


class SessionDocument(pydantic.BaseModel):
    """
    SessionDocument
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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
