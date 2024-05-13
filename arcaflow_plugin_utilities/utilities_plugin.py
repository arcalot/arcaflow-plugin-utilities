#!/usr/bin/env python3

import sys
import uuid
from datetime import datetime, timezone
from time import time,sleep
import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import plugin, schema


@dataclass
class InputParams:
    """For steps that do not require input"""


@dataclass
class WaitInput:
    wait_time_ms: typing.Annotated[
        int,
        schema.name("Wait time"),
        schema.description("How long to wait in milliseconds"),
    ]


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
class SuccessOutputWait:
    waited_ms: typing.Annotated[
        float,
        schema.name("waited"),
        schema.description("Confirmation of milliseconds waited"),
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
    timestamp = datetime.now(timezone.utc).astimezone().isoformat()
    return "success", SuccessOutputTimestamp(str(timestamp))


@plugin.step(
    id="wait",
    name="Wait",
    description=("Wait for specified milliseconds"),
    outputs={"success": SuccessOutputWait, "error": ErrorOutput},
)
def wait(
    params: WaitInput,
) -> typing.Tuple[str, typing.Union[SuccessOutputWait, ErrorOutput]]:
    start = time()
    sleep(params.wait_time_ms / 1000)
    end = time()
    return "success", SuccessOutputWait((end - start) * 1000)


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                generate_uuid,
                generate_timestamp,
                wait,
            )
        )
    )
