# bangladesh-parliament-docAI-pipeline
End-to-end pipeline to digitize Bangladesh parliamentary records using Google Document AI + Python + LLM classification to extract information and build a dataset on legislators, legislative politics

# Bangladesh Parliament: Document AI Pipeline for Low-Resource Archives
### From Physical Archives to Structured Dataset (70k+ records)

Built the first machine-readable dataset of Bangladesh Parliament by digitizing in-person printed archives into structured data using Google Document AI + Python.

**Challenge:** No digital records existed. Data only available as printed books in Bangladesh Parliament Library (in-person access). Scans were low-quality, mixed Bangla/English, non-standard layouts.

**My End-to-End Pipeline (Field-to-Dataset):**

**Phase 1: Field Collection & Digitization**
- Collected 100k+ pages via in-person archival photography at Bangladesh Parliament Library
- Converted photos to searchable PDFs using Adobe Scan (de-skew, contrast enhancement)

**Phase 2: OCR & Extraction**
- OCR with **Google Cloud Document AI** (Document OCR Processor) optimized for low-resource Bangla/English mix
- Exported raw output to JSON with bounding boxes, confidence scores, and layout metadata

**Phase 3: Data Cleaning & Structuring**
- Cleaned JSON with **Python (pandas, json)** - removed low-confidence tokens (<0.8), fixed line-break artifacts
- Converted to `.txt` and standardized using **regex** to normalize date formats, legislator names, question numbers
- Built fuzzy-matching dictionary to fix 15k+ OCR errors (e.g., Bengali transliteration variants)

**Phase 4: Variable Construction**
- Parsed structured `.txt` files to extract variables: legislator, date, ministry, topic, question type
- Applied LLM-assisted classification + human validation (87% agreement)
- Exported final dataset to CSV/SQL for statistical analysis (R, Stata)

**Tech Stack:** Google Document AI, Python, Adobe Scan API, Regex, pandas, SQL, JSON, LLM Classification

**Impact:** 90% reduction in manual coding, reusable framework for any low-resource language archive. Methodology published in *Legislative Studies Quarterly* (2026).

**Author:** Dipak Kumar Biswas, PhD Political Science WVU 2026 | db0127@mix.wvu.edu
