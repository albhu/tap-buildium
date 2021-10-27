"""Buildium tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_buildium.streams import (
    BuildiumStream,
    UnitsStream,
    TenantsStream,
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    UnitsStream,
    TenantsStream,
]


class TapBuildium(Tap):
    """Buildium tap class."""
    name = "tap-buildium"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = {}
    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
