#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Workshop Site Verification Script
Checks all 4 HTML files for required assets, short URLs, educational motto badges,
deck modal integrity, and internal link health.
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = ["index.html", "workshop-flow.html", "prompts.html", "troubleshooting.html"]

REQUIRED_SHORT_URLS = [
    "https://www.daydaystudy.top/cdsj5",
    "https://www.daydaystudy.top/prompt"
]

REQUIRED_MOTTO_PHRASES = [
    "AI 時代守本心，毅誠勤樸篤前行",
    "AI 負責流程加速，教師專注教學判斷、算理本質與關懷學生"
]

def check_file(filename):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        return False, f"Missing file: {filename}"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    errors = []
    
    # 1. Check Deck Modal
    if 'id="deck-modal"' not in content:
        errors.append("Missing id='deck-modal'")
    if 'toggleBlackboard' not in content:
        errors.append("Missing toggleBlackboard function")
    
    # 2. Check 12 slides data
    for i in range(1, 13):
        slide_id = f"P{i:02d}"
        if slide_id not in content:
            errors.append(f"Missing slide ID: {slide_id}")
            
    # 3. Check Motto in main pages
    for phrase in REQUIRED_MOTTO_PHRASES:
        if phrase not in content:
            errors.append(f"Missing motto phrase: {phrase}")
            
    # 4. Check Short URLs in index.html and prompts.html
    if filename in ["index.html", "prompts.html"]:
        for url in REQUIRED_SHORT_URLS:
            if url not in content:
                errors.append(f"Missing required short URL: {url}")
                
    # 5. Check copyShortUrl function
    if filename in ["index.html", "prompts.html", "workshop-flow.html", "troubleshooting.html"]:
        if "copyShortUrl" not in content:
            errors.append("Missing copyShortUrl function in script")
            
    # 6. Check internal navigation links
    for target in HTML_FILES:
        if f'href="{target}"' not in content and filename != target:
            errors.append(f"Missing internal link to: {target}")

    if errors:
        return False, f"{filename} errors:\n  - " + "\n  - ".join(errors)
    return True, f"{filename} passed all checks."

def main():
    print("=" * 60)
    print(" CDSJ5 Math Workshop Site Verification")
    print("=" * 60)
    
    all_passed = True
    for f in HTML_FILES:
        ok, msg = check_file(f)
        if ok:
            print(f"[PASS] {msg}")
        else:
            print(f"[FAIL] {msg}")
            all_passed = False
            
    print("=" * 60)
    if all_passed:
        print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY.")
        sys.exit(0)
    else:
        print("SOME CHECKS FAILED. Please review output.")
        sys.exit(1)

if __name__ == "__main__":
    main()
