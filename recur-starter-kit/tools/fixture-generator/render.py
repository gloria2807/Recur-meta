import random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

F = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
DJ = "/usr/share/fonts/truetype/dejavu/DejaVuSans{}.ttf"
FOOTER = "SAMPLE IMAGE · Recur test data · not a real transaction"


def font(size, weight="Regular", naira=False):
    if naira:  # DejaVu reliably has the naira sign
        return ImageFont.truetype(DJ.format("-Bold" if weight in ("Bold", "SemiBold") else ""), size)
    return ImageFont.truetype(F.format(weight), size)


THEMES = {
    "swiftpay": dict(name="SwiftPay", color="#5B3DF5", bg="#F6F4FF", hero="You sent"),
    "brightline": dict(name="Brightline Bank", color="#0B2A4A", bg="#F3F6FA", hero="Transfer successful"),
    "harborcu": dict(name="Harbor Credit Union", color="#1F6F50", bg="#F2F8F5", hero="ACH payment sent"),
    "lagoon": dict(name="Lagoon Bank", color="#0E7C86", bg="#EFF8F9", hero="Transaction Successful"),
    "paylane": dict(name="Paylane", color="#E25F1B", bg="#FFF5EF", hero="Payment receipt"),
}
STATUS = {
    "completed": ("Completed", "#16A34A"),
    "failed": ("Failed", "#DC2626"),
    "pending": ("Pending", "#D97706"),
    "reversed": ("Reversed", "#6B7280"),
    "requested": ("Request sent", "#2563EB"),
}


def money_text(minor, currency):
    v = minor / 100
    if currency == "NGN":
        return f"₦{v:,.2f}"
    return f"${v:,.2f}"


def screenshot(path, app, amount_minor, currency, rows, status="completed", hero=None, extra_note=None, size=(720, 1440)):
    t = THEMES[app]
    W, H = size
    im = Image.new("RGB", (W, H), t["bg"])
    d = ImageDraw.Draw(im)
    # status bar
    d.text((36, 22), "9:41", font=font(26, "SemiBold"), fill="#111")
    d.text((W - 150, 22), "5G  87%", font=font(24, "Medium"), fill="#111")
    # header
    d.rectangle([0, 72, W, 196], fill=t["color"])
    d.text((36, 108), t["name"], font=font(40, "Bold"), fill="white")
    d.text((W - 90, 112), "×", font=font(44, "Medium"), fill="white")
    # card
    d.rounded_rectangle([28, 228, W - 28, H - 150], radius=32, fill="white")
    label, scol = STATUS[status]
    # status icon
    cx, cy = W // 2, 330
    d.ellipse([cx - 52, cy - 52, cx + 52, cy + 52], fill=scol)
    mark = {"completed": "✓", "failed": "!", "pending": "…", "reversed": "↺", "requested": "→"}[status]
    mf = font(56, "Bold", naira=True)
    bw = d.textlength(mark, font=mf)
    d.text((cx - bw / 2, cy - 36), mark, font=mf, fill="white")
    htxt = hero or (t["hero"] if status == "completed" else label)
    hf = font(34, "SemiBold")
    d.text(((W - d.textlength(htxt, font=hf)) / 2, 404), htxt, font=hf, fill="#111")
    amt = money_text(amount_minor, currency)
    af = font(76, "Bold", naira=currency == "NGN")
    d.text(((W - d.textlength(amt, font=af)) / 2, 458), amt, font=af, fill="#0A0A0A")
    pf = font(26, "SemiBold")
    pw = d.textlength(label, font=pf) + 48
    d.rounded_rectangle([(W - pw) / 2, 568, (W + pw) / 2, 612], radius=22, fill=scol)
    d.text(((W - pw) / 2 + 24, 575), label, font=pf, fill="white")
    y = 660
    kf, vf = font(24, "Medium"), font(27, "SemiBold")
    for k, v in rows:
        d.text((64, y), k, font=kf, fill="#6B7280")
        vfont = font(27, "SemiBold", naira="₦" in v)
        lines = wrap(d, v, vfont, W - 128)
        for i, line in enumerate(lines):
            d.text((64, y + 34 + i * 34), line, font=vfont, fill="#111")
        y += 34 + 34 * len(lines) + 26
        d.line([64, y - 14, W - 64, y - 14], fill="#EEF0F3", width=2)
    if extra_note:
        d.text((64, y + 6), extra_note, font=font(22, "Regular"), fill="#9CA3AF")
    # buttons
    d.rounded_rectangle([64, H - 270, W - 64, H - 190], radius=40, fill=t["color"])
    btxt = "Share receipt"
    d.text(((W - d.textlength(btxt, font=font(30, "SemiBold"))) / 2, H - 250), btxt, font=font(30, "SemiBold"), fill="white")
    ff = font(19, "Medium")
    d.text(((W - d.textlength(FOOTER, font=ff)) / 2, H - 100), FOOTER, font=ff, fill="#9CA3AF")
    im.save(path, optimize=True)
    return im


def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        nxt = (cur + " " + w).strip()
        if d.textlength(nxt, font=f) <= maxw:
            cur = nxt
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines or [""]


def paper_photo(path, title, lines, seed=1):
    """A printed receipt photographed at an angle on a desk."""
    rnd = random.Random(seed)
    pw, ph = 520, 300 + 44 * len(lines)
    paper = Image.new("RGB", (pw, ph), "#FBFAF6")
    d = ImageDraw.Draw(paper)
    mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 22)
    monob = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 26)
    d.text((30, 30), title, font=monob, fill="#222")
    d.text((30, 70), "-" * 34, font=mono, fill="#444")
    y = 110
    for ln in lines:
        d.text((30, y), ln, font=mono, fill="#222"); y += 44
    d.text((30, y + 10), "-" * 34, font=mono, fill="#444")
    d.text((30, y + 50), "SAMPLE · Recur test data", font=mono, fill="#777")
    paper = paper.rotate(rnd.uniform(-9, -4), expand=True, fillcolor=(0, 0, 0, 0), resample=Image.BICUBIC)
    bg = Image.new("RGB", (900, 1200), "#7A5C43")
    bd = ImageDraw.Draw(bg)
    for i in range(0, 1200, 9):  # wood grain
        bd.line([0, i + rnd.randint(-3, 3), 900, i + rnd.randint(-3, 3)], fill=(110 + rnd.randint(-12, 12), 82 + rnd.randint(-10, 10), 58), width=3)
    mask = Image.new("L", paper.size, 0)
    ImageDraw.Draw(mask).rectangle([0, 0, *paper.size], fill=255)
    rot_mask = Image.new("L", (pw, ph), 255).rotate(0)
    bg.paste(paper, (190, 220), paper.convert("L").point(lambda p: 255 if p > 8 else 0))
    # lighting gradient + slight blur and noise like a phone photo
    grad = Image.linear_gradient("L").resize(bg.size).rotate(35)
    bg = Image.composite(bg, Image.new("RGB", bg.size, (40, 30, 20)), grad.point(lambda p: 180 + p // 4))
    bg = bg.filter(ImageFilter.GaussianBlur(0.9))
    px = bg.load()
    for _ in range(60000):
        x, yy = rnd.randrange(900), rnd.randrange(1200)
        r, g, b = px[x, yy]; n = rnd.randint(-14, 14)
        px[x, yy] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))
    bg.save(path, quality=72)


def fabric_photo(path, seed=3):
    rnd = random.Random(seed)
    im = Image.new("RGB", (900, 900), "#1F3A93")
    d = ImageDraw.Draw(im)
    cols = ["#F2C14E", "#F78154", "#4D9078", "#B4436C", "#FFFFFF"]
    for y in range(0, 900, 90):
        for x in range(0, 900, 90):
            c = rnd.choice(cols)
            d.ellipse([x + 15, y + 15, x + 75, y + 75], outline=c, width=7)
            d.polygon([(x + 45, y + 25), (x + 65, y + 45), (x + 45, y + 65), (x + 25, y + 45)], fill=rnd.choice(cols))
    im = im.filter(ImageFilter.GaussianBlur(1.2))
    im.save(path, quality=80)


def pdf_remittance(path, payer, payee, lines, total_minor, currency, pay_date, method, ref):
    c = canvas.Canvas(path, pagesize=LETTER)
    W, H = LETTER
    c.setFillColor(HexColor("#1F2937")); c.setFont("Helvetica-Bold", 20)
    c.drawString(60, H - 80, payer)
    c.setFont("Helvetica", 10); c.setFillColor(HexColor("#6B7280"))
    c.drawString(60, H - 98, "Accounts Payable")
    c.setFillColor(HexColor("#111827")); c.setFont("Helvetica-Bold", 16)
    c.drawString(60, H - 150, "REMITTANCE ADVICE")
    c.setFont("Helvetica", 11)
    y = H - 180
    for k, v in [("To", payee), ("Payment date", pay_date), ("Method", method), ("Payment reference", ref)]:
        c.drawString(60, y, f"{k}:"); c.drawString(200, y, v); y -= 18
    y -= 20
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, y, "Invoice"); c.drawString(220, y, "Invoice date"); c.drawRightString(540, y, "Amount paid")
    c.line(60, y - 6, 540, y - 6); y -= 24; c.setFont("Helvetica", 11)
    for inv, dt, amt in lines:
        c.drawString(60, y, inv); c.drawString(220, y, dt); c.drawRightString(540, y, money_text(amt, currency)); y -= 20
    c.line(60, y + 8, 540, y + 8)
    c.setFont("Helvetica-Bold", 12); c.drawString(60, y - 10, "Total"); c.drawRightString(540, y - 10, money_text(total_minor, currency))
    c.setFont("Helvetica-Oblique", 8); c.setFillColor(HexColor("#9CA3AF"))
    c.drawString(60, 40, "SAMPLE DOCUMENT · Recur test data · fictional company")
    c.save()


def pdf_wire_receipt(path, bank, rows, title="Outgoing Wire Confirmation"):
    c = canvas.Canvas(path, pagesize=LETTER)
    W, H = LETTER
    c.setFillColor(HexColor("#0B2A4A")); c.rect(0, H - 90, W, 90, fill=1, stroke=0)
    c.setFillColor(HexColor("#FFFFFF")); c.setFont("Helvetica-Bold", 20); c.drawString(50, H - 55, bank)
    c.setFillColor(HexColor("#111827")); c.setFont("Helvetica-Bold", 15); c.drawString(50, H - 130, title)
    y = H - 165; c.setFont("Helvetica", 11)
    for k, v in rows:
        c.setFillColor(HexColor("#6B7280")); c.drawString(50, y, k)
        c.setFillColor(HexColor("#111827")); c.drawString(230, y, v); y -= 22
    c.setFont("Helvetica-Oblique", 8); c.setFillColor(HexColor("#9CA3AF"))
    c.drawString(50, 40, "SAMPLE DOCUMENT · Recur test data · not a real transaction")
    c.save()


def pdf_invoice(path, seller, buyer, number, issued, due, items, currency):
    c = canvas.Canvas(path, pagesize=LETTER)
    W, H = LETTER
    c.setFont("Helvetica-Bold", 22); c.drawString(60, H - 80, seller)
    c.setFont("Helvetica-Bold", 28); c.setFillColor(HexColor("#6B7280")); c.drawRightString(550, H - 80, "INVOICE")
    c.setFillColor(HexColor("#111827")); c.setFont("Helvetica", 11)
    c.drawString(60, H - 130, f"Bill to: {buyer}")
    c.drawRightString(550, H - 130, f"Invoice {number}")
    c.drawRightString(550, H - 148, f"Issued {issued}")
    c.drawRightString(550, H - 166, f"Due {due}")
    y = H - 220; c.setFont("Helvetica-Bold", 11); c.drawString(60, y, "Description"); c.drawRightString(550, y, "Amount")
    c.line(60, y - 6, 550, y - 6); y -= 26; c.setFont("Helvetica", 11); total = 0
    for desc, amt in items:
        c.drawString(60, y, desc); c.drawRightString(550, y, money_text(amt, currency)); y -= 20; total += amt
    c.line(60, y + 8, 550, y + 8); c.setFont("Helvetica-Bold", 13)
    c.drawString(60, y - 12, "Amount due"); c.drawRightString(550, y - 12, money_text(total, currency))
    c.setFont("Helvetica", 10); c.drawString(60, y - 50, "Please pay by bank transfer and include the invoice number as your reference.")
    c.setFont("Helvetica-Oblique", 8); c.setFillColor(HexColor("#9CA3AF"))
    c.drawString(60, 40, "SAMPLE DOCUMENT · Recur test data · fictional company")
    c.save()
