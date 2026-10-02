#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Workshop Site Verification Script
Checks all 4 HTML files for required assets, short URLs, educational motto badges,
deck modal integrity, zero scrollbar architecture, and isolation of prompts.html.
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
    
    # Check Motto phrases in all pages
    for phrase in REQUIRED_MOTTO_PHRASES:
        if phrase not in content:
            errors.append(f"Missing motto phrase: {phrase}")
            
    # Check copyShortUrl function
    if "copyShortUrl" not in content:
        errors.append("Missing copyShortUrl function in script")

    # SPECIFIC CHECKS FOR prompts.html (ISOLATED STUDENT WORKBENCH)
    if filename == "prompts.html":
        # Must have prompt short URL
        if "https://www.daydaystudy.top/prompt" not in content:
            errors.append("Missing student short URL: https://www.daydaystudy.top/prompt")
            
        # Must NOT have deck-modal or slides
        if 'id="deck-modal"' in content:
            errors.append("prompts.html must NOT contain id='deck-modal' (should be isolated from chalkboard presentation)")
        if 'slidesData' in content:
            errors.append("prompts.html must NOT contain slidesData")
            
        # Must NOT link to other pages
        other_pages = ["index.html", "workshop-flow.html", "troubleshooting.html"]
        for p in other_pages:
            if f'href="{p}"' in content or f"href='{p}'" in content:
                errors.append(f"prompts.html must be isolated, but links to {p}")
                
        # Must contain copyPrompt
        if "copyPrompt" not in content:
            errors.append("Missing copyPrompt function in prompts.html")
            
    # SPECIFIC CHECKS FOR PRESENTATION PAGES (index, workshop-flow, troubleshooting)
    else:
        # Check Deck Modal
        if 'id="deck-modal"' not in content:
            errors.append("Missing id='deck-modal'")
        if 'toggleBlackboard' not in content:
            errors.append("Missing toggleBlackboard function")
        
        # Check 12 slides data
        for i in range(1, 13):
            slide_id = f"P{i:02d}"
            if slide_id not in content:
                errors.append(f"Missing slide ID: {slide_id}")
                
        # Check Zero Scrollbar CSS requirements
        if ".deck-slide-card" not in content or "overflow: hidden !important" not in content:
            errors.append("Missing overflow: hidden !important in deck modal CSS")
        if "#deck-slide-content" not in content:
            errors.append("Missing #deck-slide-content flex styling in deck modal CSS")
        if "@media (max-height: 780px)" not in content:
            errors.append("Missing @media (max-height: 780px) responsive adaptation")

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
