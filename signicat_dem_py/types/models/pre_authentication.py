import pydantic


class PreAuthentication(pydantic.BaseModel):
    """
    PreAuthentication
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
