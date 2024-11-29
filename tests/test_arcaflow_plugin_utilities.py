#!/usr/bin/env python3
import unittest
import arcaflow_plugin_utilities
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            arcaflow_plugin_utilities.SuccessOutputUUID("ABCD-EFGH-IJKL")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_utilities.SuccessOutputTimestamp(
                "2023-11-20T18:34:59.784498Z"
            )
        )

        plugin.test_object_serialization(
            arcaflow_plugin_utilities.SuccessOutputWait(1.234)
        )

        plugin.test_object_serialization(
            arcaflow_plugin_utilities.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        input = arcaflow_plugin_utilities.InputParams()
        output_id, output_data = arcaflow_plugin_utilities.generate_uuid(
            params=input, run_id="plugin_ci"
        )

        self.assertEqual("success", output_id)
        self.assertIsNotNone(output_data.uuid)

        output_id, output_data = arcaflow_plugin_utilities.generate_timestamp(
            params=input, run_id="plugin_ci"
        )

        self.assertEqual("success", output_id)
        self.assertIsNotNone(output_data.timestamp)

        test_time = 500

        output_id, output_data = arcaflow_plugin_utilities.wait(
            params=arcaflow_plugin_utilities.WaitInput(wait_time_ms=test_time),
            run_id="plugin_ci",
        )

        self.assertEqual("success", output_id)
        self.assertGreater(output_data.waited_ms, test_time)


if __name__ == "__main__":
    unittest.main()
