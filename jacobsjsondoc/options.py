
from typing import List, Callable

from enum import Enum

class RefResolutionMode(Enum):
    USE_REFERENCES_OBJECTS = 0
    RESOLVE_REFERENCES = 1


class ParseOptions:

    def __init__(self):
        self.ref_resolution_mode:RefResolutionMode = RefResolutionMode.USE_REFERENCES_OBJECTS
        self.dollar_id_token:str = "$id"
        self.dollar_ref_token:str = "$ref"

    def has_new_base_uri(self, node):
        if self.dollar_id_token in node:
            if not isinstance(node[self.dollar_id_token], str):
                return False
            if node._pointers.idx in ["properties"]:
                return False
            return True
        return False