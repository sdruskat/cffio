```yaml hl_lines="22-49"
cff-version: 1.2.0
message: "If you use this software, please cite it using these metadata."
authors:
  - family-names: Druskat
    given-names: Stephan
    orcid: https://orcid.org/1234-5678-9101-1121
title: "ResearchSoftware"
abstract: "A fast, reliable and easy-to-use open source research software."
version: 2.0.4
identifiers:
  - type: doi
    value: 10.5281/zenodo.1234
    description: "Resolves to ResearchSoftware v2.0.4 published on Zenodo"
date-released: 2021-08-11
repository-code: https://git.example.org/research-software
keywords:
  - interdisciplinary research
  - state-of-the-art research
  - research software engineering
  - high performance computing
license: MIT
references:
  - type: software
    title: NumLib
    authors:
      - family-names: Bar
        given-names: Foo
    version: 1.0.3
    repository-artifact: https://pkgs.example.org/project/numlib/1.0.3
  - type: software
    title: dataframer
    authors:
      - name: The dataframer 2.4.13 authors
    version: 2.4.13
    identifiers:
      - type: doi
        value: 10.1234/openaccessrepository.1234567
  - type: software
    title: Security Checker
    authors:
      - family-names: Eggs
        given-names: Spa M.
      - family-names: Ham
        given-names: Real
      - name: SecOps Working Group
    version: 0.16.8.rc2
    identifiers:
      - type: swh
        value: swh:1:dir:4ef2302827801964c4211929149278ec52f52808
```