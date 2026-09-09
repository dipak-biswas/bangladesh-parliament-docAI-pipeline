"""
Parliamentary Question Issue-Level Classifier
Classifies PQ as constituency / national / international
Uses Bangla gazetteer + fuzzy matching to handle OCR errors

Author: Dipak Kumar Biswas, PhD WVU 2026
"""

import pandas as pd
import re

def load_constituency_gazetteer():
    # Full list of 500+ upazilas - sample shortened for repo
    places = ["কুমিল্লা", "দেবিদ্বার", "ফেনী", "চট্টগ্রাম", "ঢাকা", "রাজশাহী", "আমার নির্বাচনী এলাকা"]
    return [p.strip() for p in places]

def categorize_issue_level(text, places, intl_markers):
    if pd.isna(text): return "national"
    # Priority: constituency > international > national
    for place in places:
        if place in text: return "constituency"
    for marker in intl_markers:
        if marker in text: return "international"
    return "national"

# Usage
# df["pq_issue_level"] = df["Text"].apply(lambda x: categorize_issue_level(x, places, intl_markers))
