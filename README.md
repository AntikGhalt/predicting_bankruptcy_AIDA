# Bankruptcy Prediction Notebook

This repository contains a single Jupyter notebook used to aggregate and clean AIDA export files in order to study bankruptcy-related events.  The notebook was written for Google Colab and expects the input files to reside in Google Drive.

## Directory Structure

The notebook expects the following directories on your Google Drive:

```
MyDrive/SETUP DEFINITIVO/Temporaneo, lezioni ML/AIDA/
├── DATA/
│   └── model_test/            # Excel input files and processed data
└── output/
    └── model_test/            # Generated models and intermediate outputs
```

`model_test` is the default folder name configured inside the notebook.  If you change the variable `model_folder` at the top of the notebook, ensure that both `DATA` and `output` contain a subdirectory with the same name.

Place the Excel files listed in the notebook (e.g. `Aida_Export_TESTin_0_1000.xlsx`, `Aida_Export_testD_001_200.xlsx`, …) inside `DATA/model_test/`.

## Purpose

`AIDA_2_TEST2.ipynb` loads multiple AIDA export files, parses date columns, merges them into a single dataframe and generates several indicators for bankruptcy analysis.  The final dataframe is saved as a pickle file for subsequent modelling steps.

## Usage

1. Open the notebook in Google Colab, ensuring your Google Drive is mounted.
2. Verify the `path_data` and `path_MODEL` variables at the top match your Drive structure.
3. Run the cells sequentially to generate the processed dataset and analysis.

### Running as a script

If you prefer to execute the notebook programmatically, you can convert it to a script with:

```bash
jupyter nbconvert --to script AIDA_2_TEST2.ipynb
python AIDA_2_TEST2.py
```

The script assumes the same directory structure as the notebook.

