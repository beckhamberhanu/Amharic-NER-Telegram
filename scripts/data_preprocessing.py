import pandas as pd
import re
import nltk
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize

# Load data
df = pd.read_csv("data/raw_messages.csv")

# Function to clean Amharic text
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"\d+", "", text)  # Remove numbers
    text = re.sub(r"[^\w\s፡።፣፤፥፦፧]", "", text)  # Remove punctuation except Amharic ones
    text = text.strip()
    return text

# Function to tokenize text
def tokenize_text(text):
    return " ".join(word_tokenize(text))

# Apply cleaning and tokenization
df["Cleaned_Text"] = df["Text"].apply(clean_text)
df["Tokenized_Text"] = df["Cleaned_Text"].apply(tokenize_text)

# Save preprocessed data
df.to_csv("data/preprocessed_messages.csv", index=False)
print("✅ Preprocessed data saved to data/preprocessed_messages.csv")