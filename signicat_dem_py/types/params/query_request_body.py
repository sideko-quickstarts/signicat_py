import pydantic
import typing
import typing_extensions

from .query_condition import QueryCondition, _SerializerQueryCondition


class QueryRequestBody(typing_extensions.TypedDict):
    """
    An object containing up to three lists of <code>QueryCondition</code> objects. Each list represents a logic operator used to bind the <code>QueryCondition</code> objects into a statement. <br>The <code>'and'</code> list executes the QueryCondition objects with a logical AND operator, all conditions must be met. <br> The <code>'or'</code> list executes the QueryCondition objects with a logical OR operator, at least one of the conditions must be met. <br> The <code>'not'</code> list is currently not in use, but it will in the future execute the QueryCondition objects with a logical NOR operator.
    """

    and_: typing_extensions.NotRequired[typing.List[QueryCondition]]

    not_: typing_extensions.NotRequired[typing.List[QueryCondition]]

    or_: typing_extensions.NotRequired[typing.List[QueryCondition]]


class _SerializerQueryRequestBody(pydantic.BaseModel):
    """
    Serializer for QueryRequestBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    and_: typing.Optional[typing.List[_SerializerQueryCondition]] = pydantic.Field(
        alias="and", default=None
    )
    not_: typing.Optional[typing.List[_SerializerQueryCondition]] = pydantic.Field(
        alias="not", default=None
    )
    or_: typing.Optional[typing.List[_SerializerQueryCondition]] = pydantic.Field(
        alias="or", default=None
    )
