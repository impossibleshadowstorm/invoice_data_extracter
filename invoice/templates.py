PLANT_LIPIDS = {
    "name": "Plant Lipids Private Limited",
    "keywords": [
        "Plant Lipids Private Limited",
        "32AABCP6061C1ZY",
        "10012041000146",
    ],
    "fields": {
        "gst": {
            "parser": "regex",
            "pattern": "GSTIN : \d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}",
            "type": "str",
        },
        "cin": {
            "parser": "regex",
            "pattern": "CIN NO: ([LUu]{1})([0-9]{5})([A-Za-z]{2})([0-9]{4})([A-Za-z]{3})([0-9]{6})",
            "type": "str",
        },
        "invoice_date": {
            "parser": "regex",
            "pattern": "invoice date\s*([\d]{1,2}\s\w+\s[\d]{4})",
            "type": "str",
        },
        "invoice_number": {
            "parser": "regex",
            "pattern": "invoice no\.\s*:\s*(\w+)",
            "type": "str",
        },
        "total_amount": {
            "parser": "regex",
            "pattern": "Total[ \w]*?(\d{2},\d{2,3},\d{3}\.\d{2})",
            "type": "float",
        },
    },
}

ASSOCIATE_ALLIED = {
    "name": "ASSOCIATE ALLIED CHEMICALS (INDIA) PRIVATE LIMITED",
    "keywords": [
        "ASSOCIATE ALLIED CHEMICALS (INDIA) PRIVATE LIMITED",
        "27AACCA0687L1ZG",
        "U24110MH1995PTC089749",
    ],
    "fields": {
        "gst": {
            "parser": "regex",
            "pattern": "GSTIN : \d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}",
            "type": "str",
        },
        "cin": {
            "parser": "regex",
            "pattern": "CIN NO: ([LUu]{1})([0-9]{5})([A-Za-z]{2})([0-9]{4})([A-Za-z]{3})([0-9]{6})",
            "type": "str",
        },
        "invoice_date": {
            "parser": "regex",
            "pattern": "Invoice Date\s*:\s*([\d]{2}\s\w{3}\s[\d]{4})",
            "type": "str",
        },
        "invoice_number": {
            "parser": "regex",
            "pattern": "Invoice No\.\s*:\s*(\w+)",
            "type": "str",
        },
        "total_amount": {
            "parser": "regex",
            "pattern": "Total\s*([,\d]+\.\d{2})",
            "type": "float",
        },
    },
}

TEMPLATES = [ASSOCIATE_ALLIED, PLANT_LIPIDS]