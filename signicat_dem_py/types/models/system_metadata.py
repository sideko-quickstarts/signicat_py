import pydantic
import typing
import typing_extensions


class SystemMetadata(pydantic.BaseModel):
    """
    SystemMetadata
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    audit_level: typing.Optional[
        typing_extensions.Literal["ADVANCED", "QUALIFIED", "SIMPLE"]
    ] = pydantic.Field(alias="auditLevel", default=None)
    created_by: typing.Optional[str] = pydantic.Field(alias="createdBy", default=None)
    created_date: typing.Optional[str] = pydantic.Field(
        alias="createdDate", default=None
    )
    created_date_time: typing.Optional[str] = pydantic.Field(
        alias="createdDateTime", default=None
    )
    expiry_date: typing.Optional[str] = pydantic.Field(alias="expiryDate", default=None)
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
