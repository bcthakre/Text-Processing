# Text Preprocessing README

This repository contains a Python module for text preprocessing. The module provides sequential text preprocessing, covering the following steps:

1. Lowercasing
2. Punctuation Removal
3. Trim Whitespace
4. NFKD Normalization
5. Strip Accents
6. Lemmatization
7. Stemming

## Flowchart of the Preprocessing Steps

```mermaid
graph TD
    A[Input Sentence]
    B[Lowercasing]
    C[Punctuation Removal]
    D[Trim Whitespace]
    E[NFKD Normalization]
    F[Strip Accents]
    G[Lemmatization]
    H[Stemming]
    I[Processed Sentence]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I

