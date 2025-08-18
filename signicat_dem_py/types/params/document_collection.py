import pydantic
import typing
import typing_extensions

from .collection_output import CollectionOutput, _SerializerCollectionOutput
from .document_reference import DocumentReference, _SerializerDocumentReference


class DocumentCollection(typing_extensions.TypedDict):
    """
    DocumentCollection
    """

    documents: typing_extensions.Required[typing.List[DocumentReference]]

    id: typing_extensions.NotRequired[str]
    """
    The unique ID of the document collection.
    """

    output: typing_extensions.NotRequired[CollectionOutput]

    package_to: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["PADES_CONTAINER"]]
    ]
    """
    A list of formats the collection should be packaged to when all sessions connected to it are signed.
    """


class _SerializerDocumentCollection(pydantic.BaseModel):
    """
    Serializer for DocumentCollection handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    documents: typing.List[_SerializerDocumentReference] = pydantic.Field(
        alias="documents",
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    output: typing.Optional[_SerializerCollectionOutput] = pydantic.Field(
        alias="output", default=None
    )
    package_to: typing.Optional[
        typing.List[typing_extensions.Literal["PADES_CONTAINER"]]
    ] = pydantic.Field(alias="packageTo", default=None)
