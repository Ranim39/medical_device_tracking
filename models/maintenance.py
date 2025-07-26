from odoo import models,fields
class MedicalDeviceMaintenance(models.Model):
    _name = 'medical.device.maintenance'
    _description = 'Historique des maintenances'
    #creation d'une relation entre les deux modéles 
    #une maintenance concerne un seul appareil
    #le champ device_id permet de dire="cette ligne de maint appartient à cet appareil médical" 
    device_id=fields.Many2one('medical.device',string='Appareil Concerné',required=True,ondelete='cascade')
    maintenance_date=fields.Date(string='Date de Maintenance',required=True)
    technician_name=fields.Char(string='Nom du Technicien')
    intervention_type=fields.Selection(
    [
        ('prevent','Préventive'),
        ('correct','Corrective'),
        ('inspect','Inspection')
    ],
    string="Type d'intervention",required=True
    )
    duration=fields.Float(string='Durée de maintenance')
    #Pour gerer le montant d'argent tu dois lui associer une devise(currency)
    #exp Devise ou currency :EUROS , DINARS ...  donc cout=12000 EUROS
    cost=fields.Monetary(string="le Coùt de la maintenance",currency_field='currency_id')
    #res.currency:c'est un modéle standars d'Odoo qui contient toutes les devises utilisées dans le systéme
    currency_id=fields.Many2one('res.currency',string='Devise liée au cout')
    notes=fields.Text(string='Remarques')
