import pydantic
import typing
import typing_extensions


class SessionLifecycle(typing_extensions.TypedDict):
    """
    Contains session lifecycle metadata.
    """

    state: typing_extensions.NotRequired[
        typing_extensions.Literal["BLOCKED", "READY", "REJECTED", "SIGNED"]
    ]

    state_is_final: typing_extensions.NotRequired[bool]


class _SerializerSessionLifecycle(pydantic.BaseModel):
    """
    Serializer for SessionLifecycle handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    state: typing.Optional[
        typing_extensions.Literal["BLOCKED", "READY", "REJECTED", "SIGNED"]
    ] = pydantic.Field(alias="state", default=None)
    state_is_final: typing.Optional[bool] = pydantic.Field(
        alias="stateIsFinal", default=None
    )
