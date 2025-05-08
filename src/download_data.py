# src/download_data.py

import os
import requests
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def download_file(url, out_path):
    if out_path.exists():
        print(f"[✓] Already downloaded: {out_path.name}")
        return
    print(f"Downloading: {out_path.name}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"[✓] Done: {out_path.name}")

# --- gnomAD exome variant summary (TSV) ---
gnomad_url = "https://storage.googleapis.com/gnomad-public/release/3.1.2/ht/exomes/gnomad.exomes.r3.1.2.sites.summary.tsv.bgz"
gnomad_path = RAW_DIR / "gnomad.exomes.r3.1.2.sites.summary.tsv.bgz"

# --- ClinVar summary (optional, evaluation only) ---
clinvar_url = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz"
clinvar_path = RAW_DIR / "variant_summary.txt.gz"

# --- UniProt human proteins (FASTA) ---
uniprot_url = "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot_human.fasta.gz"
uniprot_path = RAW_DIR / "uniprot_sprot_human.fasta.gz"

# --- Download all ---
download_file(gnomad_url, gnomad_path)
download_file(clinvar_url, clinvar_path)
download_file(uniprot_url, uniprot_path)
