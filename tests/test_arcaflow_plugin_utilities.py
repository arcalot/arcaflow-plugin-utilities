#!/usr/bin/env python3
import unittest
import utilities_plugin
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            utilities_plugin.SuccessOutputUUID("ABCD-EFGH-IJKL")
        )

        plugin.test_object_serialization(
            utilities_plugin.SuccessOutputTimestamp("2023-11-20T18:34:59.784498Z")
        )

        plugin.test_object_serialization(utilities_plugin.SuccessOutputWait(1.234))

        plugin.test_object_serialization(
            utilities_plugin.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        input = utilities_plugin.InputParams()
        output_id, output_data = utilities_plugin.generate_uuid(
            params=input, run_id="plugin_ci"
        )

        self.assertEqual("success", output_id)
        self.assertIsNotNone(output_data.uuid)

        output_id, output_data = utilities_plugin.generate_timestamp(
            params=input, run_id="plugin_ci"
        )

        self.assertEqual("success", output_id)
        self.assertIsNotNone(output_data.timestamp)

        test_time = 500

        output_id, output_data = utilities_plugin.wait(
            params=utilities_plugin.WaitInput(wait_time_ms=test_time),
            run_id="plugin_ci",
        )

        self.assertEqual("success", output_id)
        self.assertGreater(output_data.waited_ms, test_time)


if __name__ == "__main__":
    unittest.main()
