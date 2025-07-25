# Pap2Pat Dataset


## Installation

```bash
poetry install
```


## Usage


### Evaluation


```py
import pap2pat

preds = pap2pat.Predictions(
    {
        sample_id: generated_text
    }
)
preds.compute_bleu()
preds.compute_rouge()
preds.compute_tokens()
preds.compute_rr()
preds.compute_bertscore()

metrics = preds.average_metrics()
```



### File Schema

Every directory in `data` corresponds to one patent-paper pair and contains the full texts of both patent and paper, as well as the patent outlines. We include all information in JSON for programmatic parsing and Markdown for manual inspection.

```yaml
data/:
    paper_id-patent_id/:
        # Nested JSON format
        patent.json: JSON file containing patent metadata and full-text, as well as all outlines
        paper.json: JSON file containing paper metadata and full-text
        # Markdown format
        patent.md: patent full-text formatted in markdown
        paper.md: paper full-text formatted in markdown
        patent_outline_long.md: long patent outline formatted in markdown
        patent_outline_medium.md: medium patent outline formatted in markdown
        patent_outline_short.md: short patent outline formatted in markdown
        patent_outline_empty.md: empty (headings only) patent outline formatted in markdown
```

JSON Schema of `patent.json`:

```json
{
    "id": "str; USPTO Patent number",
    "authors": "list[str]; Inventor names",
    "title": "str; Patent title",
    "date": "str; Patent application date. Publication date is available in data/metadata.json",
    "abstract": "str; Patent abstract",
    "sections": [
        {
            "title": "str; Section title",
            "paragraphs": "list[str]; Section paragraphs",
            "num_characters": "int; Number of characters in this section. Does not include subsections",
            "outline_long": "list[str]; long list of bullet points outlining this section's text. Does not include subsections",
            "outline_medium": "list[str]; medium list of bullet points outlining this section's text. Does not include subsections",
            "outline_short": "list[str]; short list of bullet points outlining this section's text. Does not include subsections",
            "subsections": "list[dict]; list of subsections in the same format with title, paragraphs, num_characters, outline_long, outline_medium, outline_short and subsections"
        },
    ...
    ],
    "claims": "list[str]; Patent claims"
}
```

JSON Schema of `paper.json`:

```json
{
    "id": "str; OpenAlex paper ID",
    "authors": "list[str]; author names",
    "title": "str; Paper title",
    "date": "str; Paper publication date",
    "abstract": "str; Paper abstract",
    "sections": [
        {
            "title": "str; Section title",
            "paragraphs": "list[str]; Section paragraphs",
            "subsections": "list[dict]; list of subsections in the same format with title, paragraphs, and subsections"
        },
    ...
    ],
}
```
