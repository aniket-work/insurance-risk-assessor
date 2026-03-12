from PIL import Image, ImageDraw, ImageFont
import os

WIDTH = 800
HEIGHT = 500
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (240, 240, 240)
HIGHLIGHT = (80, 200, 120)
WARNING = (239, 68, 68)

def create_mac_window(draw):
    draw.rounded_rectangle([(10, 10), (WIDTH-10, HEIGHT-10)], fill=BG_COLOR, outline=(60, 60, 60), width=2, radius=10)
    # Mac buttons
    draw.ellipse([(20, 20), (32, 32)], fill=(255, 95, 86))  # Red
    draw.ellipse([(40, 20), (52, 32)], fill=(255, 189, 46)) # Yellow
    draw.ellipse([(60, 20), (72, 32)], fill=(39, 201, 63))  # Green
    draw.text((WIDTH//2 - 50, 18), "bash - main.py", fill=(150, 150, 150))
    draw.line([(10, 45), (WIDTH-10, 45)], fill=(60, 60, 60), width=1)

def generate_gif():
    os.makedirs("images", exist_ok=True)
    frames = []
    
    try:
        font = ImageFont.truetype("Courier", 16)
        bold_font = ImageFont.truetype("Courier-Bold", 16)
    except:
        font = ImageFont.load_default()
        bold_font = font
    
    # Typing animation
    command = "$ python main.py"
    for i in range(len(command) + 1):
        img = Image.new('RGB', (WIDTH, HEIGHT), (15, 15, 15))
        draw = ImageDraw.Draw(img)
        create_mac_window(draw)
        
        draw.text((30, 60), command[:i], font=font, fill=TEXT_COLOR)
        if i % 2 == 0: # Blinking cursor
            draw.rectangle([(30 + i*10, 60), (40 + i*10, 75)], fill=TEXT_COLOR)
        frames.append(img)
        
    # Execution Pause
    for _ in range(5):
        img = Image.new('RGB', (WIDTH, HEIGHT), (15, 15, 15))
        draw = ImageDraw.Draw(img)
        create_mac_window(draw)
        draw.text((30, 60), command, font=font, fill=TEXT_COLOR)
        frames.append(img)

    # Process logs
    logs = [
        "[1] Processing Claim: CLM-2026-X99 - Amount: $12500",
        "[2] Generating Independent Reasoning Paths (Self-Consistency)...",
        "    - Path 1: Focusing on medical_history. Calculated Risk Score: 0.61.",
        "    - Path 2: Focusing on time_of_reporting. Calculated Risk Score: 0.72.",
        "    - Path 3: Focusing on claim_amount. Calculated Risk Score: 0.45.",
        "    - Path 4: Focusing on time_of_reporting. Calculated Risk Score: 0.81.",
        "    - Path 5: Focusing on provider_reputation. Calculated Risk Score: 0.39.",
        "\n[3] Synthesizing Consensus...",
        "    Consensus Decision: FLAG FOR MANUAL REVIEW",
        "    Consistency Agreement: 60%",
        "\n[4] Engaging Internal Critic Review...",
        "    ! CRITIQUE: Critic Note: Disagreement in initial reasoning paths indicates underlying ambiguity.",
        "    ! CRITIQUE: Critic Note: Auto-approving high-value claim ($10k+) without secondary documentation check.",
        "\n[5] Estimating Overall Uncertainty..."
    ]
    
    current_logs = [command]
    y_offset = 60
    
    for log in logs:
        current_logs.append(log)
        img = Image.new('RGB', (WIDTH, HEIGHT), (15, 15, 15))
        draw = ImageDraw.Draw(img)
        create_mac_window(draw)
        
        y = 60
        for l in current_logs:
            color = TEXT_COLOR
            if "FLAG" in l or "!" in l: color = WARNING
            elif "Consensus Decision" in l: color = HIGHLIGHT
            draw.text((30, y), l, font=font, fill=color)
            y += 20
        frames.append(img)
        frames.append(img) # Hold frame slightly

    # ASCII Output
    img = Image.new('RGB', (WIDTH, HEIGHT), (15, 15, 15))
    draw = ImageDraw.Draw(img)
    create_mac_window(draw)
    y = 60
    for l in current_logs[-4:]: # Show last few logs
        draw.text((30, y), l, font=font, fill=TEXT_COLOR)
        y += 20
        
    ascii_table = [
        "==================================================",
        "FINAL RISK ASSESSMENT REPORT",
        "==================================================",
        "{",
        '  "Claim ID": "CLM-2026-X99",',
        '  "Initial Consensus": "FLAG FOR MANUAL REVIEW",',
        '  "Final Decision": "FLAG FOR MANUAL REVIEW",',
        '  "Confidence Score": "15.0%",',
        '  "Requires Human Adjucator": true',
        "}",
        "=================================================="
    ]
    
    for line in ascii_table:
        color = WARNING if "FLAG" in line or "15" in line or "true" in line else HIGHLIGHT
        if "====" in line or "{" in line or "}" in line: color = TEXT_COLOR
        draw.text((30, y), line, font=font, fill=color)
        y += 20
    
    for _ in range(15): # Hold ASCII table
        frames.append(img)

    # UI Transition
    ui_bg = (250, 250, 252)
    img_ui = Image.new('RGB', (WIDTH, HEIGHT), ui_bg)
    draw_ui = ImageDraw.Draw(img_ui)
    
    # Premium UI Card
    draw_ui.rounded_rectangle([(50, 50), (WIDTH-50, HEIGHT-50)], fill=(255, 255, 255), outline=(220, 220, 220), width=2, radius=15)
    
    # Header
    draw_ui.text((80, 80), "Risk Assessor Dashboard", fill=(40, 40, 40), font=bold_font)
    draw_ui.line([(80, 110), (WIDTH-80, 110)], fill=(230, 230, 230), width=2)
    
    # Claim Details
    draw_ui.text((80, 130), "Claim ID: CLM-2026-X99", fill=(100, 100, 100), font=font)
    draw_ui.text((80, 160), "Value: $12,500 | Type: Auto Collision", fill=(100, 100, 100), font=font)
    
    # Risk Score Widget
    draw_ui.rounded_rectangle([(80, 200), (380, 380)], fill=(255, 245, 245), outline=(255, 200, 200), width=1, radius=10)
    draw_ui.text((100, 220), "Overall Confidence", fill=(150, 50, 50), font=font)
    draw_ui.text((100, 260), "15.0%", fill=(220, 38, 38), font=bold_font)
    draw_ui.text((100, 310), "Status: MANUAL REVIEW REQ.", fill=(220, 38, 38), font=font)

    # Critic Insights Widget
    draw_ui.rounded_rectangle([(400, 200), (720, 380)], fill=(249, 250, 251), outline=(230, 230, 230), width=1, radius=10)
    draw_ui.text((420, 220), "Critic Insights", fill=(80, 80, 80), font=font)
    draw_ui.text((420, 260), "- Disagreement in paths", fill=(100, 100, 100), font=font)
    draw_ui.text((420, 290), "- High-value without docs", fill=(100, 100, 100), font=font)
    draw_ui.text((420, 340), "Severity: High", fill=(202, 138, 4), font=bold_font)

    for _ in range(20): # Hold UI frame
        frames.append(img_ui)

    # MANDATORY: P-Mode Conversion with Global Palette
    print("Optimizing GIF with global palette (P-Mode)...")
    sample = Image.new("RGB", (WIDTH, HEIGHT * 3))
    sample.paste(frames[0], (0,0))
    sample.paste(frames[len(frames)//2], (0,HEIGHT))
    sample.paste(frames[-1], (0,HEIGHT*2))
    palette = sample.quantize(colors=256, method=2)
    
    final_frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    output_path = "images/title-animation.gif"
    final_frames[0].save(output_path, save_all=True, append_images=final_frames[1:], optimize=True, loop=0, duration=100)
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    generate_gif()
