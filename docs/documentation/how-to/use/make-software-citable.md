!!! success
    Complete.

# How to use the Citation File Format to make your software citable

Making your software citable is one of the most important uses of the
Citation File Format.

The examples below each show the complete contents of a **valid `CITATION.cff` file**.
Any of them will make your software citable, but they differ in the *effort* they take to apply,
and in how *reliable* and *useful* the citation metadata is.

- _If you want to **get started quickly** and with **minimal effort**,
use the [minimal example](#how-to-get-started)._
- _If you care about following **academic standards**,
[include a DOI for your software](#how-to-include-a-doi)
to **identify individual versions** or the whole project._
- _If you care about **granular traceability** of software versions or parts,
[include an SWHID](#how-to-include-a-software-hash-identifier-from-software-heritage)._
- _If you want to enable **different citation use cases**, you can also
[combine multiple identifiers](#how-to-include-multiple-identifiers)._

## How to get started

This example shows you how to create a `CITATION.cff` file 
with the minimal information that is needed to cite your software correctly.

In addition to the technically required fields, it provides information about
the *version* of your software, its *release date* and the
*source code repository*.

{!_assets/snippets/cff-simple-example-repo.md!}

{!_assets/snippets/copy-paste.md!}

## How to include a DOI

This example shows you how to create a `CITATION.cff` file 
with a DOI that reliably identifies a version of your software for citation.

Persistent [*Digital Object Identifiers*](https://en.wikipedia.org/wiki/Digital_object_identifier) (*DOI*s)
are used to uniquely identify various digital research outputs,
including software versions and software projects. 
Many reference management tools can resolve DOIs to retrieve the metadata of the objects they identify,
and automatically create references and bibliographies from them.
These can then be easily used in academic writing.

{!_assets/snippets/cff-simple-example-doi.md!}

{!_assets/snippets/copy-paste.md!}
1. Archive the software version in a repository that assigns a DOI to each published software version.
Many projects use the open access repository [Zenodo](https://zenodo.org) for this.
There, you can also pre-reserve a DOI and add it to your CFF file before publication.
Zenodo also gives you a second "concept" DOI.
This identifies all versions of your software at once.
It can be used to cite your whole software *project*, rather than a specific version.
1. Copy the DOI you want people to use for citation.
1. Add the DOI in the `identifiers` section of your `CITATION.cff` and define its type as `doi`.
{!_assets/snippets/save-file-maintain.md!}

## How to include a SoftWare Hash IDentifier from Software Heritage

This example shows you how to create a `CITATION.cff` file
with a [*SoftWare Hash IDentifier*](https://www.swhid.org/) (*SWHID*) that reliably identifies
versions of your software
or parts of your software for citation.
SWHIDs are most commonly used to reference software parts of versions
in the [Software Heritage Archive](https://archive.softwareheritage.org/):
a specific *snapshot*, *release* or *revision*,
or a *directory* or file *content* of the software.
You can even reference specific lines in a file.

{!_assets/snippets/cff-simple-example-swhid.md!}

{!_assets/snippets/copy-paste.md!}
1. Archive your repository in the Software Heritage Archive using their [*Save Code Now*](https://archive.softwareheritage.org/save/) option.
1. Once the save request has been successful, go to the Software Heritage Archive page for your repository
and open the page for the version you want to make citable.
1. Copy the identifier you want people to use for citation from the "Permalinks" menu.
1. Add the identifier in the `identifiers` section of your `CITATION.cff` and define its type as `swh`.
{!_assets/snippets/save-file-maintain.md!}

## How to include multiple identifiers

This example shows you how to create a `CITATION.cff` file
with multiple identifiers.
The different identifiers may serve different citation purposes.
Some enable people to cite the software project as such,
others can be used in reference managers,
or resolve to specific versions of the software.
Some identifiers orreference different software artifacts such as the source code,
a package in a package manager, or the landing page of the software.

{!_assets/snippets/cff-simple-example-combined.md!}

{!_assets/snippets/copy-paste.md!}
1. Add the identifiers you want to provide in the `identifiers` section of your `CITATION.cff`.
Make sure you define a suitable type for each.
1. Briefly describe the exact purpose of each identifier in the `description` field.
{!_assets/snippets/save-file-maintain.md!}

[^1]: Read ["Software Citation Principles"](https://doi.org/10.7717/peerj-cs.86)
to learn more about software citation and relevant software citation metadata.