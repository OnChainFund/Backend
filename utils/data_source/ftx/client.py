import time
import urllib.parse
from typing import Optional, Dict, Any, List

from requests import Request, Session, Response
import hmac
from ciso8601 import parse_datetime


class FtxClient:
    _ENDPOINT = "https://ftx.com/api/"

    def __init__(self) -> None:
        self._session = Session()

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        request = Request(method, self._ENDPOINT + path, **kwargs)
        response = self._session.send(request.prepare())
        return self._process_response(response)

    def _process_response(self, response: Response) -> Any:
        try:
            data = response.json()
        except ValueError:
            response.raise_for_status()
            raise
        else:
            if not data["success"]:
                raise Exception(data["error"])
            return data["result"]

    def get_markets(self) -> List[dict]:
        return self._get("markets")

    def get_market_data(self, market_name: str) -> List[dict]:
        return self._get(f"/markets/{market_name}")

    def get_price(self, market_name: str) -> List[dict]:
        return self.get_market_data(market_name)["price"]
