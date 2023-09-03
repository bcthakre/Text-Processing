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

## Let's integrate Kaggle. 
# How fun it will be to see all the methods we created earlier 
# to apply on the real life dataset

Some changes were made to the earlier created file to 
use it with pandas dataframe.

This guide provides a step-by-step process to integrate the Kaggle API with Python to access various Kaggle functionalities programmatically.

## Table of Contents
1. [Setting Up Kaggle API](#setting-up-kaggle-api)
2. [Available Methods](#available-methods)
3. [Flow Diagram](#flow-diagram)
4. [Troubleshooting](#troubleshooting)

---

## Setting Up Kaggle API

1. **API Token**:
    - Go to your Kaggle account settings page.
    - Find the API section and click on `Create New API Token`.
    - This will download a `kaggle.json` file, which contains your API token.
    
2. **Setup in Python**:
    - Install the Kaggle Python package: 
    ```bash
    pip install kaggle
    ```
    - Place the `kaggle.json` in the directory `~/.kaggle/`.
    - This folder is hidden and you won't see it

3. ** Apply restriction to kaggle.json file

    - Since the Kaggle.json contains the key , you may want to apply restrictions.
    ```
    bash

    chmod 600 ~/.kaggle/kaggle.json
    ```
    
4. **Initialization**:
    ```python
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    ```

---

## Available Methods

### Datasets

1. `api.dataset_list()`: Lists available datasets.
2. `api.dataset_download_files(dataset, path, unzip)`: Downloads specified dataset files.

### Competitions

1. `api.competitions_list()`: Lists all available competitions.
2. `api.competition_submit(file_name, message, competition)`: Submits a solution to a competition.
3. `api.competition_leaderboard_view(competition)`: Fetches the leaderboard for a specific competition.

---

## Flow Diagram

![Kaggle Integration](/Users/bhupendrasinhthakre/Documents/Python/text-preprocessing/kaggleIntegration.png)
