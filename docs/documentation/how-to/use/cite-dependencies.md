!!! warning
    Incomplete

# How to use the Citation File Format to cite the dependencies of your software

Your software probably depends on other existing software packages or libraries to provide specific functionality,
so that you don't have to implement this functionality yourself.
You should cite these dependencies in your research software,
just like you cite the work that your own work builds on in scientific writing.

This example shows you how to create a `CITATION.cff` file 
that includes references to the dependencies of your software.

{!_assets/snippets/cff-cite-dependencies-example.md!}

{!_assets/snippets/copy-paste.md!}
1. Add `software` references for *all direct* dependencies of your software.
Direct dependencies include all software packages
that the source code of your software uses directly,
including packages that are not strictly required for your software to run
(sometimes called "optional dependencies" or "extras").
1. Consider adding `software` references to software packages that
you use for the development of your software,
especially if they are are important in ensuring the quality of your software.
These "development dependencies" may include
test frameworks,
linters and formatters,
code analysis tools,
etc.
1. Include all metadata fields in the references to the dependencies of your software
that are necessary to identify the exact *version* and the *authors* of the dependency that your software uses.
{!_assets/snippets/save-file-maintain.md!}

There may be :warning: TODO ADD TOOLS PAGE LINK->tools available for some programming languages and build systems
that can automatically create a CFF `references` section from the manifest or requiremnts file for your software (e.g., `pyproject.toml`, `Cargo.toml`, `pom.xml`, `Gemfile`, etc.)
