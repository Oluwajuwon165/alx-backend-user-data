#!/usr/bin/env python3
"""
Filtered Logger
"""

import logging
import re


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.

    This formatter filters specified fields in log records
    and replaces their values with a redaction string.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by filtering specified fields.

        Arguments:
        - record: The log record to be formatted.

        Returns:
        - The formatted log message.
        """
        log_message = super().format(record)
        log_message = self.filter_fields(log_message)
        return log_message

    def filter_fields(self, message):
        """
        Filter specified fields in the log message.

        Arguments:
        - message: The log message to be filtered.

        Returns:
        - The filtered log message.
        """
        for field in self.fields:
            pattern = field + r'=([^;]+)'
            message = re.sub(pattern, field + '=' + self.REDACTION, message)
        return message
