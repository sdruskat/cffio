```yaml hl_lines="15-38"
cff-version: 1.2.0
message: "If you use this software, please cite it using these metadata."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/1234-5678-9101-1121
title: "ResearchSoftware"
version: 2.0.4
identifiers:
  - type: doi
    value: 10.5281/zenodo.1234
    description: "Resolves to ResearchSoftware v2.0.4 published on Zenodo"
date-released: 2021-08-11
repository-code: https://git.example.org/research-software
references:
  - type: software
    title: Data Processing Library
    authors:
      - family-names: Bar
        given-names: Foo
      - name: The Data Processing Library Community
    version: 1.0.3
    identifiers:
      - type: doi
        value: 10.5281/zenodo.5678
  - type: software
    title: The GUI Framework
    authors:
      - family-names: Baz
        given-names: Spam
        orcid: https://orcid.org/1234-5678-9101-1122
      - family-names: Eggs
        given-names: Kim
        orcid: https://orcid.org/1234-5678-9101-1123
    version: 2025-09
    identifiers:
      - type: swh
        value: swh:1:dir:4ef2302827801964c4211929149278ec52f52800
```