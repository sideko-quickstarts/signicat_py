import pydantic
import typing


class Link(pydantic.BaseModel):
    """
    Link
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deprecation: typing.Optional[str] = pydantic.Field(
        alias="deprecation", default=None
    )
    href: typing.Optional[str] = pydantic.Field(alias="href", default=None)
    hreflang: typing.Optional[str] = pydantic.Field(alias="hreflang", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    profile: typing.Optional[str] = pydantic.Field(alias="profile", default=None)
    templated: typing.Optional[bool] = pydantic.Field(alias="templated", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
