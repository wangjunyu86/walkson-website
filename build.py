# -*- coding: utf-8 -*-
"""Walkson overseas website static generator.
Product data comes from the official Made-in-China storefront scrape."""
import json, os, html
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, 'data', 'category-groups.json')

COMPANY = 'Chongqing Walkson Machinery Equipment Manufacturing Co., Ltd.'
PHONE = '+86 23 4040 8333'
EMAIL = 'sales@walksonmachinery.com'
ADDRESS = 'Building 2, No.124 Tongxi Road, Bake Sub-district, Changshou District, Chongqing 401220, China'
SITE = 'https://www.walksonmachinery.com'

ORG_LD = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": COMPANY,
  "alternateName": "Walkson Machinery",
  "url": SITE,
  "logo": SITE + "/assets/img/logo.svg",
  "foundingDate": "2019-03-04",
  "email": EMAIL,
  "telephone": "+86-23-4040-8333",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Building 2, No.124 Tongxi Road, Bake Sub-district",
    "addressLocality": "Changshou District, Chongqing",
    "postalCode": "401220",
    "addressCountry": "CN"
  },
  "description": "Manufacturer of aluminum pergolas, bus shelters, outdoor benches, planters, waste bins, signage and street furniture. ISO 9001:2015 certified, OEM/ODM with MOQ from 1 piece.",
  "numberOfEmployees": {"@type": "QuantitativeValue", "value": 30},
  "knowsAbout": ["Aluminum Pergolas","Bus Shelters","Outdoor Benches","Metal Planters","Waste Bins","Wayfinding Signage","Bicycle Racks","Hand Trucks","Clothing Donation Bins","Parcel Boxes","Bollards","Dog Park Equipment"],
  "hasCredential": [
    {"@type": "EducationalOccupationalCredential", "name": "ISO 9001:2015"}
  ],
  "award": "8 nationally authorized patents",
  "sameAs": ["https://busshelters.en.made-in-china.com/"]
}

CATS = [
 ('gazebo','Aluminum Pergolas & Gazebos','gazebo-nLrUPGquoAkE.jpg',
  'Motorized louvered pergolas and gazebos in powder-coated aluminium with adjustable roofs, LED lighting and retractable side curtains for hotels, resorts, restaurants and villas.',
  'From US $680 / Set · MOQ 1 Set'),
 ('bus-shelter','Bus Shelters','bus-shelter-egOrpYoDXfkv.jpg',
  'Smart solar bus shelters with LED/LCD advertising light boxes, tempered glass and integrated seating, customised for municipal transit projects.',
  'From US $2,500 / Set · MOQ 1 Set'),
 ('outdoor-bench','Outdoor Benches & Seating','outdoor-bench-tuJUTPoyOGkZ.jpg',
  'Powder-coated metal, stainless steel, solid wood and recycled composite seating, including solar-powered smart park benches with charging ports.',
  'From US $79 / Set · MOQ 1 Set'),
 ('planter','Planters & Flower Boxes','planter-SgFYDVhJHEWi.jpg',
  'Corten steel, stainless steel and galvanised planters, raised beds and street flower boxes with custom dimensions, finishes and laser-cut logos.',
  'From US $178 / Piece · MOQ 5 Pieces'),
 ('waste-bin','Waste Bins & Recycling','waste-bin-WgfpduRVvGhA.jpg',
  'Street and park litter bins, stainless steel and HDPE bins, dual-compartment recycling stations and foot-pedal models.',
  'From US $49 / Piece · MOQ 10 Pieces'),
 ('signage','Signage & Wayfinding','signage-HzQRMyaxJYVd.jpg',
  'Wayfinding signage, traffic safety signs and notice boards in galvanised steel, aluminium, stainless steel and UV-printed acrylic.',
  'From US $48 / Piece · MOQ 1 Piece'),
 ('bicycle-parking-rack','Bicycle Parking Racks','bicycle-parking-rack-ZzgRcEWDaLkU.jpg',
  'Loop, grid, wave, spiral and vertical bicycle racks in powder-coated steel with anchor-bolt mounting and OEM branding.',
  'From US $48 / Piece · MOQ 1 Piece'),
 ('hand-truck','Hand Trucks & Trolleys','hand-truck-KLlrqDPAXgVZ.jpg',
  'Folding convertible hand trucks, platform carts and electric stair-climbing or riding trolleys for warehouses, hospitals and logistics.',
  'From US $99 / Piece · MOQ 1 Piece'),
 ('clothing-donation-bin','Clothing Donation Bins','clothing-donation-bin-CLpURTqGurWa.jpg',
  'Outdoor clothing and recycling donation banks with front-loading doors, advertising panels and custom colours and logos.',
  'From US $199 / Piece · MOQ 1 Piece'),
 ('parcel-box','Parcel Boxes','parcel-box-RPgpsnQyJuke.jpg',
  'Freestanding, wall-mounted and multi-compartment steel parcel boxes for homes and communities, powder-coated and weather-resistant.',
  'From US $129 / Piece · MOQ 1 Piece'),
 ('bollard','Bollards & Parking Posts','bollard-QPurqNjDgLct.jpg',
  'Fold-down parking posts plus removable and automatic rising bollards in stainless steel with reflective bands and lock systems.',
  'From US $59 / Piece · MOQ 1 Piece'),
 ('dog-park-equipment','Dog Park Equipment','dog-park-equipment-wPDYQZIEsRVJ.jpg',
  'Agility hoops, tunnels, seesaws, A-frames and pause tables for public dog parks and pet playgrounds in powder-coated steel and UV-resistant plastics.',
  'From US $288 / Piece · MOQ 1 Piece'),
]

# slug -> display key in category-groups.json
KEYMAP = {
 'gazebo':'Gazebo','bus-shelter':'Bus Shelter','outdoor-bench':'Outdoor Bench',
 'planter':'Planter','waste-bin':'Waste Bin','signage':'Signage',
 'bicycle-parking-rack':'Bicycle Parking Rack','hand-truck':'Hand Truck',
 'clothing-donation-bin':'Clothing Donation Bin','parcel-box':'Parcel Box',
 'bollard':'Bollard','dog-park-equipment':'Dog Park Equipment',
}

def items_for(data, slug):
    return data.get(KEYMAP.get(slug, ''), [])

FAQ_LD = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type":"Question","name":"What is the minimum order quantity (MOQ)?","acceptedAnswer":{"@type":"Answer","text":"Walkson accepts trial orders from 1 piece or 1 set for most product lines, with volume pricing available for larger municipal and project orders."}},
    {"@type":"Question","name":"Can Walkson customise products to my drawings?","acceptedAnswer":{"@type":"Answer","text":"Yes. Walkson offers OEM and ODM services and manufactures to sample, drawing or full custom design, including custom size, colour, RAL finish, logo and structure."}},
    {"@type":"Question","name":"What certifications does Walkson hold?","acceptedAnswer":{"@type":"Answer","text":"Walkson operates an ISO 9001:2015 quality management system. Applicable products can be supplied with CE conformity, and third-party inspection by SGS or TUV can be arranged on request."}},
    {"@type":"Question","name":"What are the payment and shipping terms?","acceptedAnswer":{"@type":"Answer","text":"Walkson accepts PayPal, T/T bank transfer, L/C and D/P. Products ship on FOB Chongqing or Shanghai, or CIF to the destination port."}},
    {"@type":"Question","name":"How long is the lead time?","acceptedAnswer":{"@type":"Answer","text":"Lead time is approximately one month in low season and longer during peak season; the exact schedule is confirmed per order."}},
    {"@type":"Question","name":"Where is Walkson located?","acceptedAnswer":{"@type":"Answer","text":"Chongqing Walkson Machinery Equipment Manufacturing Co., Ltd. is located at Building 2, No.124 Tongxi Road, Bake Sub-district, Changshou District, Chongqing 401220, China."}}
  ]
}

PRODUCT_DROPDOWN = '\n'.join(
    f'<a href="products.html#{k}">{html.escape(n)}</a>' for k, n, *_ in CATS
)

def esc(s): return html.escape(s or '', quote=True)

def head(title, desc, path='index.html', extra_ld=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Walkson Machinery">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{json.dumps(ORG_LD, ensure_ascii=False)}</script>
{extra_ld}
</head>
<body>
<div class="topbar"><div class="wrap">
  <span>ISO 9001:2015 Quality System · OEM / ODM Manufacturer · 8 National Patents</span>
  <span>Tel/WhatsApp {PHONE} &nbsp;·&nbsp; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
</div></div>
<header>
  <div class="wrap nav">
    <a class="brand" href="index.html">
      <span class="logo">W</span>
      <span><b>WALKSON</b><span>Outdoor Furniture &amp; Shelters</span></span>
    </a>
    <button class="nav-toggle" aria-label="Menu">☰</button>
    <nav><ul>
      <li><a href="index.html">Home</a></li>
      <li class="has-drop"><a href="products.html">Products &#9662;</a>
        <div class="dropdown">{PRODUCT_DROPDOWN}</div>
      </li>
      <li><a href="about.html">About Us</a></li>
      <li><a href="capabilities.html">Capabilities</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul></nav>
  </div>
</header>'''

FOOT = f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><span class="logo">W</span><b>WALKSON</b></div>
        <p>{esc(COMPANY)}</p>
        <p style="margin-top:10px">{esc(ADDRESS)}</p>
        <div class="badges"><span>ISO 9001:2015</span><span>CE</span><span>OEM / ODM</span></div>
      </div>
      <div><h4>Products</h4><ul>
        <li><a href="products.html#gazebo">Aluminum Pergolas</a></li>
        <li><a href="products.html#bus-shelter">Bus Shelters</a></li>
        <li><a href="products.html#outdoor-bench">Outdoor Benches</a></li>
        <li><a href="products.html#planter">Planters</a></li>
        <li><a href="products.html#waste-bin">Waste Bins</a></li>
        <li><a href="products.html">View all →</a></li>
      </ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="about.html">About Walkson</a></li>
        <li><a href="capabilities.html">Capabilities</a></li>
        <li><a href="capabilities.html#certifications">Certifications</a></li>
        <li><a href="contact.html">Contact &amp; Quotation</a></li>
      </ul></div>
      <div><h4>Contact</h4><ul>
        <li>Tel: {PHONE}</li>
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>WhatsApp / WeChat: on request</li>
        <li><a href="contact.html">Request a quotation →</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>© {date.today().year} {esc(COMPANY)} All rights reserved.</span>
      <span>Chongqing, China · Manufacturer &amp; exporter since 2019</span>
    </div>
  </div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>'''

def page_hero(eyebrow, h1, p):
    # h1 may contain trusted HTML entities; eyebrow/p are escaped
    return f'''<div class="page-hero"><div class="wrap">
  <div class="eyebrow">{esc(eyebrow)}</div><h1>{h1}</h1><p>{esc(p)}</p>
</div></div>'''

def cta_band():
    return f'''<section class="soft"><div class="wrap"><div class="cta-band">
  <div><h2>Need a custom quotation?</h2><p>Send us your drawings, dimensions or reference photos. We reply with pricing, lead time and shipping options — usually within one working day.</p></div>
  <div><a class="btn btn-primary" href="contact.html">Request a Quote</a></div>
</div></div></section>'''

def build_index(data):
    # ---- hero carousel slides: real photos + short selling copy ----
    slides = [
        ('gazebo-nLrUPGquoAkE.jpg',
         'Aluminum Pergolas &amp; Gazebos',
         'Motorized louvered roofs, LED lighting and retractable curtains — engineered for hotels, resorts and villas.',
         'gazebo', 'Explore Pergolas'),
        ('bus-shelter-egOrpYoDXfkv.jpg',
         'Smart Bus Shelters',
         'Solar-powered shelters with LCD advertising light boxes and tempered glass, built for municipal transit projects.',
         'bus-shelter', 'Explore Bus Shelters'),
        ('outdoor-bench-tuJUTPoyOGkZ.jpg',
         'Park Benches &amp; Seating',
         'Powder-coated steel, stainless steel and wood-composite seating, including solar smart benches with charging ports.',
         'outdoor-bench', 'Explore Benches'),
        ('waste-bin-WgfpduRVvGhA.jpg',
         'Planters, Waste Bins &amp; Street Furniture',
         'A full range of public-space furniture with custom RAL colours, laser-cut logos and OEM/ODM service.',
         'planter', 'Explore Street Furniture'),
    ]
    slides_html = ''
    dots = ''
    for i, (img, title, desc, key, cta) in enumerate(slides):
        active = ' active' if i == 0 else ''
        slides_html += f'''<div class="slide{active}" style="background-image:linear-gradient(115deg,rgba(8,18,32,.92) 0%,rgba(9,26,44,.72) 45%,rgba(9,26,44,.35) 100%),url('assets/img/products/{img}')">
  <div class="wrap"><div class="slide-inner">
    <div class="kicker">Chongqing Manufacturer · Since 2019</div>
    <h1>{title}</h1>
    <p>{desc}</p>
    <div class="cta">
      <a class="btn btn-primary" href="products.html#{key}">{cta}</a>
      <a class="btn btn-ghost" href="contact.html">Get a Quote</a>
    </div>
  </div></div>
</div>'''
        dots += f'<button class="dot{active}" data-slide="{i}" aria-label="Slide {i+1}"></button>'
    hero = f'''<div class="hero-carousel">
  <div class="slides">{slides_html}</div>
  <button class="arrow prev" aria-label="Previous">&#10094;</button>
  <button class="arrow next" aria-label="Next">&#10095;</button>
  <div class="dots">{dots}</div>
</div>'''

    # ---- simplified product navigation (icon + name, not a product shot) ----
    nav_items = ''
    for key, name, cover, desc, price in CATS:
        if not items_for(data, key): continue
        nav_items += f'''<a class="cat-tile" href="products.html#{key}">
  <span class="cat-name">{esc(name)}</span>
  <span class="cat-arrow">&#8594;</span>
</a>'''

    body = f'''{hero}
<section class="trustbar"><div class="wrap">
  <div class="trust"><b>1,564 m&#178;</b><span>Own factory workshop</span></div>
  <div class="trust"><b>8</b><span>National patents</span></div>
  <div class="trust"><b>ISO 9001</b><span>Quality management</span></div>
  <div class="trust"><b>MOQ 1</b><span>Piece or set</span></div>
  <div class="trust"><b>24/7</b><span>Global response</span></div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Product Range</div><h2>What We Manufacture</h2>
  <p>Twelve product lines produced in our own factory in Changshou District, Chongqing — from pergolas and bus shelters to hand trucks and dog park equipment. Trial orders from one piece.</p></div>
  <div class="cat-nav">{nav_items}</div>
  <div class="center" style="margin-top:38px"><a class="btn btn-dark" href="products.html">See Full Product Range</a></div>
</div></section>
<section class="soft"><div class="wrap">
  <div class="sec-head center" style="text-align:center;margin-bottom:34px"><div class="eyebrow">Why Walkson</div><h2>Factory-Direct, Quality-Focused</h2></div>
  <div class="feat-grid">
    <div class="feat"><div class="ico">&#127981;</div><h3>Own Factory</h3><p>1,564 m&#178; workshop with laser cutting, CNC bending and shearing equipment, two production lines and 100% finished-goods inspection.</p></div>
    <div class="feat"><div class="ico">&#9999;&#65039;</div><h3>OEM / ODM</h3><p>Custom size, colour, logo and structure. Send a drawing, sample or reference photo and we manufacture to your specification.</p></div>
    <div class="feat"><div class="ico">&#128220;</div><h3>Quality System</h3><p>ISO 9001:2015 quality management, traceable raw materials and documented inspection at every production stage.</p></div>
    <div class="feat"><div class="ico">&#128674;</div><h3>Export Ready</h3><p>FOB / CIF terms with T/T, L/C or D/P, plus one-piece trial orders before volume production.</p></div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Certifications</div><h2>Certificates &amp; Quality Documents</h2>
  <p>Our quality system and factory documents are available for buyer review. Third-party inspection can be arranged through SGS, T&#220;V or your nominated agency.</p></div>
  <div class="cert-grid">
    <div class="cert"><div class="cert-ico">&#9989;</div><h3>ISO 9001:2015</h3><p>Quality management system certificate covering production.</p><span class="cert-link">Certificate copy on request</span></div>
    <div class="cert"><div class="cert-ico">&#127970;</div><h3>Factory Audit Report</h3><p>Workshop capacity, equipment and process audit documentation.</p><span class="cert-link">Available on request</span></div>
    <div class="cert"><div class="cert-ico">&#129514;</div><h3>Material / Test Reports</h3><p>Raw material and finish test reports from third-party labs.</p><span class="cert-link">Available on request</span></div>
    <div class="cert"><div class="cert-ico">&#128196;</div><h3>Export Documents</h3><p>Commercial invoice, packing list, B/L and certificate of origin.</p><span class="cert-link">Issued per order</span></div>
  </div>
  <p class="note" style="margin-top:16px">Certificate images will be uploaded once the latest scanned copies are supplied by the factory.</p>
</div></section>
<section class="soft"><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Projects</div><h2>Engineering Case Studies</h2>
  <p>We support municipal, landscape, hospitality and transit projects with custom fabrication, drawings and installation guidance.</p></div>
  <div class="case-grid">
    <div class="case"><div class="case-img"><img src="assets/img/products/bus-shelter-egOrpYoDXfkv.jpg" alt="Bus shelter project" loading="lazy"></div><div class="case-body"><span class="tag">Public Transit</span><h3>Smart Bus Shelter Programme</h3><p>Solar shelters with LCD advertising panels and seating, delivered in knock-down form for local assembly.</p></div></div>
    <div class="case"><div class="case-img"><img src="assets/img/products/gazebo-nLrUPGquoAkE.jpg" alt="Pergola project" loading="lazy"></div><div class="case-body"><span class="tag">Hospitality</span><h3>Louvered Pergola for Resort Poolside</h3><p>Motorised aluminium pergolas with LED lighting and side curtains for an outdoor dining terrace.</p></div></div>
    <div class="case"><div class="case-img"><img src="assets/img/products/outdoor-bench-tuJUTPoyOGkZ.jpg" alt="Park furniture project" loading="lazy"></div><div class="case-body"><span class="tag">Landscape</span><h3>Park Furniture Package</h3><p>Benches, planters and waste bins finished in a matched RAL colour for a public park upgrade.</p></div></div>
  </div>
  <p class="note" style="margin-top:16px">Project photos and reference lists are added as clients approve publication.</p>
</div></section>
<section><div class="wrap about-2">
  <div>
    <div class="sec-head" style="margin-bottom:14px"><div class="eyebrow">About the Factory</div><h2>Metal Fabrication in Chongqing&#39;s Industrial Belt</h2></div>
    <p>Walkson is located in Changshou District, Chongqing &#8212; next to the Chongqing steel industrial base, with a complete local supply chain for raw materials, subcontracting and logistics.</p>
    <p>Since 2019 we have built a team with over 15 years of industry experience and eight nationally authorised patents, serving municipal, tourism and commercial projects worldwide.</p>
    <ul class="check">
      <li>Laser cutting, CNC bending and shearing equipment</li>
      <li>Two production lines with 100% finished-goods inspection</li>
      <li>Own logistics and installation team, 24/7 global response</li>
      <li>Custom manufacturing to drawing, site conditions and budget</li>
    </ul>
  </div>
  <img src="assets/img/products/bus-shelter-fuaYRBsOCtVw.jpg" alt="Bus shelter manufactured by Walkson" loading="lazy">
</div></section>
{cta_band()}'''
    return head('Walkson Machinery | Aluminum Pergolas, Bus Shelters & Outdoor Furniture Manufacturer in China',
                'Chongqing Walkson manufactures aluminum pergolas, bus shelters, outdoor benches, planters, waste bins, signage and street furniture. ISO 9001 quality system, OEM/ODM, MOQ 1 piece.') + body + FOOT

def build_products(data):
    # ---- left sidebar catalogue ----
    side = '<a class="side-link active" href="#top" data-side="all">All Products</a>'
    for key, name, *_ in CATS:
        items = items_for(data, key)
        if not items: continue
        side += f'<a class="side-link" href="#{key}" data-side="{key}">{esc(name)} <span>{len(items)}</span></a>'

    sections = ''
    for key, name, cover, desc, price in CATS:
        items = items_for(data, key)
        if not items: continue
        cards = ''
        for it in items:
            if not it.get('local'): continue
            p_ = it.get('price') or price.split('\u00b7')[0].replace('From ','')
            m = it.get('moq') or ''
            cards += f'''<div class="pcard" data-cat="{key}">
  <div class="thumb"><img src="{esc(it['local'])}" alt="{esc(it['title'])}" loading="lazy" width="400" height="400"></div>
  <div class="body">
    <h3>{esc(it['title'][:96])}</h3>
    <div class="meta"><span class="price">{esc(p_)}</span><span class="moq">MOQ {esc(m) if m else '1'}</span></div>
    <div class="iq"><a href="contact.html?product={esc(it['id'])}">Request Quotation</a></div>
  </div>
</div>'''
        sections += f'''<div class="cat-head" id="{key}"><h2>{esc(name)}</h2><a href="contact.html">Ask about this range &#8594;</a></div>
<div class="pgrid" data-cat-group="{key}">{cards}</div>'''

    # ItemList of products for rich results / AI
    il_items = []
    pos = 0
    for key, name, cover, desc, price in CATS:
        for it in items_for(data, key):
            if not it.get('local'): continue
            pos += 1
            il_items.append({
                "@type": "ListItem", "position": pos, "name": it['title'],
                "url": SITE + "/products.html#" + key,
                "image": SITE + "/" + it['local']
            })
    il = {"@context":"https://schema.org","@type":"ItemList","numberOfItems":pos,"itemListElement":il_items[:120]}
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(il, ensure_ascii=False)
    body = page_hero('Product Catalogue',
        'Street Furniture &amp; Outdoor Structures',
        'A representative selection from our catalogue of more than 1,000 products. All items can be customised in size, colour, material and branding. Prices shown are indicative FOB Chongqing.') + \
        f'''<section id="top"><div class="wrap product-layout">
  <aside class="side-nav">
    <h3>Product Categories</h3>
    {side}
    <div class="side-cta"><b>Can&#39;t find it?</b><p>Send a drawing or reference photo for a custom quotation.</p><a class="btn btn-primary" href="contact.html">Request a Quote</a></div>
  </aside>
  <div class="product-main">{sections}</div>
</div></section>{cta_band()}'''
    return head('Products | Walkson Machinery — Pergolas, Bus Shelters, Benches, Planters & More',
                'Browse Walkson outdoor products: aluminum pergolas, bus shelters, park benches, planters, waste bins, signage, bicycle racks, hand trucks, bollards, parcel boxes and dog park equipment.',
                'products.html', extra_ld=extra) + body + FOOT

def build_about():
    body = page_hero('About Us','Chongqing Walkson Machinery Equipment Manufacturing Co., Ltd.',
        'A metal fabrication manufacturer producing outdoor furniture, public shelters and municipal amenities for domestic and export markets since 2019.') + f'''
<section><div class="wrap about-2">
  <div>
    <div class="sec-head" style="margin-bottom:14px"><div class="eyebrow">Who We Are</div><h2>Manufacturer &amp; Trading Company</h2></div>
    <p>Walkson is based in Changshou District, Chongqing, close to the Chongqing steel industrial base. This location gives us a complete local supply chain for raw material sourcing, subcontract processing and logistics.</p>
    <p>We specialise in customised metal products — integrating in-house R&amp;D, custom production, global sales and full project support. Our core technical team brings more than 15 years of industry experience.</p>
    <p>Our equipment includes laser cutting machines, CNC bending machines and shearing machines, supported by two production lines and a 100% finished-goods inspection process.</p>
    <ul class="check">
      <li>Founded 2019 · registered capital RMB 5 million</li>
      <li>1,564 m² manufacturing workshop</li>
      <li>8 nationally authorised patents</li>
      <li>OEM and ODM services · customisation to sample or drawing</li>
      <li>Exporting since May 2024 to North America, Europe, Southeast Asia, the Middle East, Africa and Oceania</li>
    </ul>
  </div>
  <img src="assets/img/products/gazebo-hPYrvToDJtWi.jpg" alt="Aluminum louvered pergola" loading="lazy">
</div></section>
<section class="soft"><div class="wrap">
  <div class="sec-head center" style="text-align:center;margin-bottom:34px"><div class="eyebrow">Company Facts</div><h2>At a Glance</h2></div>
  <div class="feat-grid">
    <div class="feat"><div class="ico">📅</div><h3>Established 2019</h3><p>Chongqing Walkson Machinery Equipment Manufacturing Co., Ltd., registered 4 March 2019.</p></div>
    <div class="feat"><div class="ico">🏗️</div><h3>1,564 m² Workshop</h3><p>Two production lines, laser cutting, CNC bending, shearing and welding equipment.</p></div>
    <div class="feat"><div class="ico">🌍</div><h3>Global Exports</h3><p>Serving North &amp; South America, Europe, Southeast Asia, the Middle East, Africa and Oceania.</p></div>
    <div class="feat"><div class="ico">🤝</div><h3>50–80% Repeat</h3><p>A high proportion of returning customers, supported by an average response time under 2.4 hours.</p></div>
  </div>
</div></section>
{cta_band()}'''
    return head('About Walkson Machinery | Metal Fabrication Manufacturer in Chongqing, China',
                'Chongqing Walkson Machinery Equipment Manufacturing Co., Ltd. — established 2019, 1,564 m2 factory, 8 patents, ISO 9001:2015 quality system, OEM/ODM metal fabrication.',
                'about.html') + body + FOOT

def build_capabilities():
    body = page_hero('Capabilities &amp; Certifications','Engineering, Quality Control and Export Services',
        'From custom design and prototype to volume production, inspection and shipping — all handled in-house or through our verified supplier network.') + f'''
<section><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Production</div><h2>Equipment &amp; Capacity</h2>
  <p>Two production lines and a full sheet-metal workshop allow us to produce both one-off custom pieces and volume orders.</p></div>
  <div class="feat-grid">
    <div class="feat"><div class="ico">⚙️</div><h3>Sheet Metal Processing</h3><p>Laser cutting machines, CNC bending machines, shearing machines, rolling and polishing equipment.</p></div>
    <div class="feat"><div class="ico">🔥</div><h3>Welding &amp; Assembly</h3><p>Welding stations for aluminium and steel structures, followed by grinding, assembly and finishing.</p></div>
    <div class="feat"><div class="ico">🎨</div><h3>Surface Finishing</h3><p>Powder coating, galvanising and stainless steel finishing in standard or custom RAL colours.</p></div>
    <div class="feat"><div class="ico">🔍</div><h3>100% Inspection</h3><p>Every finished product is inspected for appearance and function against a written work instruction.</p></div>
  </div>
</div></section>
<section class="soft"><div class="wrap">
  <div class="sec-head"><div class="eyebrow">How We Work</div><h2>From Inquiry to Delivery</h2></div>
  <div class="steps">
    <div class="step"><h3>Share Requirements</h3><p>Send drawings, dimensions, reference photos or a target budget and quantity.</p></div>
    <div class="step"><h3>Quotation &amp; Drawing</h3><p>We confirm material, finish and specification, then issue an FOB or CIF quotation.</p></div>
    <div class="step"><h3>Sample or Production</h3><p>Approve a sample or drawing, then we manufacture with in-process and final inspection.</p></div>
    <div class="step"><h3>Packing &amp; Shipping</h3><p>Protective export packing, documentation and shipment from Chongqing or Shanghai port.</p></div>
  </div>
</div></section>
<section id="certifications"><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Certifications</div><h2>Quality &amp; Compliance</h2>
  <p>Our quality system and export documentation are in place, and third-party inspection can be arranged on request.</p></div>
  <div class="feat-grid">
    <div class="feat"><div class="ico">✅</div><h3>ISO 9001:2015</h3><p>Quality management system certification covering our production operations.</p></div>
    <div class="feat"><div class="ico">🛡️</div><h3>Third-Party Testing</h3><p>Products can be tested by SGS, TÜV or other nominated third-party inspection agencies on request.</p></div>
    <div class="feat"><div class="ico">🧪</div><h3>CE / Export Compliance</h3><p>Applicable products can be supplied with CE conformity and export documentation for European market requirements.</p></div>
    <div class="feat"><div class="ico">📄</div><h3>Trade Documentation</h3><p>Commercial invoice, packing list, bill of lading and certificates of origin as required.</p></div>
  </div>
</div></section>
<section class="soft"><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Trade Terms</div><h2>Export Terms at a Glance</h2></div>
  <div class="feat-grid">
    <div class="feat"><h3>MOQ</h3><p>From 1 piece or 1 set, allowing trial orders and small project quantities.</p></div>
    <div class="feat"><h3>Incoterms</h3><p>FOB Chongqing / Shanghai and CIF to your destination port.</p></div>
    <div class="feat"><h3>Payment</h3><p>PayPal, T/T bank transfer, L/C letter of credit and D/P.</p></div>
    <div class="feat"><h3>Lead Time</h3><p>Approximately one month in low season; longer during peak season, confirmed per order.</p></div>
  </div>
</div></section>
{cta_band()}'''
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(FAQ_LD, ensure_ascii=False)
    return head('Capabilities & Certifications | Walkson Machinery',
                'Walkson production capabilities: laser cutting, CNC bending, welding, powder coating, 100% inspection. ISO 9001:2015 certified with OEM/ODM custom fabrication.',
                'capabilities.html', extra_ld=extra) + body + FOOT

def build_contact():
    body = page_hero('Contact Us','Request a Quotation',
        'Tell us the product, quantity, size and destination port — and attach a drawing or reference photo if you have one. Our export team normally replies within one working day.') + f'''
<section><div class="wrap contact-grid">
  <div>
    <div class="sec-head" style="margin-bottom:20px"><div class="eyebrow">Get in Touch</div><h2>Export Sales Department</h2></div>
    <div class="info-row"><span class="ico">🏢</span><div><b>Company</b><span>{esc(COMPANY)}</span></div></div>
    <div class="info-row"><span class="ico">📍</span><div><b>Address</b><span>{esc(ADDRESS)}</span></div></div>
    <div class="info-row"><span class="ico">☎️</span><div><b>Telephone</b><span>{PHONE}</span></div></div>
    <div class="info-row"><span class="ico">✉️</span><div><b>Email</b><span>{EMAIL} <em>(to be confirmed)</em></span></div></div>
    <div class="info-row"><span class="ico">🕐</span><div><b>Business Hours</b><span>Monday–Saturday, 09:00–18:00 China Standard Time (GMT+8)</span></div></div>
    <div class="info-row"><span class="ico">🌐</span><div><b>Languages</b><span>English · Chinese</span></div></div>
    <p class="note">For the fastest quotation, include product type, dimensions, quantity, colour/finish and destination port.</p>
  </div>
  <form action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
    <h3 style="font-size:18px;margin-bottom:6px">Send an Inquiry</h3>
    <p style="font-size:13px;color:#5b6b7c">Fields marked * are required.</p>
    <label for="name">Your Name *</label>
    <input id="name" name="name" required>
    <label for="company">Company</label>
    <input id="company" name="company">
    <label for="email">Email *</label>
    <input id="email" type="email" name="email" required>
    <label for="country">Country</label>
    <input id="country" name="country">
    <label for="product">Product of Interest *</label>
    <select id="product" name="product" required>
      <option value="">Please select…</option>
      <option>Aluminum Pergola / Gazebo</option>
      <option>Bus Shelter</option>
      <option>Outdoor Bench / Seating</option>
      <option>Planter / Flower Box</option>
      <option>Waste Bin / Recycling</option>
      <option>Signage / Wayfinding</option>
      <option>Bicycle Parking Rack</option>
      <option>Hand Truck / Trolley</option>
      <option>Clothing Donation Bin</option>
      <option>Parcel Box</option>
      <option>Bollard / Parking Post</option>
      <option>Dog Park Equipment</option>
      <option>Other / Custom Project</option>
    </select>
    <label for="message">Quantity, Size &amp; Requirements *</label>
    <textarea id="message" name="message" rows="5" required></textarea>
    <label for="drawing">Upload Drawing / Reference Photo <span style="font-weight:400;color:#5b6b7c">(optional)</span></label>
    <input id="drawing" type="file" name="attachment" accept=".pdf,.dwg,.dxf,.jpg,.jpeg,.png,.zip,.rar,.xlsx,.doc,.docx">
    <p class="note" style="margin-top:6px">Engineering customers can upload CAD drawings (DWG/DXF), PDFs or reference photos. Max 10 MB per file; for larger files, mention it in your message and we will send a secure upload link.</p>
    <input type="hidden" name="_subject" value="New website inquiry — Walkson">
    <input type="hidden" name="_template" value="table">
    <button class="btn btn-primary" type="submit">Send Inquiry</button>
    <p class="note">This static form uses a free form-to-email relay. No customer data is stored on the website, and drawings are sent only to our export sales inbox.</p>
  </form>
</div></section>
{cta_band()}'''
    return head('Contact Walkson Machinery | Request a Quotation',
                'Contact Chongqing Walkson Machinery for quotations on aluminum pergolas, bus shelters, benches, planters, waste bins and street furniture. Export sales reply within one working day.',
                'contact.html') + body + FOOT

def main():
    data = json.load(open(DATA, encoding='utf-8'))
    pages = {
        'index.html': build_index(data),
        'products.html': build_products(data),
        'about.html': build_about(),
        'capabilities.html': build_capabilities(),
        'contact.html': build_contact(),
    }
    for fn, htmltxt in pages.items():
        open(os.path.join(ROOT, fn), 'w', encoding='utf-8').write(htmltxt)
        print('wrote', fn, len(htmltxt))

if __name__ == '__main__':
    main()
