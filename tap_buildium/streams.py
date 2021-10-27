"""Stream type classes for tap-buildium."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_buildium.client import BuildiumStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class UnitsStream(BuildiumStream):
    """Define custom stream."""
    name = "units"
    path = "/rentals/units"
    primary_keys = ["Id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "Id",
            th.IntegerType,
            description=""
        ),
        th.Property(
            "PropertyId",
            th.IntegerType,
            description=""
        ),
        th.Property(
            "BuildingName",
            th.StringType,
            description=""
        ),
        th.Property("UnitNumber", th.StringType),
        th.Property("Description", th.StringType),
        th.Property("MarketRent", th.IntegerType),
        th.Property("Address", 
            th.ObjectType(
                th.Property("AddressLine1", th.StringType),
                th.Property("AddressLine2", th.StringType),
                th.Property("AddressLine3", th.StringType),
                th.Property("City", th.StringType),
                th.Property("State", th.StringType),
                th.Property("PostalCode", th.StringType),
                th.Property("Country", th.StringType)
            )
        ),
        th.Property("UnitBedrooms", th.StringType),
        th.Property("UnitBathrooms", th.StringType),
        th.Property("UnitSize", th.IntegerType),
        th.Property("IsUnitLIsted", th.BooleanType),
        th.Property("IsUnitOccupied", th.BooleanType)
    ).to_dict()

# test out a different way to define schema
class TenantsStream(BuildiumStream):
    """Define custom stream."""
    name = "tenants"
    path = "/leases/tenants"
    primary_keys = ["Id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "tenants.json"