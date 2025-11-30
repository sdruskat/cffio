!!! success
    Complete

# How to use the Citation File Format to cite other work that your software builds on

The Citation File Format lets you [make your software citable](make-software-citable.md).
In the `CITATION.cff` file for your software, you can [cite the dependencies of your software](cite-dependencies.md),
but you can also cite other work that your software builds on.
This includes, for example, articles, conference papers, monographs or preprints describing an algorithm or method that you implement in your software, or other research work that your software takes into account.

!!! note
    If you want others to cite a paper or other work that describes your software
    *in addition* to the software itself,
    see [*How to use the Citation File Format to let others also cite a paper or other work*](preferred-citation.md).

This example shows you how to create a `CITATION.cff` file 
that includes references to other work that your software builds on,
and that is *not* a [software package or library that your software depends on](cite-dependencies.md) to run.

{!_assets/snippets/cff-cite-other-work-example.md!}

{!_assets/snippets/copy-paste.md!}
1. Add references for *all relevant other work*
that your software builds on.
To decide what is relevant, 
think about a paper that you would write to describe your software.
Include references to all work that you would cite in the paper.
{!_assets/snippets/save-file-maintain.md!}
