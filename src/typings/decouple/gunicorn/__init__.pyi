"""
This type stub file was generated by pyright.
"""

class HaltServer(BaseException):
    def __init__(self, reason, exit_status=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class ConfigError(Exception):
    """ Exception raised on config error """
    ...


class AppImportError(Exception):
    """ Exception raised when loading an application """
    ...

