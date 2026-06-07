"""
MCP Server: Thesis Paper Search
Searches OpenAlex (250M+ papers, free, no key) across 10 topic areas
relevant to ML-based groundwater potential mapping.

Tools:
  search_papers(query, limit)         — free-text search
  search_topic(topic_key)             — predefined topic search
  get_bibtex(openalex_id)             — return BibTeX entry for a paper
  bulk_search_all_topics()            — search all 10 topics at once
  search_pakistan_groundwater()       — Pakistan/Pothohar specific
"""

import httpx
import json
import re
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("thesis-papers")

BASE   = "https://api.openalex.org"
MAILTO = "zeeshamali472@gmail.com"
HDR    = {"User-Agent": f"GW-Thesis/1.0 (mailto:{MAILTO})"}

# ── Pre-defined topic searches for the thesis ─────────────────────────────────
TOPICS = {
    "ml_groundwater_mapping":
        "machine learning groundwater potential mapping remote sensing",
    "xgboost_gis":
        "XGBoost random forest LightGBM land use remote sensing classification",
    "gee_water_resources":
        "Google Earth Engine groundwater water resources mapping",
    "ndvi_ndwi_groundwater":
        "NDVI NDWI vegetation index groundwater potential GIS",
    "dem_twi_groundwater":
        "DEM SRTM topographic wetness index TWI groundwater recharge",
    "rainfall_recharge":
        "CHIRPS rainfall recharge groundwater potential spatial",
    "soil_texture_permeability":
        "soil texture permeability infiltration groundwater aquifer SoilGrids",
    "weighted_overlay_gis":
        "weighted overlay multi-criteria GIS groundwater potential zones",
    "pakistan_punjab_groundwater":
        "groundwater Pakistan Punjab aquifer water table",
    "pothohar_hydrology":
        "Pothohar Plateau Chakwal Rawalpindi Attock Jhelum Mianwali groundwater hydrology",
    "deep_learning_hydrogeology":
        "deep learning convolutional neural network groundwater hydrogeology mapping",
    "rs_review_groundwater":
        "remote sensing review groundwater delineation potential zones systematic",
}


def _fmt_authors(authorships: list) -> str:
    names = []
    for a in authorships[:5]:
        auth = a.get("author", {})
        name = auth.get("display_name", "")
        if name:
            names.append(name)
    suffix = " et al." if len(authorships) > 5 else ""
    return ", ".join(names) + suffix if names else "Unknown"


def _fmt_paper(w: dict) -> dict:
    doi  = w.get("doi") or ""
    year = w.get("publication_year") or ""
    venue = ""
    if w.get("primary_location"):
        src = w["primary_location"].get("source") or {}
        venue = src.get("display_name", "")
    abstract = w.get("abstract_inverted_index")
    abs_text = "N/A"
    if abstract:
        try:
            words = {pos: word for word, positions in abstract.items()
                     for pos in positions}
            abs_text = " ".join(words[i] for i in sorted(words))[:400]
        except Exception:
            abs_text = "N/A"
    return {
        "id"       : w.get("id", "").replace("https://openalex.org/", ""),
        "title"    : w.get("display_name", "N/A"),
        "authors"  : _fmt_authors(w.get("authorships", [])),
        "year"     : year,
        "venue"    : venue,
        "doi"      : doi,
        "citations": w.get("cited_by_count", 0),
        "abstract" : abs_text,
        "url"      : w.get("open_access", {}).get("oa_url") or doi or "",
    }


def _search(query: str, limit: int = 10, year_from: int = 2015) -> list[dict]:
    params = {
        "search"      : query,
        "per-page"    : min(limit, 50),
        "filter"      : f"publication_year:>{year_from - 1}",
        "sort"        : "cited_by_count:desc",
        "select"      : "id,display_name,authorships,publication_year,"
                        "primary_location,doi,cited_by_count,"
                        "abstract_inverted_index,open_access",
        "mailto"      : MAILTO,
    }
    try:
        r = httpx.get(f"{BASE}/works", params=params, headers=HDR, timeout=20)
        r.raise_for_status()
        return [_fmt_paper(w) for w in r.json().get("results", [])]
    except Exception as e:
        return [{"error": str(e)}]


def _to_bibtex(paper: dict) -> str:
    title   = paper.get("title", "")
    authors = paper.get("authors", "")
    year    = str(paper.get("year", ""))
    venue   = paper.get("venue", "")
    doi     = paper.get("doi", "")
    pid     = paper.get("id", "ref")

    # Build cite key: FirstAuthorLastname + year
    first_author = authors.split(",")[0].strip().split()[-1].lower()
    first_author = re.sub(r"[^a-z]", "", first_author)
    key = f"{first_author}{year}"

    lines = [
        f"@article{{{key},",
        f'  author  = {{{authors}}},',
        f'  title   = {{{title}}},',
        f'  journal = {{{venue}}},',
        f'  year    = {{{year}}},',
    ]
    if doi:
        lines.append(f'  doi     = {{{doi}}},')
    lines.append("}")
    return "\n".join(lines)


# ── MCP Tools ──────────────────────────────────────────────────────────────────

@mcp.tool()
def search_papers(query: str, limit: int = 10, year_from: int = 2015) -> str:
    """
    Search OpenAlex for papers matching any query.
    Returns title, authors, year, venue, DOI, citation count, and abstract snippet.
    """
    results = _search(query, limit, year_from)
    if not results:
        return "No results found."
    out = []
    for i, p in enumerate(results, 1):
        out.append(
            f"{i}. [{p.get('citations',0)} cites] {p.get('title')}\n"
            f"   Authors : {p.get('authors')}\n"
            f"   Year    : {p.get('year')}  |  Venue: {p.get('venue')}\n"
            f"   DOI     : {p.get('doi','N/A')}\n"
            f"   Abstract: {p.get('abstract','N/A')[:250]}...\n"
        )
    return "\n".join(out)


@mcp.tool()
def search_topic(topic_key: str, limit: int = 8) -> str:
    """
    Search a predefined thesis topic. Available keys:
    ml_groundwater_mapping, xgboost_gis, gee_water_resources,
    ndvi_ndwi_groundwater, dem_twi_groundwater, rainfall_recharge,
    soil_texture_permeability, weighted_overlay_gis,
    pakistan_punjab_groundwater, pothohar_hydrology,
    deep_learning_hydrogeology, rs_review_groundwater
    """
    if topic_key not in TOPICS:
        available = ", ".join(TOPICS.keys())
        return f"Unknown topic. Available: {available}"
    query = TOPICS[topic_key]
    results = _search(query, limit)
    if not results:
        return f"No results for topic: {topic_key}"
    out = [f"=== Topic: {topic_key} ===\nQuery: {query}\n"]
    for i, p in enumerate(results, 1):
        out.append(
            f"{i}. {p.get('title')}\n"
            f"   {p.get('authors')} ({p.get('year')}) — {p.get('venue')}\n"
            f"   Citations: {p.get('citations',0)}  |  DOI: {p.get('doi','N/A')}\n"
        )
    return "\n".join(out)


@mcp.tool()
def get_bibtex(openalex_id: str) -> str:
    """
    Fetch full metadata for a paper by its OpenAlex ID (e.g. W2741809807)
    and return a BibTeX entry ready to paste into references.bib.
    """
    url = f"{BASE}/works/{openalex_id}"
    try:
        r = httpx.get(url, params={"mailto": MAILTO}, headers=HDR, timeout=15)
        r.raise_for_status()
        paper = _fmt_paper(r.json())
        return _to_bibtex(paper)
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def bulk_search_all_topics(papers_per_topic: int = 5) -> str:
    """
    Search ALL 12 predefined thesis topics at once.
    Returns top N papers per topic — use this to build the full reference list.
    """
    all_papers = []
    seen_dois  = set()
    out        = ["=== BULK SEARCH — All Thesis Topics ===\n"]

    for topic_key, query in TOPICS.items():
        out.append(f"\n--- {topic_key.upper().replace('_',' ')} ---")
        results = _search(query, papers_per_topic)
        count = 0
        for p in results:
            doi = p.get("doi", "")
            if doi and doi in seen_dois:
                continue
            if doi:
                seen_dois.add(doi)
            out.append(
                f"  • {p.get('title')}\n"
                f"    {p.get('authors')} ({p.get('year')}) — {p.get('venue')}\n"
                f"    Citations: {p.get('citations',0)}  DOI: {doi or 'N/A'}\n"
            )
            all_papers.append(p)
            count += 1
        out.append(f"  [{count} papers found for this topic]")

    out.append(f"\n=== TOTAL UNIQUE PAPERS: {len(all_papers)} ===")
    return "\n".join(out)


@mcp.tool()
def search_pakistan_groundwater(limit: int = 15) -> str:
    """
    Focused search for Pakistan / Pothohar / Punjab groundwater papers.
    Returns papers most relevant to the study area.
    """
    queries = [
        "groundwater potential zones Pakistan Punjab GIS remote sensing",
        "Pothohar Plateau groundwater hydrology Pakistan",
        "Chakwal Rawalpindi Attock Jhelum Mianwali water resources",
        "PCRWR Pakistan groundwater monitoring level",
        "groundwater depletion Punjab Pakistan aquifer",
    ]
    seen = set()
    out  = ["=== Pakistan / Pothohar Groundwater Papers ===\n"]
    count = 0
    for q in queries:
        results = _search(q, limit // len(queries) + 3, year_from=2010)
        for p in results:
            doi = p.get("doi", "")
            key = doi or p.get("title", "")
            if key in seen:
                continue
            seen.add(key)
            out.append(
                f"{count+1}. {p.get('title')}\n"
                f"   {p.get('authors')} ({p.get('year')}) — {p.get('venue')}\n"
                f"   Citations: {p.get('citations',0)}  DOI: {doi or 'N/A'}\n"
            )
            count += 1
            if count >= limit:
                break
        if count >= limit:
            break
    out.append(f"\nTotal: {count} papers")
    return "\n".join(out)


@mcp.tool()
def generate_bibtex_file(topic_key: str = "all", papers_per_topic: int = 4) -> str:
    """
    Generate a complete .bib file content for one topic or all topics.
    Pass topic_key='all' to get all topics.
    Paste the output directly into references.bib.
    """
    if topic_key == "all":
        topics_to_search = TOPICS
    elif topic_key in TOPICS:
        topics_to_search = {topic_key: TOPICS[topic_key]}
    else:
        return f"Unknown topic. Available: {', '.join(TOPICS.keys())}"

    seen_dois = set()
    entries   = []
    used_keys = set()

    for tkey, query in topics_to_search.items():
        results = _search(query, papers_per_topic)
        for p in results:
            doi = p.get("doi", "")
            if doi and doi in seen_dois:
                continue
            if doi:
                seen_dois.add(doi)
            bib = _to_bibtex(p)
            # Deduplicate cite keys
            key_match = re.search(r"@article\{(\w+),", bib)
            if key_match:
                key = key_match.group(1)
                if key in used_keys:
                    bib = bib.replace(f"@article{{{key},",
                                      f"@article{{{key}_{tkey[:4]},", 1)
                else:
                    used_keys.add(key)
            entries.append(f"% Topic: {tkey}\n{bib}\n")

    header = (
        "% Auto-generated bibliography — D:\\GW-Thesis\\references.bib\n"
        "% Generated by thesis-papers MCP server\n"
        f"% Total entries: {len(entries)}\n\n"
    )
    return header + "\n".join(entries)


if __name__ == "__main__":
    mcp.run(transport="stdio")
