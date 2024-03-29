# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "ThaiEV: Report",
    "summary": "Customize Report template for ThaiEV",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "Thai EV",
    "author": "Ecosoft",
    "installable": True,
    "depends": [
        "account",
        "purchase",
        "sale",
    ],
    "data": [
        "report/sale_report_templates.xml",
        "report/purchase_order_templates.xml",
        "report/report_payment_receipt_templates.xml",
        "report/report_invoice_template.xml",
        "report/report.xml",
        "report/withholding_tax_cert_form_view.xml",
    ],
}
