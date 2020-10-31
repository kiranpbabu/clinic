# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ClinicClinic(models.Model):
    _name = 'clinic.clinic'
    _description = "Clinic"

    name = fields.Char(required=1)
    contact_name = fields.Char(required=1)
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    phone = fields.Char('Phone')
    mobile = fields.Char('Mobile')
    title = fields.Many2one('res.partner.title')
    function = fields.Char('Job Position')
    email = fields.Char('Email')
    line_ids = fields.One2many('clinic.line', 'clinic_id')

class ClinicLine(models.Model):
    _name = 'clinic.line'
    _description = "Clinic Lines"
    _order = 'date desc'

    clinic_id = fields.Many2one('clinic.clinic')
    date = fields.Date(required=1, default=fields.Date.context_today)
    prescription = fields.Html(required=1)
    amount = fields.Monetary(currency_field='currency_id', required=1)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.user.company_id.currency_id)
