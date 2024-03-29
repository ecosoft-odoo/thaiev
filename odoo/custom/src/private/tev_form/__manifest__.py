# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "TEV Form",
    "summary": "Collect all form of Thai EV",
    "version": "14.0.1.0.0",
    "author": "I C E Solutions",
    "category": "TEV",
    "license": "AGPL-3",
    "depends": [
        "stock",
        "sale",
        "sale_management",
        "l10n_th_amount_to_text"
    ],
    "data": [
        "views/product_product.xml",
        "views/sale_order.xml",
        "views/res_users.xml",
        "data/report_paperformat_data.xml",
        "data/report_data.xml",
        "report/quotation_form_sale.xml",
        "report/delivery_note_tax_invoice.xml",
        "report/credit_note_tax_invoice.xml",
        "report/invoice.xml",
        "report/receipt_tax_invoice.xml",
        "report/receipt.xml"
    ],
    "installable": True,
     'application': True,
}
