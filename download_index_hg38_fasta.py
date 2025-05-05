# download_index_hg38_fasta.py

"""
This script downloads the hg38 reference genome (FASTA format) from UCSC and creates an index (.fai) using samtools.

Make sure you have 'wget' and 'samtools' installed before running this script.
"""

import os
import subprocess

# Define the URL and filename
url = "http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz"
fasta_gz = "hg38.fa.gz"
fasta = "hg38.fa"

# Step 1: Download the compressed FASTA file
print("🔽 Downloading hg38.fa.gz from UCSC...")
subprocess.run(["wget", url])

# Step 2: Unzip the FASTA file
print("📦 Unzipping hg38.fa.gz...")
subprocess.run(["gunzip", fasta_gz])

# Step 3: Index the FASTA using samtools
print("🔧 Indexing FASTA file with samtools...")
subprocess.run(["samtools", "faidx", fasta])

print("✅ Download and indexing completed.")
