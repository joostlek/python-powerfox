"""Asynchronous Python client for Powerfox."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin


@dataclass
class Device(DataClassORJSONMixin):
    """Object representing a Device from Powerfox."""

    device_id: str = field(metadata=field_options(alias="DeviceId"))
    name: str | None = field(metadata=field_options(alias="Name"))
    date_added: datetime = field(
        metadata=field_options(
            alias="AccountAssociatedSince",
            deserialize=lambda x: datetime.fromtimestamp(x, tz=UTC),
        )
    )
    main_device: bool = field(metadata=field_options(alias="MainDevice"))
    bidirectional: bool = field(metadata=field_options(alias="Prosumer"))
    division: int = field(metadata=field_options(alias="Division"))


# class Power

# class Heat

# class Water
