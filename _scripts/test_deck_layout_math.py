#!/usr/bin/env python3
# -*- coding: utf-8 -*-

resolutions = [
    ("768p Laptop / Projector", 1366, 768),
    ("800p Projector", 1280, 800),
    ("900p Display", 1600, 900),
    ("1080p Standard", 1920, 1080),
    ("1440p 2K Display", 2560, 1440)
]

def clamp(val, min_v, max_v):
    return max(min_v, min(val, max_v))

def test_resolution(name, w, h):
    vh = h / 100.0
    vw = w / 100.0
    container_h = h * 0.96
    
    if h <= 780:
        topbar_p = 6 * 2
        topbar_content = 28
        topbar_h = topbar_p + topbar_content # 40px
        
        bottombar_p = 5 * 2
        bottombar_content = 18
        bottombar_h = bottombar_p + bottombar_content # 28px
        
        main_p = 8 * 2 # 16px
        card_p = 10 * 2 # 20px
        
        avail_card_h = container_h - topbar_h - bottombar_h - main_p - card_p
        
        title_font = clamp(2.8 * vh, 1.45 * 16, 1.8 * 16)
        title_h = title_font * 1.25 + 6
        
        desc_font = clamp(1.8 * vh, 1.05 * 16, 1.25 * 16)
        desc_h = desc_font * 1.45 + 8
        
        callout_font = clamp(1.8 * vh, 1.0 * 16, 1.18 * 16)
        callout_h = callout_font * 1.45 + 16
        
        gap_total = 6 * 4 # 24px
        remaining_for_list = avail_card_h - title_h - desc_h - callout_h - 8
        li_h = (remaining_for_list - gap_total) / 5.0
        
        li_font = clamp(2.0 * vh, 1.08 * 16, 1.25 * 16)
        needed_li_h = li_font * 1.45 + 14
        
    else:
        topbar_p = clamp(1.2 * vh, 8, 12) * 2
        topbar_content = clamp(1.3 * vh, 24, 30)
        topbar_h = topbar_p + topbar_content
        
        bottombar_p = clamp(1.0 * vh, 6, 10) * 2
        bottombar_content = clamp(1.2 * vh, 18, 22)
        bottombar_h = bottombar_p + bottombar_content
        
        main_p = clamp(1.3 * vh, 10, 16) * 2
        card_p = clamp(1.5 * vh, 14, 22) * 2
        
        avail_card_h = container_h - topbar_h - bottombar_h - main_p - card_p
        
        title_font = clamp(3.2 * vh, 1.65 * 16, 2.5 * 16)
        title_h = title_font * 1.25 + clamp(0.6 * vh, 6, 10)
        
        desc_font = clamp(2.0 * vh, 1.1 * 16, 1.4 * 16)
        desc_h = desc_font * 1.45 + clamp(1.0 * vh, 10, 14)
        
        callout_font = clamp(1.95 * vh, 1.05 * 16, 1.3 * 16)
        callout_h = callout_font * 1.45 + clamp(1.3 * vh, 16, 24)
        
        gap_total = clamp(0.8 * vh, 8, 12) * 4
        remaining_for_list = avail_card_h - title_h - desc_h - callout_h - clamp(1.0 * vh, 8, 14)
        li_h = (remaining_for_list - gap_total) / 5.0
        
        li_font = clamp(2.25 * vh, 1.12 * 16, 1.45 * 16)
        needed_li_h = li_font * 1.45 + clamp(1.1 * vh, 16, 24)
        
    margin = li_h - needed_li_h
    print(f"[{name}] H={h}px: AvailCardH={avail_card_h:.1f}px | li_h={li_h:.1f}px vs needed={needed_li_h:.1f}px | Margin={margin:+.1f}px | li_font={li_font:.1f}px ({li_font/16:.2f}rem) | title_font={title_font:.1f}px")
    return margin >= 0

all_ok = True
for name, w, h in resolutions:
    ok = test_resolution(name, w, h)
    if not ok: all_ok = False

print(f"\nOverall Layout Test: {'PASS' if all_ok else 'FAIL'}")
