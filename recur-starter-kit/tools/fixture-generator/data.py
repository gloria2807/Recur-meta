"""Single source of truth for Recur's test world.

Everything here is fictional: companies, people, banks and payment apps.
Domains use the reserved .example TLD. Amounts are in minor units.
"""

US_ORG = {"slug": "northwind", "name": "Northwind Studio", "legal_name": "Northwind Studio LLC",
          "city": "Austin, TX", "currency": "USD"}
NG_ORG = {"slug": "adaeze", "name": "Adaeze Fabrics", "legal_name": "Adaeze Fabrics Ltd",
          "city": "Lagos", "currency": "NGN"}

US_CUSTOMERS = [
    ("bluebird", "Bluebird Coffee", ["Bluebird Coffee Co", "Marcus Hale", "M Hale"], "marcus@bluebirdcoffee.example"),
    ("oakline", "Oakline Builders", ["Oakline Builders Inc"], "ap@oaklinebuilders.example"),
    ("lumen", "Lumen Dental", ["Lumen Dental Group", "Priya Nair"], "billing@lumendental.example"),
    ("harborpine", "Harbor & Pine", ["Harbor and Pine", "Harbor Pine Hospitality"], "accounts@harborpine.example"),
    ("fernstreet", "Fern Street Bakery", ["Fern St Bakery", "Dana Whitfield"], "dana@fernstreetbakery.example"),
    ("kestrel", "Kestrel Logistics", ["Kestrel Logistics LLC"], "payables@kestrel.example"),
    ("copperleaf", "Copperleaf Realty", ["Copperleaf Realty Partners", "Jordan Reyes"], "jordan@copperleaf.example"),
    ("juniper", "Juniper Yoga", ["Juniper Yoga Studio", "Ana Lima"], "ana@juniperyoga.example"),
    ("tidewater", "Tidewater Marine", ["Tidewater Marine Supply"], "ap@tidewatermarine.example"),
    ("redwood", "Redwood Legal Group", ["Redwood Legal", "RLG"], "finance@redwoodlegal.example"),
    ("sable", "Sable Fitness", ["Sable Fitness Club", "Chris Okoro"], "chris@sablefitness.example"),
    ("maplemoss", "Maple & Moss Florist", ["Maple and Moss", "Elena Park"], "elena@maplemoss.example"),
    ("atlas", "Atlas Tutoring", ["Atlas Tutoring Center"], "office@atlastutoring.example"),
    ("vantage", "Vantage Supply Co", ["Vantage Supply"], "orders@vantagesupply.example"),
]

NG_CUSTOMERS = [
    ("chioma", "Chioma Okafor Stores", ["Chioma Okafor", "C Okafor Stores"], "chioma@okaforstores.example"),
    ("bello", "Bello Textiles", ["Bello Textiles Nig", "Musa Bello"], "musa@bellotextiles.example"),
    ("adesons", "Ade & Sons Clothing", ["Ade and Sons", "Adewale Ade"], "adewale@adesons.example"),
    ("kemi", "Kemi's Boutique", ["Kemi Boutique", "Kemi Adebayo"], "kemi@kemiboutique.example"),
    ("emeka", "Emeka Tailoring", ["Emeka Nwosu"], "emeka@emekatailoring.example"),
    ("zainab", "Zainab Couture", ["Zainab Yusuf"], "zainab@zainabcouture.example"),
    ("ifeoma", "Ifeoma Designs", ["Ifeoma Eze"], "ifeoma@ifeomadesigns.example"),
    ("tunde", "Tunde Fashion House", ["Tunde Bakare"], "tunde@tundefashion.example"),
]

# (number, customer_slug, total_minor, issued, due)
US_INVOICES = [
    ("INV-1031", "oakline", 1250000, "2026-09-15", "2026-10-15"),
    ("INV-1032", "lumen", 380000, "2026-09-18", "2026-10-18"),
    ("INV-1033", "harborpine", 615000, "2026-09-20", "2026-10-20"),
    ("INV-1034", "fernstreet", 145000, "2026-09-22", "2026-10-22"),
    ("INV-1035", "kestrel", 920000, "2026-09-24", "2026-10-24"),
    ("INV-1036", "copperleaf", 275000, "2026-09-25", "2026-10-25"),
    ("INV-1037", "juniper", 98000, "2026-09-26", "2026-10-26"),
    ("INV-1038", "tidewater", 433500, "2026-09-28", "2026-10-28"),
    ("INV-1039", "redwood", 760000, "2026-09-29", "2026-10-29"),
    ("INV-1040", "sable", 212500, "2026-09-30", "2026-10-30"),
    ("INV-1041", "maplemoss", 64000, "2026-10-01", "2026-10-31"),
    ("INV-1042", "bluebird", 420000, "2026-10-02", "2026-11-01"),
    ("INV-1043", "atlas", 150000, "2026-10-03", "2026-11-02"),
    ("INV-1044", "oakline", 875000, "2026-10-05", "2026-11-04"),
    ("INV-1045", "lumen", 222000, "2026-10-06", "2026-11-05"),
    ("INV-1046", "kestrel", 350000, "2026-10-07", "2026-11-06"),
    ("INV-1047", "bluebird", 185000, "2026-10-08", "2026-11-07"),
    ("INV-1048", "harborpine", 199000, "2026-10-09", "2026-11-08"),
    ("INV-1049", "bluebird", 185000, "2026-10-10", "2026-11-09"),
    ("INV-1050", "copperleaf", 540000, "2026-10-11", "2026-11-10"),
    ("INV-1051", "fernstreet", 87500, "2026-10-12", "2026-11-11"),
    ("INV-1052", "juniper", 120000, "2026-10-13", "2026-11-12"),
    ("INV-1053", "tidewater", 312000, "2026-10-14", "2026-11-13"),
    ("INV-1054", "redwood", 990000, "2026-10-15", "2026-11-14"),
    ("INV-1055", "sable", 165000, "2026-10-16", "2026-11-15"),
    ("INV-1056", "maplemoss", 52500, "2026-10-17", "2026-11-16"),
    ("INV-1057", "atlas", 240000, "2026-10-18", "2026-11-17"),
    ("INV-1058", "vantage", 360000, "2026-10-19", "2026-11-18"),
    ("INV-1059", "kestrel", 128000, "2026-10-20", "2026-11-19"),
    ("INV-1060", "oakline", 350000, "2026-10-21", "2026-11-20"),
]

NG_INVOICES = [
    ("AF-2201", "chioma", 45000000, "2026-09-20", "2026-10-20"),
    ("AF-2202", "bello", 128000000, "2026-09-24", "2026-10-24"),
    ("AF-2203", "adesons", 37500000, "2026-09-27", "2026-10-27"),
    ("AF-2204", "kemi", 18500000, "2026-09-30", "2026-10-30"),
    ("AF-2205", "emeka", 9200000, "2026-10-02", "2026-11-01"),
    ("AF-2206", "zainab", 62000000, "2026-10-04", "2026-11-03"),
    ("AF-2207", "ifeoma", 24000000, "2026-10-06", "2026-11-05"),
    ("AF-2208", "tunde", 51500000, "2026-10-08", "2026-11-07"),
    ("AF-2209", "chioma", 33000000, "2026-10-10", "2026-11-09"),
    ("AF-2210", "bello", 76000000, "2026-10-12", "2026-11-11"),
    ("AF-2211", "kemi", 14000000, "2026-10-14", "2026-11-13"),
    ("AF-2212", "adesons", 41000000, "2026-10-16", "2026-11-15"),
    ("AF-2213", "zainab", 28500000, "2026-10-18", "2026-11-17"),
    ("AF-2214", "emeka", 11800000, "2026-10-20", "2026-11-19"),
    ("AF-2215", "tunde", 66000000, "2026-10-22", "2026-11-21"),
]

# Trusted money records. source: bank_feed (US bank CSV), bank_alert (trusted email),
# paystack (NG). These are the only things that can make an invoice paid.
MONEY = [
    # id, org, source, external_id, amount_minor, currency, received_at, payer_name, reference/narration
    ("M01", "northwind", "bank_feed", "BL-77120", 1250000, "USD", "2026-10-20T15:02:00-05:00", "OAKLINE BUILDERS INC", "ACH CREDIT OAKLINE BUILDERS INV-1031"),
    ("M02", "northwind", "bank_feed", "BL-77131", 380000, "USD", "2026-10-21T10:11:00-05:00", "PRIYA NAIR", "ZELLE FROM PRIYA NAIR INV 1032"),
    ("M03", "northwind", "bank_feed", "BL-77158", 615000, "USD", "2026-10-22T13:40:00-05:00", "HARBOR PINE HOSPITALITY", "ACH CREDIT HARBOR PINE HOSP 1033"),
    ("M04", "northwind", "bank_feed", "BL-77162", 145000, "USD", "2026-10-22T16:05:00-05:00", "DANA WHITFIELD", "ZELLE FROM DANA WHITFIELD FERN ST"),
    ("M05", "northwind", "bank_feed", "BL-77190", 920000, "USD", "2026-10-23T09:30:00-05:00", "KESTREL LOGISTICS LLC", "WIRE IN KESTREL LOGISTICS REF KL-88213"),
    ("M06", "northwind", "bank_feed", "BL-77204", 98000, "USD", "2026-10-23T18:22:00-05:00", "ANA LIMA", "ZELLE FROM ANA LIMA YOGA SEPT"),
    ("M07", "northwind", "bank_feed", "BL-77233", 433500, "USD", "2026-10-24T11:15:00-05:00", "TIDEWATER MARINE SUPPLY", "ACH CREDIT TIDEWATER MARINE INV1038"),
    ("M08", "northwind", "bank_feed", "BL-77251", 185000, "USD", "2026-10-25T12:03:00-05:00", "BLUEBIRD COFFEE CO", "ZELLE FROM BLUEBIRD COFFEE CO"),
    ("M09", "northwind", "bank_feed", "BL-77268", 200000, "USD", "2026-10-26T10:48:00-05:00", "REDWOOD LEGAL GROUP", "ACH CREDIT REDWOOD LEGAL PARTIAL"),
    ("M10", "northwind", "bank_feed", "BL-77279", 212500, "USD", "2026-10-26T14:30:00-05:00", "C OKORO", "ZELLE FROM C OKORO"),
    ("M11", "northwind", "bank_feed", "BL-77290", 64000, "USD", "2026-10-27T09:05:00-05:00", "ELENA PARK", "ZELLE FROM ELENA PARK FLOWERS"),
    ("M12", "northwind", "bank_feed", "BL-77301", 275000, "USD", "2026-10-27T15:20:00-05:00", "COPPERLEAF REALTY PARTNERS", "ACH CREDIT COPPERLEAF INV-1036"),
    ("M13", "northwind", "bank_feed", "BL-77315", 150000, "USD", "2026-10-28T08:50:00-05:00", "ATLAS TUTORING CENTER", "ACH CREDIT ATLAS TUTORING 1043"),
    ("M14", "northwind", "bank_feed", "BL-77322", 1225000, "USD", "2026-10-28T10:10:00-05:00", "OAKLINE BUILDERS INC", "ACH CREDIT OAKLINE BUILDERS REMIT 2026-1028"),
    ("M15", "northwind", "bank_feed", "BL-77330", 125000, "USD", "2026-10-28T11:40:00-05:00", "J REYES", "ZELLE FROM J REYES"),
    ("N01", "adaeze", "paystack", "ps_ref_8812301", 45000000, "NGN", "2026-10-19T10:15:00+01:00", "Chioma Okafor", "Payment for AF-2201"),
    ("N02", "adaeze", "paystack", "ps_ref_8812377", 37500000, "NGN", "2026-10-24T14:02:00+01:00", "Adewale Ade", "AF-2203"),
    ("N03", "adaeze", "bank_alert", "LGN-55120931", 18500000, "NGN", "2026-10-26T09:41:00+01:00", "KEMI ADEBAYO", "TRF FRM KEMI ADEBAYO/BOUTIQUE GOODS"),
    ("N04", "adaeze", "paystack", "ps_ref_8812490", 50000000, "NGN", "2026-10-27T16:30:00+01:00", "Musa Bello", "Part payment"),
    ("N05", "adaeze", "bank_alert", "LGN-55121877", 24000000, "NGN", "2026-10-28T11:12:00+01:00", "IFEOMA EZE", "TRF FRM IFEOMA EZE AF2207"),
]
