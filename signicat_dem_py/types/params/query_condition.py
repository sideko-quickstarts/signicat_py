import pydantic
import typing
import typing_extensions


class QueryCondition(typing_extensions.TypedDict):
    """
    Object describing a condition for a search. <br> It consists of three fields:
    """

    field: typing_extensions.Required[str]

    operator: typing_extensions.Required[str]

    value: typing_extensions.Required[typing.Any]


class _SerializerQueryCondition(pydantic.BaseModel):
    """
    Serializer for QueryCondition handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    field: str = pydantic.Field(
        alias="field",
    )
    operator: str = pydantic.Field(
        alias="operator",
    )
    value: typing.Any = pydantic.Field(
        alias="value",
    )
