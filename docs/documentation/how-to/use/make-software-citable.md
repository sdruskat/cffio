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

1. Archive the software version in a repository that assigns a DOI to each published software version.
Many projects use the open access repository [Zenodo](https://zenodo.org) for this.
There, you can also pre-reserve a DOI and add it to your CFF file before publication.
Zenodo also gives you a second "concept" DOI.
This identifies all versions of your software at once.
It can be used to cite your whole software *project*, rather than a specific version.
{!_assets/snippets/copy-paste.md!}

## How to include a SoftWare Hash IDentifier from Software Heritage

This example shows you how to create a `CITATION.cff` file 
with a [*SoftWare Hash IDentifier*](https://www.swhid.org/) (*SWHID*) that reliably identifies 
versions of your software 
or parts of your software for citation.

<!-- TODO:     
  "snp"  (* snapshot *)
  | "rel"  (* release *)
  | "rev"  (* revision *)
  | "dir"  (* directory *)
  | "cnt"  (* content *) -->

1. Archive the software version in a repository that assigns a 
unique digital identifier 
to each published software version, e.g.,
a *digital object identifier* (*DOI*).
Many projects use the open access repository [Zenodo](https://zenodo.org)
for this.

{!_assets/snippets/cff-simple-example-doi.md!}

## How to include multiple identifiers

{!_assets/snippets/cff-simple-example-doi.md!}




[^1]: Read ["Software Citation Principles"](https://doi.org/10.7717/peerj-cs.86)
to learn more about software citation and relevant software citation metadata.