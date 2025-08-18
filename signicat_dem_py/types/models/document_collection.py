import pydantic
import typing
import typing_extensions

from .collection_output import CollectionOutput
from .document_reference import DocumentReference


class DocumentCollection(pydantic.BaseModel):
    """
    DocumentCollection
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    documents: typing.List[DocumentReference] = pydantic.Field(
        alias="documents",
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    The unique ID of the document collection.
    """
    output: typing.Optional[CollectionOutput] = pydantic.Field(
        alias="output", default=None
    )
    package_to: typing.Optional[
        typing.List[typing_extensions.Literal["PADES_CONTAINER"]]
    ] = pydantic.Field(alias="packageTo", default=None)
    """
    A list of formats the collection should be packaged to when all sessions connected to it are signed.
    """
