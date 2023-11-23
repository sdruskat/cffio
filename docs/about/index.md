# About the Citation File Format (CFF)

<!-- !!! question
    Should there be something else here than history?

## (Background?)

## A brief history -->

## Background

Software is ubiquitous in research.
Not only is it *used* to conduct research,
it is also *created* specifically for this purpose in many cases.

The people that create this *research software* often struggle to be recognized for the crucial software work they do.
This is because the *academic paper* is still the most prestigious way to present the research that has been done.
But if you spend a lot of your time creating or maintaining research software, you may not have the time
to write papers, or even sufficiently increase your expertise in a specific field of research.

Nevertheless, almost all research that is "advertized" in papers relies on research software,
but *academic credit* is usually given to the domain scientists that are listed as (important) authors of papers.

We believe that **research software is so important, that it must be *cited*** in the papers and other works that report research
which has been conducted using research software.
By citing software, the *software authors* that have created or are maintaining it can receive credit,
and use that credit in building their careers.

But *software citation*[^1] is important in more ways than to award recognition for software authors.
In fact, it is a necessary prerequisite for the *reproducibility of research*.
Only if you *cite the exact version* of the software you have used in your research -- and describe exactly how you have used it -- 
can others fully understand your research and can attempt to reproduce its results.

[^1]: If you want to learn more about software citation, we suggest you read about the [Software Citation Principles](https://doi.org/10.7717/peerj-cs.86).

### Software citation needs metadata!

In order to cite the exact version of the software they have used in their research,
researchers must have the **complete and correct metadata** for the software.

Unfortunately, software as such does not have a title page like papers do, 
where all the relevant metadata is included.

This is where the **Citation File Format** comes in:
You can create a "title page" for your software by providing a `CITATION.cff` file for your software!
If you *add this file* to your software's source code repository, *update it* for each new version and *ship it* with your software,
users can use the metadata from this file to **cite the software correctly**!
