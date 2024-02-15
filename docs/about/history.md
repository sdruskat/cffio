---
authors:
  - name: Stephan Druskat
---

# A brief history of the Citation File Format

## Predecessors

On 30 August 2013, [Robin Wilson](https://orcid.org/0000-0001-7352-8912) - fellow of the British [Software Sustainability Institute (SSI)](https://software.ac.uk) - published a blog post
that was [re-published on the SSI's blog](https://web.archive.org/web/20231123110743/https://www.software.ac.uk/blog/encouraging-citation-software-introducing-citation-files).
In this post, he proposes the addition of **plaintext files named `CITATION`** to source code repositories.
These files should contain information about how to cite the respective software.

## A standard format for `CITATION` files?

Based on [Robin Wilson's previous work](#predecessors), [Stephan Druskat](https://orcid.org/0000-0003-4925-7248) proposed a
standard format for `CITATION` files in a [lightning talk]((https://doi.org/10.6084/m9.figshare.3827058.v4)) at the [Workshop on Sustainable Software for Science: Practice and Experiences (WSSSPE5.1)](https://wssspe.researchcomputing.org.uk/wssspe5-1/)
on 06 September 2017 in Manchester, UK.
The proposal was discussed further at the workshop, and the outcomes of the discussion published in a [blog post on the SSI blog](https://web.archive.org/web/20231123113500/https://www.software.ac.uk/blog/standard-format-citation-files). The discussion group defined **requirements for a standard format for `CITATION` files**, such as support for: human- and machine-readability, human-writability, a dedicated reference type for software, version identifiers, persistent identifiers, release dates, software authors and their [ORCiD](https://orcid.org/)s, references to the described software's dependencies and other works. Additionally, the format should be compatible with other metadata formats, and should support Unicode.

Between the discussion at the workshop and the publication of the blog post on 12 December 2017,
Stephan Druskat started specifying a format that would meet the discussed requirements on 19 September 2017, and published the **first draft of the Citation File Format** ([0.9-RC1](https://doi.org/10.5281/zenodo.1003150)) on 06 October 2017.

## Community work

The first version of CFF was referenced in the [blog post](https://web.archive.org/web/20231123113500/https://www.software.ac.uk/blog/standard-format-citation-files)
reporting the discussion mentioned above, as a suggested format that met the requirements for machine-readable `CITATION` files.
To **build support for the format and a community**, CFF was presented and discussed at different in-person and online events[^1] in the US, the UK, Portugal, Germany and the Netherlands starting in late 2018.
While some presentations were used for publicity, outreach and the gathering of initial feedback, other events included in-depth discussions that informed future versions of CFF.

The **growing community** also continued working hands-on on the CFF format, schema and documentation, and on tooling that worked with CFF:

- **CFF version [1.0.0](https://doi.org/10.5281/zenodo.1108269)** was released as an outcome of work done by Morane Gruenpeter, Neil Chue Hong and Stephan Druskat at a hackathon of the FORCE11 Software Citation Implementation WG hackathon during the FORCE2017 conference in Berlin (Germany).
- **CFF version [1.0.3](https://doi.org/10.5281/zenodo.3515946)** included additional work by James Baker, Robert Haines and Stephan Druskat on the format specifications, partly done during the hack day of the Software Sustainability Institute's Collaborations Workshop 2018 in Cardiff (UK).
- Robert Haines created **[`ruby-cff`](https://github.com/citation-file-format/ruby-cff)**, a Ruby library that converts and validates CFF files.
- Jurriaan Spaaks created **[`cffconvert`](https://github.com/citation-file-format/cffconvert)**, a Python library that converts and validates CFF files.
- The [Research Software Directory](https://research-software-directory.org/) developed at the Netherlands eScience Center ingests metadata for the software it lists from CFF files.

Meanwhile, the first `CITATION.cff` files started appearing on collaborative software development platforms such as GitHub, GitLab, and others.

The Citation File Format isn't the only metadata format to describe (research) software,
or provide citation information.
The [CodeMeta project](https://codemeta.github.io/), for example, provides a linked data schema that extends schema.org to
describe (research) software.
As part of the community work, CFF was compared and contrasted with other formats
in discussions with the community
to assess its viability and usefulness for the research software community (for details, see the [FAQs](../documentation/faq.md)).

As of late 2018, the Citation File Format project was maintained by Stephan Druskat.
This changed during the [WSSSPE6.1](https://wssspe.researchcomputing.org.uk/wssspe6-1/) in Amsterdam (the Netherlands),
when Jurriaan Spaaks agreed to join the project as co-lead.
Jurriaan had prior experience with CFF as a main developer of both [`cffconvert`](https://github.com/citation-file-format/cffconvert)
and the Netherlands eScience Center's [Research Software Directory](https://research-software-directory.org/).

Together, Stephan and Jurriaan developed and released **CFF version [1.1.0](https://doi.org/10.5281/zenodo.4813122)** in May 2021.


[^1]: Events at which the Citation File Format was presented, discussed or worked upon include the [Scientific Software Registry Collaboration Workshop](https://doi.org/10.6084/m9.figshare.10296917.v1) at the University of Maryland (USA), the ["Software Engineering and Reuse in Computational Science and Engineering" birds-of-a-feather session](https://doi.org/10.6084/m9.figshare.11276087.v1) at the ISC High Performance conference in Frankfurt/Main (Germany), a [meeting of the working group "Research Practice"](https://doi.org/10.6084/m9.figshare.9918653.v1) of the Alliance of Research Organisations in Bonn (Germany), a [Berlin Colloquium of Library Sciences](https://zenodo.org/doi/10.5281/zenodo.3876118) online, the [2018 Conference of Research Software Engineers](https://doi.org/10.6084/m9.figshare.7053698.v1) in Birmingham (UK), and a [dedicated hack day](https://www.software.ac.uk/blog/hacking-software-citation-implementation-citation-file-format-hack-day-rse18) co-locating with the conference, a [Faculty Day "Research Data"](https://zenodo.org/doi/10.5281/zenodo.1172281) at the faculty of language, literature and humanities at Humboldt-Universität zu Berlin in Berlin (Germany), the [2018 Collaborations Workshop](https://doi.org/10.6084/m9.figshare.6139406.v1) of the Software Sustainability Institute in Cardiff (UK), a [FORCE11 Software Citation Implementation Working Group hackathon](https://www.software.ac.uk/blog/hacking-future-software-citation) in Berlin (Germany), the [9th Workshop on Sustainable Software for Science: Practice and Experiences (WSSSPE6.1)](https://www.software.ac.uk/blog/credit-and-recognition-research-software-current-state-practice-and-outlook) during the IEEE eScience conference in Amsterdam (the Netherlands), and the [9th Brazil-Portugal Conference on Open Access](https://www.software.ac.uk/blog/9th-confoa-brazil-portugal-conference-open-access) in Lisbon (Portugal).

## A standard format for `CITATION` files for software!

In late 2018, 

- Jurriaan becomes maintainer
- 1.1.0
- more community work
- 1.2.0 (with JSON schema)
- GitHub, Zotero, Zenodo, JabRef, IDEs
- Rising number of files

NEWER ONES

- https://zenodo.org/records/7312323
- https://zenodo.org/records/6598444
- https://zenodo.org/records/5764777
- https://zenodo.org/records/5529914
- https://zenodo.org/records/5222321
- https://zenodo.org/records/7835366
- https://zenodo.org/records/7655140
- https://zenodo.org/records/7560153
- https://zenodo.org/records/7346192

## The Citation File Format project

- As is
