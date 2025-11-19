!!! warning
    Resolve into how-tos, let main page link directly to exactly these how-tos!

Here are some example `CITATION.cff` files that show
how to use the Citation File Format for different purposes.
You can copy, paste and adapt them for your own use.

## Simple example

This example shows the contents of a valid `CITATION.cff` file that contains all the necessary fields
for users to cite the software correctly[^1].

{!_assets/cff-simple-example.md!}

## Typical example

This example shows the contents of a valid `CITATION.cff` file that
provides some more metadata that may be helpful for users.

{!_assets/cff-typical-example.md!}

## Including references to other work

This example shows the contents of a valid `CITATION.cff` file that
provides references to work that the software builds on.

The references section works like a references list in a paper.
Importantly, references can be to software, so that you can cite the direct dependencies
of your software.

{!_assets/cff-references-example.md!}

## Asking users to cite additional works

This example shows the contents of a valid `CITATION.cff` file that
provides citation information for a work that is related to the software.

As a researcher, your work may still be evaluated based on traditional outputs, i.e., papers or monographs, and their citation.
If this is the case, you can ask your users to cite another work in addition to citing your software,
using the `preferred-citation` field, and describe the preferred way of citing your software in the `message`.

{!_assets/cff-preferred-citation-example.md!}

## Required fields

This example shows the contents of a valid `CITATION.cff` file that uses only the *required* fields.

!!! warning inline end
    While this example is *technically* valid, it is not useful for the purposes of software citation, as a lot of metadata required for citation is missing.

{!_assets/cff-minimal-example.md!}

[^1]: You can read the [software citation principles](https://doi.org/10.7717/peerj-cs.86)
to learn more about software citation and relevant software citation metadata.
