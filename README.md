# EthioMart-NER

This project focuses on **fine-tuning a Named Entity Recognition (NER) system for Amharic text** to extract key business entities such as **product names, prices, and locations** from Ethiopian e-commerce Telegram channels. The extracted data will be used to build a centralized marketplace, **EthioMart**, consolidating product listings from multiple Telegram vendors.

---

## Project Structure

```plaintext

EthioMart-NER/
├── .github/
│   └── workflows/
│       ├── ci.yml                      # GitHub Actions CI/CD pipeline configuration
├── data/
│   ├── raw/                            # Raw data collected from Telegram
│   ├── processed/                       # Preprocessed and labeled data
│   ├── conll/                          # Labeled data in CoNLL format for model training
├── notebooks/
│   ├── 01_Data_Ingestion.ipynb         # Data scraping and Telegram message collection
│   ├── 02_Data_Preprocessing.ipynb     # Cleaning, tokenization, and formatting
│   ├── 03_NER_Finetuning.ipynb         # Fine-tuning NER models
│   ├── 04_Model_Evaluation.ipynb       # Model comparison and performance analysis
│   ├── 05_Model_Interpretability.ipynb # SHAP & LIME explanations
├── scripts/
│   ├── data_ingestion.py               # Fetches messages from Telegram channels
│   ├── data_preprocessing.py           # Tokenization and text normalization
│   ├── labeling.py                      # Converts labeled data into CoNLL format
│   ├── ner_training.py                  # Fine-tunes NER models
│   ├── model_evaluation.py              # Compares multiple models
│   ├── interpretability.py              # Model interpretability with SHAP/LIME
├── models/
│   ├── trained_models/                  # Saved fine-tuned models
│   ├── results/                         # Model performance reports
├── tests/
│   ├── test_data_preprocessing.py       # Unit tests for preprocessing functions
│   ├── test_ner_training.py             # Unit tests for model training pipeline
├── .gitignore                           # Ignore unnecessary files and directories
├── README.md                            # Project overview and setup guide
├── requirements.txt                     # Python dependencies
├── dvc.yaml                             # DVC pipeline for dataset versioning
├── .env                                 # Environment variables (Telegram API credentials)
└── LICENSE                              # License information
<!-- 

```
## Script Functionalities
data_ingestion.py: Scrapes messages from Ethiopian e-commerce Telegram channels and stores raw data in a structured format.

**data_preprocessing.py:** Tokenizes Amharic text, normalizes words, and structures data for entity extraction.

**labeling.py:** Converts a manually labeled dataset into the CoNLL format for Named Entity Recognition (NER) training.

**ner_training.py:** Fine-tunes transformer-based NER models (e.g., BERT, XLM-Roberta, AfroXLMR) on the labeled dataset.

**model_evaluation.py:** Compares multiple fine-tuned models based on F1-score, precision, recall, and execution speed.

**interpretability.py:** Uses SHAP & LIME to interpret the predictions of the NER models and identify biases.

## Commit Message Guidelines
To maintain a clear and well-organized repository, follow these commit message guidelines:

**Use the imperative mood:** "Fix data preprocessing bug" instead of "Fixed data preprocessing bug".
** Be concise and descriptive:** Example: "Add Telegram data ingestion script (#Task1)".
Reference tasks where applicable (e.g., #Task1, #Task2).
Example:

```plaintext
git commit -m "Implement text normalization in preprocessing script (#Task1)"

```
## Usage
This project provides scripts and notebooks to streamline the NER fine-tuning process for Amharic e-commerce messages.

### Set Up the Environment

```plaintext

# Clone the repository
git clone https://github.com/beckhamberhanu/Amharic-NER-Telegram.git
cd Amharic-NER-Telegram

// Create and activate a virtual environment (recommended)
python3 -m venv env
source ner_env/bin/activate   # For Mac/Linux

// Install required dependencies
pip install -r requirements.txt
2️⃣ Configure Environment Variables
Create a .env file and add your Telegram API credentials:

API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=your_phone_number

3️⃣ Running the Pipeline
Step 1: Data Ingestion

python scripts/data_ingestion.py
Fetches messages from Telegram channels and stores them in /data/raw/.

Step 2: Data Preprocessing

python scripts/data_preprocessing.py
Cleans and tokenizes text, then saves structured data in /data/processed/.

Step 3: Annotate & Label Data

python scripts/labeling.py
Converts labeled messages into CoNLL format for training.

Step 4: Train NER Model

python scripts/ner_training.py
Fine-tunes XLM-Roberta, mBERT, AfroXLMR, or DistilBERT models.

Step 5: Evaluate Model Performance

python scripts/model_evaluation.py
Compares models based on F1-score, precision, recall.

Step 6: Interpret Model Predictions

python scripts/interpretability.py
Uses SHAP & LIME to analyze NER decisions. -->