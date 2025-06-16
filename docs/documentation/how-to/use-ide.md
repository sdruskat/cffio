!!! warning
    Draft incomplete

# Create, edit, validate `CITATION.cff` files in your IDE

These how-tos show how to set up support for the Citation File Format in your IDE.

This generally works as follows:

- The Citation File Format has defined a JSON schema, which can also be used for YAML files.
- 

## Visual Studio Code (VSCode)

1. Install a plugin that supports using JSON Schemas to edit YAML, e.g., the [YAML language support plugin by RedHat](https://marketplace.visualstudio.com/items/?itemName=redhat.vscode-yaml).
2. Create a new file.
3. Set the Language Mode to `YAML` (`^` + `K` + `M`, or `^` + `Shift` + `P` and start typing `language`).
4. In the status bar of VSCode at the bottom of the screen, open the selection of the JSON Schema by clicking on `No JSON Schema`.
5. Select `Citation File Format`.
6. You can now use code completion (CTRL + Space) to populate the required fields, select valid values, browser through fields, etc.
