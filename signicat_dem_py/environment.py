import enum
import typing
import typing_extensions


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    DEM = "https://api.signicat.com/dem"
    SIGN = "https://api.signicat.com/sign"
    SIGNICAT_DEM_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/signicat-dem/0.1.0"
    )
    SIGNICAT_SIGN_MOCK_SERVER = (
        "https://api.sideko.dev/v1/mock/public/signicat-sign/0.1.0"
    )


class ServerGroup(typing_extensions.TypedDict):
    """Pre-defined set of base URLs for the APIs serviced by this SDK"""

    dem: typing_extensions.NotRequired[typing.Union[Environment, str]]
    sign: typing_extensions.NotRequired[typing.Union[Environment, str]]


DEFAULT: ServerGroup = {"dem": Environment.DEM.value, "sign": Environment.SIGN.value}

SIDEKO_MOCK_SERVER: ServerGroup = {
    "dem": Environment.SIGNICAT_DEM_MOCK_SERVER.value,
    "sign": Environment.SIGNICAT_SIGN_MOCK_SERVER.value,
}


def _get_base_url(
    server_group: ServerGroup,
    api: typing.Literal["dem", "sign"],
    default: typing.Union[Environment, str],
) -> str:
    env_or_str = server_group.get(api, default)
    if isinstance(env_or_str, Environment):
        return env_or_str.value
    else:
        return str(env_or_str)
