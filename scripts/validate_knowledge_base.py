#!/usr/bin/env python3
"""Validate the approved knowledge corpus and current batch; never read original sources."""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import hashlib
import math
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("Cannot run: existing PyYAML is unavailable; no dependencies installed.")

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "03_knowledge_base"
EXPECTED = {
    "ma4502": "02_profiles/courses/ma4502-combinatorial-optimization.md",
    "in2361": "02_profiles/courses/in2361-natural-language-processing.md",
    "ei7646": "02_profiles/courses/ei7646-computational-neuroscience.md",
    "additional-cognitive-systems": "02_profiles/courses/additional-cognitive-systems-technical-cognitive-systems.md",
    "ma4802": "02_profiles/courses/ma4802-statistical-learning.md",
    "cit4230003": "02_profiles/courses/cit4230003-advanced-machine-learning-deep-generative-models.md",
    "additional-foml": "02_profiles/courses/additional-foml-fundamentals-of-optimization-for-machine-learning.md",
    "tum-machine-learning-optimization": "02_profiles/supplementary/machine_learning.md",
    "ma3001": "02_profiles/courses/ma3001-functional-analysis.md",
    "ma4800": "02_profiles/courses/ma4800-foundations-of-data-analysis.md",
    "ma3503": "02_profiles/courses/ma3503-nonlinear-optimization.md",
    "ma5348": "02_profiles/courses/ma5348-numerical-methods-uncertainty-quantification.md",
    "ma6015": "02_profiles/courses/ma6015-advanced-seminar-course.md",
    "ma6018": "02_profiles/projects/thesis.md",
    "ma8102": "02_profiles/projects/pyloworder.md",
    "scientific_paper": "02_profiles/projects/ngvalidation.md",
    "tum-approximate-dynamic-programming": "02_profiles/supplementary/approximate_dynamic_programming.md",
    "cit413042": (
        "02_profiles/courses/cit413042-case-studies-optimization.md",
        "02_profiles/projects/case_studies_optimization.md",
    ),
    "in2138": "02_profiles/courses/in2138-robot-motion-planning.md",
    "tum-advanced-control": "02_profiles/supplementary/advanced_control.md",
    "mgt001299": "02_profiles/courses/mgt001299-introduction-to-deep-reinforcement-learning.md",
    "ei7263": "02_profiles/courses/ei7263-biologically-inspired-learning-humanoid-robots.md",
    "tum-dynamical-systems": "02_profiles/supplementary/dynamical_systems.md",
    "tum-mobile-robotics": "02_profiles/supplementary/mobile_robotics.md",
}
CATEGORIES = {"accredited_coursework", "documented_project_work", "supplementary_academic_material"}
KINDS = {"knowledge", "implementation", "contribution", "decision", "result", "lesson"}
BASES = {"course_material", "project_code", "project_report", "external_reference", "supplementary_material"}
ACTORS = {"user", "team", "third_party", "unspecified", "not_applicable"}
VERIFICATIONS = {"not_applicable", "statically_documented", "reported_not_reproduced", "independently_reproduced"}
PERSONAL_KINDS = {"implementation", "contribution", "decision"}


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def parse(text):
    return yaml.load(text, Loader=UniqueLoader)


def rows_by_id(rows, label):
    result = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise ValueError(f"{label}: missing string id")
        if row["id"] in result:
            raise ValueError(f"{label}: duplicate id {row['id']}")
        result[row["id"]] = row
    return result


def headings(text):
    return re.findall(r"^#{2,3} (.+)$", text, re.M)


def frontmatter(path):
    text = path.read_text()
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError(f"{path}: missing front matter")
    data = parse(match[1])
    if not isinstance(data, dict) or data.get("id") != path.stem:
        raise ValueError(f"{path}: metadata/filename ID mismatch")
    if len(text[match.end():].split()) < 60:
        raise ValueError(f"{path}: missing substantive Markdown body")
    return data


def claim_errors(c, experiences, concepts, texts):
    errors = []
    required = {"id", "experience", "kind", "concepts", "statement", "basis", "actor", "verification", "references", "limitations"}
    if not required <= c.keys():
        return [f"Missing claim fields: {required - c.keys()}"]
    exp = experiences.get(c["experience"])
    if exp is None:
        return ["Unknown claim experience"]
    if not c["id"].startswith(c["experience"] + ":"):
        errors.append("Claim ID does not preserve experience namespace")
    for field, allowed in [("kind", KINDS), ("basis", BASES), ("actor", ACTORS), ("verification", VERIFICATIONS)]:
        if c[field] not in allowed:
            errors.append(f"Invalid {field}")
    if not c["statement"] or not c["concepts"] or not set(c["concepts"]) <= concepts.keys():
        errors.append("Missing statement or unknown/empty concepts")
    if not isinstance(c["limitations"], list):
        errors.append("Limitations must be a list")
    allowed_profiles = {p["path"] for p in exp["profiles"]}
    if not isinstance(c["references"], list) or not c["references"]:
        errors.append("Missing references")
    else:
        for ref in c["references"]:
            p = ref.get("profile")
            if p not in allowed_profiles or p not in texts or ref.get("section") not in headings(texts.get(p, "")):
                errors.append("Profile reference/section locator does not resolve to its experience")
    if c["basis"] in {"course_material", "supplementary_material"} and (c["kind"] != "knowledge" or c["actor"] != "not_applicable"):
        errors.append("Course/supplementary content promoted to personal activity")
    if "supplementary_academic_material" in exp["facets"] and c["basis"] != "supplementary_material":
        errors.append("Supplementary provenance lost")
    if c["basis"] == "external_reference" and c["actor"] == "user":
        errors.append("External evidence promoted to a personal outcome")
    if c["kind"] == "result":
        payload = c.get("result", {})
        if not all(payload.get(k) for k in ["metric", "values", "unit", "evaluation_context"]):
            errors.append("Result lacks metric/values/unit/context")
        if not c["limitations"] or c["verification"] not in {"reported_not_reproduced", "independently_reproduced"}:
            errors.append("Result lacks limitations or empirical verification qualification")
        for value in payload.get("values", []):
            number = value.get("value")
            if not value.get("method") or not isinstance(number, (float, int)) or isinstance(number, bool) or not math.isfinite(number):
                errors.append("Invalid labeled result value")
            if "denominator" in value and (value["denominator"] <= 0 or number > value["denominator"]):
                errors.append("Invalid result denominator")
    if c["kind"] == "decision" and not all(c.get("decision", {}).get(k) for k in ["choice", "context", "rationale"]):
        errors.append("Decision lacks choice/context/rationale")
    if c["kind"] == "lesson" and not all(c.get("lesson", {}).get(k) for k in ["observation", "implication", "scope"]):
        errors.append("Lesson lacks observation/implication/scope")
    return errors


def competency_errors(cap, claims):
    refs = cap.get("evidence_refs", [])
    if not refs or any(r not in claims for r in refs):
        return ["Missing/unknown competency evidence"]
    supported = any(claims[r]["actor"] == "user" and claims[r]["kind"] in PERSONAL_KINDS
                    and claims[r]["basis"] in {"project_code", "project_report"} for r in refs)
    return [] if supported else ["Competency has no documented personal activity"]


def main():
    experiences = rows_by_id(parse((KB / "experiences.yaml").read_text())["experiences"], "experiences")
    if set(experiences) != set(EXPECTED):
        raise ValueError("Registry does not contain exactly the approved pilot and current batch experiences")
    taxonomy = rows_by_id(parse((KB / "taxonomy.yaml").read_text())["domains"], "taxonomy")
    concepts = rows_by_id([frontmatter(p) for p in sorted((KB / "concepts").glob("*.md"))], "concepts")
    caps = rows_by_id([frontmatter(p) for p in sorted((KB / "competencies").glob("*.md"))], "competencies")
    texts, errors = {}, []
    for eid, exp in experiences.items():
        for field in ["title", "profiles", "facets", "academic_credit", "learning_relationship", "limitations"]:
            if field not in exp:
                raise ValueError(f"{eid}: missing {field}")
        if not exp["facets"] or not set(exp["facets"]) <= CATEGORIES:
            errors.append(f"{eid}: invalid provenance facets")
        if exp["academic_credit"] not in {"established", "not_established", "not_applicable"}:
            errors.append(f"{eid}: invalid academic-credit status")
        expected_paths = {EXPECTED[eid]} if isinstance(EXPECTED[eid], str) else set(EXPECTED[eid])
        if len(exp["profiles"]) != len(expected_paths) or {p["path"] for p in exp["profiles"]} != expected_paths:
            raise ValueError(f"{eid}: unexpected or duplicate profile mapping")
        if eid in {"ma3001", "ma4800", "ma3503", "ma5348", "ma6015", "ma6018", "ma8102", "cit413042", "in2138", "mgt001299", "ei7263", "ma4802", "cit4230003", "ma4502", "in2361", "ei7646"} and exp.get("associated_module") != eid.upper():
            errors.append(f"{eid}: academic association lost")
        if eid == "cit413042" and {p["path"]: p["category"] for p in exp["profiles"]} != {
            EXPECTED[eid][0]: "accredited_coursework", EXPECTED[eid][1]: "documented_project_work"
        }:
            errors.append("Case Studies course/project facets do not preserve the shared academic experience")
        if eid.startswith("tum-") and (exp["academic_credit"] != "not_established" or exp["learning_relationship"] != "unspecified"
                                       or exp.get("source_category") != "supplementary_academic_material"):
            errors.append("Supplementary experience overstates provenance")
        for p in exp["profiles"]:
            if p["category"] not in exp["facets"]:
                errors.append(f"{eid}: profile/facet mismatch")
            data = (ROOT / p["path"]).read_bytes()
            if hashlib.sha256(data).hexdigest() != p["sha256"]:
                errors.append(f"{eid}: stale profile hash")
            texts[p["path"]] = data.decode()
    all_claims = []
    for p in sorted((KB / "evidence").glob("*.yaml")):
        data = parse(p.read_text())
        if data["experience"] != p.stem or data["experience"] not in experiences:
            errors.append(f"{p}: invalid experience/file association")
        for c in data["claims"]:
            if c["experience"] != data["experience"]:
                errors.append(f"{p}: cross-experience claim")
            all_claims.append(c)
    claims = rows_by_id(all_claims, "claims")
    if {p.stem for p in (KB / "evidence").glob("*.yaml")} != set(experiences):
        errors.append("Evidence files do not cover exactly the registered experiences")
    for c in claims.values():
        errors.extend(f"{c['id']}: {e}" for e in claim_errors(c, experiences, concepts, texts))
        for relation in c.get("related_claims", []):
            if relation["type"] not in {"contrasts_with", "qualifies"} or relation["target"] not in claims:
                errors.append(f"{c['id']}: invalid claim relationship")
    for kind, rows in [("concept", concepts), ("competency", caps)]:
        for row in rows.values():
            required = {"id", "title", "evidence_refs", "status", "domains" if kind == "concept" else "concepts"}
            if not required <= row.keys() or row.get("status") not in {"draft", "reviewed"}:
                errors.append(f"{row['id']}: missing fields/status")
            if not row.get("evidence_refs") or not set(row.get("evidence_refs", [])) <= claims.keys():
                errors.append(f"{row['id']}: invalid evidence references")
            if kind == "concept":
                if not row["domains"] or not set(row["domains"]) <= taxonomy.keys():
                    errors.append(f"{row['id']}: invalid domains")
                for ref in row["evidence_refs"]:
                    if ref in claims and row["id"] not in claims[ref]["concepts"]:
                        errors.append(f"{row['id']}: claim does not concern this concept")
                for rel in row.get("relations", []):
                    if rel["type"] not in {"requires", "specializes", "contrasts_with", "related_to"} or rel["target"] not in concepts:
                        errors.append(f"{row['id']}: invalid concept relationship")
                    if rel["type"] in {"related_to", "contrasts_with"} and row["id"] >= rel["target"]:
                        errors.append(f"{row['id']}: symmetric edge not stored once in ID order")
            else:
                if not row["concepts"] or not set(row["concepts"]) <= concepts.keys():
                    errors.append(f"{row['id']}: invalid concepts")
                errors.extend(f"{row['id']}: {e}" for e in competency_errors(row, claims))
                if not set(row["concepts"]) <= {cid for ref in row["evidence_refs"] if ref in claims for cid in claims[ref]["concepts"]}:
                    errors.append(f"{row['id']}: competency concepts lack supporting claims")
    coverage = parse((KB / "coverage.yaml").read_text())["profiles"]
    if len(coverage) != len(texts) or {r["profile"] for r in coverage} != texts.keys():
        errors.append("Coverage does not contain exactly the registered profiles")
    for row in coverage:
        if row["profile"] not in texts:
            continue
        expected_sections = headings(texts[row["profile"]])
        if [s["section"] for s in row["sections"]] != expected_sections:
            errors.append(f"{row['profile']}: missing/duplicate/reordered coverage headings")
        profile_hash = hashlib.sha256(texts[row["profile"]].encode()).hexdigest()
        if row["sha256"] != profile_hash or row["status"] not in {"draft", "reviewed"}:
            errors.append("Invalid coverage hash/status")
        for s in row["sections"]:
            expected_refs = {c["id"] for c in claims.values() if any(r["profile"] == row["profile"] and r["section"] == s["section"] for r in c["references"])}
            if set(s["evidence_refs"]) != expected_refs:
                errors.append(f"{s['section']}: coverage/actual claim mismatch")
            expected_concepts = {cid for ref in expected_refs for cid in claims[ref]["concepts"]}
            if set(s["concepts"]) != expected_concepts:
                errors.append(f"{s['section']}: coverage/concept mismatch")
            if s["disposition"] not in {"mapped", "partial", "context_only", "gap"} or not s.get("reason"):
                errors.append("Invalid coverage disposition/reason")
            if expected_refs and s["disposition"] not in {"mapped", "partial"}:
                errors.append("Extracted section marked unextracted")
            if not expected_refs and s["disposition"] in {"mapped", "partial"}:
                errors.append("Coverage claims extraction without evidence")
        if row["status"] == "reviewed" and any(s["disposition"] in {"partial", "gap"} for s in row["sections"]):
            errors.append("Incomplete profile marked fully reviewed")
    for p in KB.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", p.read_text()):
            if target.startswith(("https://", "http://")):
                continue
            path, _, anchor = target.partition("#")
            if not (p.parent / path).is_file():
                errors.append(f"{p.name}: broken Markdown link {target}")
            if anchor:
                errors.append(f"{p.name}: use checked exact YAML section locators rather than unchecked anchors")
    if errors:
        raise ValueError("\n- " + "\n- ".join(errors))
    # Invalid-input tests are in-memory only, not a new testing framework.
    bad = deepcopy(claims["ma8102:dlr-nlr-mae"]); bad["actor"] = "user"
    assert claim_errors(bad, experiences, concepts, texts)
    bad = deepcopy(claims["ma6018:spiral-grid-result"]); del bad["result"]["unit"]
    assert claim_errors(bad, experiences, concepts, texts)
    bad = deepcopy(claims["tum-approximate-dynamic-programming:bellman-policy-operator"]); bad.update(kind="implementation", actor="user")
    assert claim_errors(bad, experiences, concepts, texts)
    bad = deepcopy(claims["ma3001:neumann-inversion"]); bad["references"][0]["section"] = "Nonexistent section"
    assert claim_errors(bad, experiences, concepts, texts)
    assert competency_errors({"evidence_refs": ["ma8102:dlr-nlr-mae"]}, claims)
    try:
        parse("id: one\nid: two\n")
        raise AssertionError("Duplicate YAML key was not rejected")
    except ValueError:
        pass
    checks = {
        "1 Mathematical formulation": "\\sum" in (KB / "concepts/neumann-series.md").read_text() and claims["ma3001:neumann-inversion"]["actor"] == "not_applicable",
        "2 Personal implementation": claims["ma8102:seed-target-alignment"]["actor"] == "user" and "index_select" in claims["ma8102:seed-target-alignment"]["statement"],
        "3 Qualified result": [v["value"] for v in claims["ma6018:spiral-grid-result"]["result"]["values"]] == [47, 78] and all(v["denominator"] == 121 for v in claims["ma6018:spiral-grid-result"]["result"]["values"]) and "12 mm" in " ".join(claims["ma6018:spiral-grid-result"]["limitations"]),
        "4 Analytical competency": "ma6018:impedance-formulation" in caps["impedance-aware-control-design"]["evidence_refs"] and claims["ma6018:impedance-formulation"]["kind"] == "contribution",
        "5 Supplementary knowledge": experiences["tum-approximate-dynamic-programming"]["academic_credit"] == "not_established" and claims["tum-approximate-dynamic-programming:projected-policy-evaluation"]["kind"] == "knowledge",
        "6 Cross-domain distinction": len(concepts["projected-policy-evaluation"]["domains"]) > 1 and {"type": "related_to", "target": "projected-policy-evaluation"} in concepts["hilbert-projection"]["relations"],
    }
    for label, passed in checks.items():
        print(f"Retrieval {label}: {'PASS' if passed else 'FAIL'}")
    assert all(checks.values())
    print(f"OK: {len(experiences)} experiences; {len(concepts)} concepts; {len(claims)} claims; {len(caps)} competencies")
    print("Claim kinds:", dict(Counter(c["kind"] for c in claims.values())))
    print("Coverage:", dict(Counter(s["disposition"] for r in coverage for s in r["sections"])))
    print("Six invalid-input safety checks passed. Structural/retrieval checks are not independent experiment verification.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as exc:
        print(f"Knowledge-base validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
