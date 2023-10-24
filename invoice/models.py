from django.db import models
from model_utils.models import TimeStampedModel

class File(TimeStampedModel):
    file            = models.FileField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"CommonFile [{self.pk}] {self.file}"

class VendorInvoice(models.Model):
    vendor_name     = models.CharField(max_length=255, null=True, default=None)
    gstin           = models.CharField(max_length=15, verbose_name="GSTIN no.", null=True, default=None)
    state_code      = models.CharField(max_length=5, null=True, default=None)
    state_name      = models.CharField(max_length=255, null=True, default=None)
    invoice_date    = models.DateField(null=True, default=None)
    invoice_no      = models.CharField(max_length=255, null=True, default=None)
    po_no           = models.CharField(max_length=255, blank=True, null=True)
    tax_percent     = models.CharField(max_length=255, verbose_name="Tax %", null=True, default=None)
    taxable_amount  = models.CharField(max_length=255, null=True, default=None)
    total_amount    = models.CharField(max_length=255, null=True, default=None)
    invoice_file    = models.ForeignKey(File, on_delete=models.CASCADE)
    result          = models.BooleanField(default=True)

    def __str__(self):
        return self.vendor_name + " - " + self.invoice_no

    class Meta:
        verbose_name = "Vendor Invoice"
        verbose_name_plural = "Vendor Invoices"