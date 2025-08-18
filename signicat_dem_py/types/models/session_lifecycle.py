import pydantic
import typing
import typing_extensions


class SessionLifecycle(pydantic.BaseModel):
    """
    Contains session lifecycle metadata.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    state: typing.Optional[
        typing_extensions.Literal["BLOCKED", "READY", "REJECTED", "SIGNED"]
    ] = pydantic.Field(alias="state", default=None)
    state_is_final: typing.Optional[bool] = pydantic.Field(
        alias="stateIsFinal", default=None
    )
