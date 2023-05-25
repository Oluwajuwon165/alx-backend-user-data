#!/usr/bin/env python3
"""
Filtered Logger
"""

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
     ) -> str:
    """
    Replaces occurrences of certain field values in the
    log message with redaction.

    Arguments:
    - fields: a list of strings representing all fields to obfuscate
    0- redaction: a string representing by what the field will be obfuscated
    - message: a string representing the log line
    -line separator: a string representing by which character
    is separating all fields in the log line (message)

    Returns:
    - The obfuscated log message
    """
    pattern = r'(' + '|'.join(fields) + r')=[^;]+'
    return re.sub(pattern, lambda match: redaction if\
match.group(1) in fields else match.group(0), message)
