import pydantic


class IdentityProvider(pydantic.BaseModel):
    """
    IdentityProvider
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    idp_name: str = pydantic.Field(
        alias="idpName",
    )
