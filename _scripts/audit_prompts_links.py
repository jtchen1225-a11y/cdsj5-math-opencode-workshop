#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit all href attributes in prompts.html to ensure complete isolation.
"""
import re

with open("prompts.html", "r", encoding="utf-8") as f:
    content = f.read()

links = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\']', content, re.IGNORECASE)
print(f"Total <a> links found in prompts.html: {len(links)}")
for idx, l in enumerate(links, 1):
    print(f"[{idx:02d}] {l}")
