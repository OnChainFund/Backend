"""
This type stub file was generated by pyright.
"""

from functools import lru_cache
from typing import List, Optional
from .constant import COMMON_SAFE_ASCII_CHARACTERS, UNICODE_SECONDARY_RANGE_KEYWORD
from .utils import is_accentuated, is_ascii, is_case_variable, is_cjk, is_emoticon, is_hangul, is_hiragana, is_katakana, is_latin, is_punctuation, is_separator, is_symbol, is_thai, is_unprintable, remove_accent, unicode_range

class MessDetectorPlugin:
    """
    Base abstract class used for mess detection plugins.
    All detectors MUST extend and implement given methods.
    """
    def eligible(self, character: str) -> bool:
        """
        Determine if given character should be fed in.
        """
        ...
    
    def feed(self, character: str) -> None:
        """
        The main routine to be executed upon character.
        Insert the logic in witch the text would be considered chaotic.
        """
        ...
    
    def reset(self) -> None:
        """
        Permit to reset the plugin to the initial state.
        """
        ...
    
    @property
    def ratio(self) -> float:
        """
        Compute the chaos ratio based on what your feed() has seen.
        Must NOT be lower than 0.; No restriction gt 0.
        """
        ...
    


class TooManySymbolOrPunctuationPlugin(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class TooManyAccentuatedPlugin(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class UnprintablePlugin(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class SuspiciousDuplicateAccentPlugin(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class SuspiciousRange(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class SuperWeirdWordPlugin(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class CjkInvalidStopPlugin(MessDetectorPlugin):
    """
    GB(Chinese) based encoding often render the stop incorrectly when the content does not fit and
    can be easily detected. Searching for the overuse of '丅' and '丄'.
    """
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


class ArchaicUpperLowerPlugin(MessDetectorPlugin):
    def __init__(self) -> None:
        ...
    
    def eligible(self, character: str) -> bool:
        ...
    
    def feed(self, character: str) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    @property
    def ratio(self) -> float:
        ...
    


@lru_cache(maxsize=1024)
def is_suspiciously_successive_range(unicode_range_a: Optional[str], unicode_range_b: Optional[str]) -> bool:
    """
    Determine if two Unicode range seen next to each other can be considered as suspicious.
    """
    ...

@lru_cache(maxsize=2048)
def mess_ratio(decoded_sequence: str, maximum_threshold: float = ..., debug: bool = ...) -> float:
    """
    Compute a mess ratio given a decoded bytes sequence. The maximum threshold does stop the computation earlier.
    """
    ...

