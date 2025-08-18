import pydantic
import typing


class DocumentReference(pydantic.BaseModel):
    """
    DocumentReference
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    document_id: str = pydantic.Field(
        alias="documentId",
    )
    """
    The document ID
    """
