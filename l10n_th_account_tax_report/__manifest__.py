# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "Thailand Localization - VAT and Withholding Tax Reports",
    "version": "14.0.1.0.0",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-thailand",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        "date_range",
        "report_xlsx_helper",
        "l10n_th_fonts",
        "l10n_th_partner",
        "l10n_th_account_tax",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/paper_format.xml",
        "data/report_data.xml",
        "reports/tax_report.xml",
        "reports/tax_report_rd.xml",
        "reports/report_wht_qweb.xml",
        "reports/report_wht_qweb_rd.xml",
        "reports/report_wht_text.xml",
        "wizard/tax_report_wizard_view.xml",
        "wizard/withholding_tax_report_wizard_view.xml",
        "views/account_withholding_tax.xml",
        "views/res_company_view.xml",
    ],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["kittiu"],
}
