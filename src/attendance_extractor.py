"""
Session Attendance Extractor from Bangla Bulletins
Extracts MP attendance using Bengali numerals (০-৯)
Pattern: (১ to (৩৫০ and সর্বজনাব... উপস্থিত ছিলেন না
"""
import re
BN_DIGITS = '০১২৩৪৫৬৭৮৯'
def to_bn(n: int) -> str:
    return ''.join(BN_DIGITS[int(d)] for d in str(n))

MEMBERS = [f"({to_bn(i)} " for i in range(1, 351)]

def extract_attendance(text):
    counts = {}
    for i, token in enumerate(MEMBERS, 1):
        counts[i] = text.count(token)
    return counts
