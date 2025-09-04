from odoo import models, fields

class EmployeeAttachment(models.Model):
    _inherit = "ir.attachment"

    employee_id = fields.Many2one("hr.employee", string="Nhân viên")
