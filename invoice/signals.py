import json
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from invoice.models import File
from invoice.helpers import get_data
from invoice.templates import TEMPLATES
from invoice.chatbot import Chatbot
from invoice.models import VendorInvoice

REGEX = "regex"


def get_template(data):
    for template in TEMPLATES:
        for keyword in template["keywords"]:
            if keyword is not None and keyword.lower() in data:
                return template


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return date_string
    except ValueError:
        return None


@receiver(post_save, sender=File)
def post_save_vendor_invoice(sender, instance, created, **kwargs):
    text = get_data(instance.file.path)

    chatbot = Chatbot()
    response = chatbot.generate_response(text)
    fail = 3
    while fail > 0:
        try:
            message_content = (
                response.get(
                    "choices",
                )[0]
                .get("message")
                .get("content")
            )
            data = json.loads(message_content.split("```json\n")[1].split("\n```")[0])

            invoice = VendorInvoice(
                vendor_name=data.get("vendor_name"),
                gstin=data.get("gstin"),
                state_code=data.get("state_code"),
                state_name=data.get("state_name"),
                invoice_date=validate_date(data.get("invoice_date")),
                invoice_no=data.get("invoice_no"),
                po_no=data.get("po_no"),
                tax_percent=data.get("tax_percent"),
                taxable_amount=data.get("taxable_amount"),
                total_amount=data.get("total_amount"),
                invoice_file=instance,
            )

            invoice.save()
            fail = 0
        except:
            fail -= 1
