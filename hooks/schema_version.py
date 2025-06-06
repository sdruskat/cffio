import json
import urllib.request, json 

def retrieve_schema_version_from_main():
    with urllib.request.urlopen("https://raw.githubusercontent.com/citation-file-format/citation-file-format/refs/heads/main/schema.json") as url:
        data = json.load(url)
    print(data)
    return "Einszweinull!"

def on_config(config, **kwargs):
    config.extra.schema_version = retrieve_schema_version_from_main()
