"""
Gets all versions of CFF published on Zenodo,
then gets all citations of each version from OpenAlex.
"""
import time

import requests
import json

def retrieve_cff_dois(repeat: bool = False):
    dois = ["10.5281/zenodo.1003149"]
    r = requests.get("https://zenodo.org/api/records/1003149")
    if r.status_code == 200:
        data = r.json()
        versions_api_url = data["links"]["versions"]
        r_versions = requests.get(versions_api_url)
        if r_versions.status_code == 200:
            data_versions = r_versions.json()
            for version in data_versions["hits"]["hits"]:
                dois.append(version["doi"])
    else:
        if not repeat:
            time.sleep(5)
            retrieve_cff_dois(True)
    return dois

if __name__ == '__main__':
    cff_dois = retrieve_cff_dois()
    print(cff_dois)
