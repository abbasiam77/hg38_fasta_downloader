# hg38 Reference Genome Downloader and Indexer

This repository contains a Python script to download the hg38 reference genome (FASTA format) from UCSC and index it using samtools.

## Prerequisites

Make sure you have the following tools installed on your system:

- `wget` for downloading the FASTA file from UCSC
- `gunzip` for decompressing the downloaded file
- `samtools` for indexing the FASTA file

## Usage

To use the script, simply run:

```bash
python download_index_hg38_fasta.py
