"""
This type stub file was generated by pyright.
"""

import os
import ipfshttpclient
from abc import abstractmethod
from pathlib import Path
from typing import Dict, List, Type
from eth_utils import import_string, to_bytes
from ethpm import get_ethpm_spec_dir
from ethpm._utils.ipfs import dummy_ipfs_pin, extract_ipfs_path_from_uri, generate_file_hash, is_ipfs_uri
from ethpm.backends.base import BaseURIBackend
from ethpm.constants import DEFAULT_IPFS_BACKEND, INFURA_GATEWAY_MULTIADDR, IPFS_GATEWAY_PREFIX
from ethpm.exceptions import CannotHandleURI, EthPMValidationError

class BaseIPFSBackend(BaseURIBackend):
    """
    Base class for all URIs with an IPFS scheme.
    """
    def can_resolve_uri(self, uri: str) -> bool:
        """
        Return a bool indicating whether or not this backend
        is capable of serving the content located at the URI.
        """
        ...
    
    def can_translate_uri(self, uri: str) -> bool:
        """
        Return False. IPFS URIs cannot be used to point
        to another content-addressed URI.
        """
        ...
    
    @abstractmethod
    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        """
        Pin assets found at `file_or_dir_path` and return a
        list containing pinned asset data.
        """
        ...
    


class IPFSOverHTTPBackend(BaseIPFSBackend):
    """
    Base class for all IPFS URIs served over an http connection.
    All subclasses must implement: base_uri
    """
    def __init__(self) -> None:
        ...
    
    def fetch_uri_contents(self, uri: str) -> bytes:
        ...
    
    @property
    @abstractmethod
    def base_uri(self) -> str:
        ...
    
    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        ...
    


class IPFSGatewayBackend(IPFSOverHTTPBackend):
    """
    Backend class for all IPFS URIs served over the IPFS gateway.
    """
    @property
    def base_uri(self) -> str:
        ...
    
    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        ...
    
    def fetch_uri_contents(self, uri: str) -> bytes:
        ...
    


class InfuraIPFSBackend(IPFSOverHTTPBackend):
    """
    Backend class for all IPFS URIs served over the Infura IFPS gateway.
    """
    @property
    def base_uri(self) -> str:
        ...
    


class LocalIPFSBackend(IPFSOverHTTPBackend):
    """
    Backend class for all IPFS URIs served through a direct connection to an IPFS node.
    Default IPFS port = 5001
    """
    @property
    def base_uri(self) -> str:
        ...
    


MANIFEST_URIS = ...
class DummyIPFSBackend(BaseIPFSBackend):
    """
    Backend class to serve IPFS URIs without having to make an HTTP request.
    Used primarily for testing purposes, returns a locally stored manifest or contract.
    ---
    `ipfs_uri` can either be:
    - Valid IPFS URI -> safe-math-lib manifest (ALWAYS)
    - Path to manifest/contract in ethpm_spec_dir -> defined manifest/contract
    """
    def fetch_uri_contents(self, ipfs_uri: str) -> bytes:
        ...
    
    def can_resolve_uri(self, uri: str) -> bool:
        ...
    
    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        """
        Return a dict containing the IPFS hash, file name, and size of a file.
        """
        ...
    


def get_ipfs_backend(import_path: str = ...) -> BaseIPFSBackend:
    """
    Return the `BaseIPFSBackend` class specified by import_path, default, or env variable.
    """
    ...

def get_ipfs_backend_class(import_path: str = ...) -> Type[BaseIPFSBackend]:
    ...
