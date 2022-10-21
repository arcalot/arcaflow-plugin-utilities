# Utilities Plugin for Arcaflow

The Utilities plugin is used to store common utility functions used by various plugins/workflows.
Where each step of the plugin corresponds to a different utility functionality. Refer to individual step functions in utilities_plugin.py to see what input is expected for each step.

## To test:

In order to run the [utilities plugin](utilities_plugin.py) run the following steps:

### Containerized
1. Clone this repository
2. Create the container with `docker build -t arca-utilities -f Dockerfile`
3. Run `cat example.yaml | docker run -i arca-utilities -f -` to run the plugin


### Native

1. Clone this repository
2. Create a `venv` in the current directory with `python3 -m venv $(pwd)/venv`
3. Activate the `venv` by running `source venv/bin/activate`
4. Run `pip install poetry`
5. Run `poetry install`
6. Run `./utilities_plugin.py -f example.yaml ` to run the plugin


## Image Building

You can change this plugin's image version tag in
`.github/workflows/carpenter.yaml` by editing the
`IMAGE_TAG` variable, and pushing that change to the
branch designated in that workflow.
