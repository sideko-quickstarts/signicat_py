import pydantic


class RedirectSettings(pydantic.BaseModel):
    """
    RedirectSettings
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancel: str = pydantic.Field(
        alias="cancel",
    )
    error: str = pydantic.Field(
        alias="error",
    )
    success: str = pydantic.Field(
        alias="success",
    )
