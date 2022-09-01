from odoo import models, fields, api


class BaseDocumentLayout(models.TransientModel):

    _inherit = 'base.document.layout'

    header_image = fields.Binary(string="Header Image", related='company_id.header_image', readonly=False)
    footer_image = fields.Binary(string="Footer Image", related='company_id.footer_image', readonly=False)
    water_mark = fields.Binary(string="Water Mark", related='company_id.water_mark', readonly=False)
    company_watermark = fields.Binary(string="Letterhead", related='company_id.company_watermark', readonly=False)
    image_type = fields.Selection([('single_image', 'Single Image'), ('multiple_image', 'Multiple Image')], string="Image Type", related='company_id.image_type', readonly=False, default='multiple_image')

    def document_layout_save(self):
        res = super(BaseDocumentLayout, self).document_layout_save()
        for wizard in self:
            wizard.company_id.header_image
            wizard.company_id.footer_image
            wizard.company_id.water_mark
            wizard.company_id.company_watermark
            wizard.company_id.image_type
        return res