# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Topnet_dossier(models.Model):
    _name = 'topnet.dossier'
    _description = 'dossier topnet '
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def create(self, vals):
        if vals.get('id_dossier', _('New')) == _('New'):
            vals['id_dossier'] = self.env['ir.sequence'].next_by_code('topnet.dossier.sequence') or _('New')
        result = super(topnet.dossier, self).create(vals)
        return result
# @api.model
# def create(self, values):
#     vals_dossier = {
#         'id_contrat': values.get('id_contrat'),
#
#     }
#     user_id = self.env['client.fiche'].sudo().create(vals_dossier)
#     values.update(id_contrat=id_contrat)
#     res = super(Topnet_dossier, self).create(values)
#
#     return res

    id_contrat = fields.Many2one('client.fiche', string='Nom du gérant')


    # id_contrat_related = fields.Char('Numero de contrat', related='id_contrat')
    # dossier_id = fields.Many2one('topnet.dossier', ondelete='set null', string="dossier", index=True)
    id_dossier = fields.Char(string='Numéro Dossier', required=True, copy=False, readonly=True,
                             index=True, default=lambda self: _('New'))
    doc1 = fields.Image(string="Registre de commerce", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc2 = fields.Image(string="CIN gérant", max_width=90, max_height=90, verify_resolution=True, required=True)
    contrat_tt = fields.Binary (string= 'telecharger contrat TT')
    doc3 = fields.Image(string="Contrat TOPNET", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc4 = fields.Image(string="Contrat TT", max_width=90, max_height=90, verify_resolution=True, required=True)

    # dossier_id = fields.Many2one('client.fiche', string='Dossier')
