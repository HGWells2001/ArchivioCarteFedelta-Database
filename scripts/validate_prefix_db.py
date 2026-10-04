#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

DB = Path("data/loyalty_prefixes.json")

def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

if not DB.is_file():
    fail(f"{DB} non trovato")

try:
    data = json.loads(DB.read_text(encoding="utf-8"))
except Exception as exc:
    fail(f"JSON non valido: {exc}")

if not isinstance(data, dict):
    fail("la radice deve essere un oggetto JSON")

if not isinstance(data.get("schemaVersion"), int) or data["schemaVersion"] < 1:
    fail("schemaVersion deve essere un intero >= 1")

prefixes = data.get("prefixes")
if not isinstance(prefixes, dict):
    fail("prefixes deve essere un oggetto JSON")

for prefix, record in prefixes.items():
    if not isinstance(prefix, str) or not re.fullmatch(r"[0-9A-Z]+", prefix):
        fail(f"prefisso non valido: {prefix!r}. Ammesse solo cifre/lettere maiuscole")
    if not isinstance(record, dict):
        fail(f"{prefix}: la regola deve essere un oggetto")
    name = record.get("name")
    if not isinstance(name, str) or not name.strip():
        fail(f"{prefix}: name mancante")
    logo = record.get("logo", "")
    if logo and (not isinstance(logo, str) or not logo.startswith("https://")):
        fail(f"{prefix}: logo deve usare HTTPS")
    category = record.get("category", "")
    if category and not isinstance(category, str):
        fail(f"{prefix}: category non valida")
    front_image = record.get("frontImage", "")
    if front_image and (not isinstance(front_image, str) or not front_image.startswith("https://")):
        fail(f"{prefix}: frontImage deve usare HTTPS")

print(f"OK: {len(prefixes)} regole, schema {data['schemaVersion']}")
