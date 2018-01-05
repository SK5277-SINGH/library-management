# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):
	_inherit = 'product.template'
	role_librarian =fields.Boolean(string="Librarian")

	_sql_constraints = [
    ('ISBN_unique', 'unique(isbn)', ' Please enter unique isbn.')
    ]
	book_type = fields.Many2many('material', string='Book Type')
	isbn = fields.Char(string='ISBN')
	description = fields.Text(string='Description')

	language = fields.Selection(
		[
			('english', 'English'), 
			('hindi', 'Hindi'),
			('urdu', 'Urdu'),
			('gujarati', 'Gujarati'),
			('other', 'Other'),
		])
	author = fields.Many2one('res.partner',domain=[('is_status', "=", "author")])
	publisher =  fields.Many2one('res.partner',domain=[('is_status', "=", "publisher")])
	copies = fields.Integer(string="Copies")
	date = fields.Date(string="Date")

	@api.constrains('isbn')
	def unique_isbn(self):
		pass

class Materials(models.Model):
	_name="material"
	name= fields.Char("Book Type")









	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management
