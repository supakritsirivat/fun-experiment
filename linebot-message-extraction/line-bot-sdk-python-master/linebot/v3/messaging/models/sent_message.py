# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic.v1 import BaseModel, Field, StrictStr

class SentMessage(BaseModel):
    """
    SentMessage
    """
    id: StrictStr = Field(..., description="ID of the sent message.")
    quote_token: Optional[StrictStr] = Field(None, alias="quoteToken", description="Quote token of the message. Only included when a message object that can be specified as a quote target was sent as a push or reply message. ")

    __properties = ["id", "quoteToken"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SentMessage:
        """Create an instance of SentMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SentMessage:
        """Create an instance of SentMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SentMessage.parse_obj(obj)

        _obj = SentMessage.parse_obj({
            "id": obj.get("id"),
            "quote_token": obj.get("quoteToken")
        })
        return _obj

