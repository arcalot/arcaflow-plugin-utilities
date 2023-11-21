#!/usr/bin/env python3

import sys
import uuid
import datetime
import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import plugin, schema


@dataclass
class InputParams:
    """
    This is the data structure for the input parameters of the uuid plugin.
    """


@dataclass
class SuccessOutputUUID:
    uuid: typing.Annotated[
        str,
        schema.name("UUID"),
        schema.description("A randomly generated UUID"),
    ]


@dataclass
class SuccessOutputTimestamp:
    timestamp: typing.Annotated[
        str,
        schema.name("timestamp"),
        schema.description("An ISO 8601 timestamp with millisecond precision"),
    ]


@dataclass
class ErrorOutput:
    error: typing.Annotated[
        str,
        schema.name("Failure Error"),
        schema.description("Reason for failure"),
    ]


@plugin.step(
    id="uuid",
    name="Generate UUID",
    description="Generates a random UUID which can be used for tracking uniqueness",
    outputs={"success": SuccessOutputUUID, "error": ErrorOutput},
)
def generate_uuid(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutputUUID, ErrorOutput]]:
    new_uuid = uuid.uuid4()
    return "success", SuccessOutputUUID(str(new_uuid))


@plugin.step(
    id="timestamp",
    name="Generate timestamp",
    description=(
        "Generates a random timestamp in ISO 8601 format with millisecond accuracy"
    ),
    outputs={"success": SuccessOutputTimestamp, "error": ErrorOutput},
)
def generate_timestamp(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutputTimestamp, ErrorOutput]]:
    timestamp = datetime.datetime.now().isoformat()
    return "success", SuccessOutputTimestamp(str(timestamp))


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                generate_uuid,
                generate_timestamp,
            )
        )
    )
