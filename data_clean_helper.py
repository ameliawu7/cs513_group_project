import pandas as pd
import re

def clean_str_col(text):
    """ General string cleaning function for short phrases type of columns e.g. noun-like columns """
    if pd.isnull(text):
        return text

    # All lowercase
    text = str(text).lower().strip()
    
    # Remove unwanted syntaxes
    text = re.sub(r'[\[\]\(\)\'"“”\\\?.,;:!@#$%^&*_+=<>|`~]', '', text)
                  
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing dashes
    text = text.strip('-–—')
    
    text = text.strip()
    return text


# Kept semicolon version of text clean
def clean_notes(text):
    """ General string cleaning function for short phrases type of columns e.g. noun-like columns """
    if pd.isnull(text):
        return text

    # All lowercase
    text = str(text).lower().strip()
    
    # Remove unwanted syntaxes
    text = re.sub(r'[\[\]\(\)\'"“”\\\?.,:!@#$%^&*_+=<>|`~]', '', text)
                  
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing dashes
    text = text.strip('-–—')
    
    text = text.strip()
    return text

def clean_str_col(text):
    """ General string cleaning function for short phrases type of columns e.g. noun-like columns """
    if pd.isnull(text):
        return text

    # All lowercase
    text = str(text).lower().strip()
    
    # Remove unwanted syntaxes
    text = re.sub(r'[\[\]\(\)\'"“”\\\?.,;:!@#$%^&*_+=<>|`~]', '', text)
                  
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing dashes
    text = text.strip('-–—')
    
    text = text.strip()
    return text



# Function to check if datetime is timezone-aware and in UTC
def is_not_utc(dt):
    if pd.isnull(dt):
        return False
    if dt.tzinfo is None:
        return True  # Naive datetime, so not UTC
    return dt.tzinfo.zone != 'UTC'


    
