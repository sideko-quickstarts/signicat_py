import httpx
import typing

from make_api_request import AsyncBaseClient, AuthBearer, SyncBaseClient
from signicat_dem_py.environment import DEFAULT, Environment, ServerGroup, _get_base_url
from signicat_dem_py.resources.dem import AsyncDemClient, DemClient
from signicat_dem_py.resources.sign import AsyncSignClient, SignClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        environment: ServerGroup = DEFAULT,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url={
                "dem": _get_base_url(environment, "dem", Environment.DEM.value),
                "sign": _get_base_url(environment, "sign", Environment.SIGN.value),
            },
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
            auths={"bearerAuth": AuthBearer(token=token)},
        )
        self.sign = SignClient(base_client=self._base_client)
        self.dem = DemClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        environment: ServerGroup = DEFAULT,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url={
                "dem": _get_base_url(environment, "dem", Environment.DEM.value),
                "sign": _get_base_url(environment, "sign", Environment.SIGN.value),
            },
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
            auths={"bearerAuth": AuthBearer(token=token)},
        )
        self.sign = AsyncSignClient(base_client=self._base_client)
        self.dem = AsyncDemClient(base_client=self._base_client)
