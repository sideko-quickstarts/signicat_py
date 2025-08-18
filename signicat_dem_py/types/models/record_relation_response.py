import pydantic
import typing
import typing_extensions

from .links import Links


class RecordRelationResponse(pydantic.BaseModel):
    """
    RecordRelationResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    links: typing.Optional[Links] = pydantic.Field(alias="_links", default=None)
    relation_id: typing.Optional[str] = pydantic.Field(alias="relationID", default=None)
    type_: typing.Optional[
        typing_extensions.Literal[
            "CONSENT",
            "GDPR",
            "INTERNAL_AUDIT",
            "KYC",
            "LOG_IN",
            "OTHER",
            "SENSITIVE",
            "SIGNATURE",
            "TRANSACTION",
        ]
    ] = pydantic.Field(alias="type", default=None)
