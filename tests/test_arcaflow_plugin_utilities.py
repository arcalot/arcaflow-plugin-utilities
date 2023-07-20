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
            utilities_plugin.ErrorOutput(exit_code=1, error="This is an error")
        )

    def test_functional(self):

        input = utilities_plugin.InputParams()
        output_id, output_data = utilities_plugin.generate_uuid(input)

        # The example plugin always returns an error:
        self.assertEqual("success", output_id)
        self.assertIsNotNone(output_data.uuid)


if __name__ == "__main__":
    unittest.main()
