"""Coinbase Platform API

This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

The version of the OpenAPI document: 0.0.1-alpha
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class PayloadSignature(BaseModel):
    """A payload signed by an address."""

    payload_signature_id: StrictStr = Field(description="The ID of the payload signature.")
    wallet_id: StrictStr = Field(description="The ID of the wallet that owns the address.")
    address_id: StrictStr = Field(description="The onchain address of the signer.")
    unsigned_payload: StrictStr = Field(
        description="The unsigned payload. This is the payload that needs to be signed by the signer address."
    )
    signature: StrictStr | None = Field(default=None, description="The signature of the payload.")
    status: StrictStr = Field(description="The status of the payload signature.")
    __properties: ClassVar[list[str]] = [
        "payload_signature_id",
        "wallet_id",
        "address_id",
        "unsigned_payload",
        "signature",
        "status",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["pending", "signed", "failed"]):
            raise ValueError("must be one of enum values ('pending', 'signed', 'failed')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of PayloadSignature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of PayloadSignature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "payload_signature_id": obj.get("payload_signature_id"),
                "wallet_id": obj.get("wallet_id"),
                "address_id": obj.get("address_id"),
                "unsigned_payload": obj.get("unsigned_payload"),
                "signature": obj.get("signature"),
                "status": obj.get("status"),
            }
        )
        return _obj
