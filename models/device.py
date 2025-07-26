#ce fichier va définir un modéle Odoo pour représenter un appareil médical vendu à un client 

from odoo import models ,fields
#importer framework Odoo :contient les fonctionnalités de base
#models=le module fourni par Odoo qui permet de créer tes propres modéles de data
#fields=le systeme de declaration des colones de la table  dans tes modéles
class  MedicalDevice(models.Model):
#models.model=la classe de base que tout les modémes Odoo doivent hériter
#chaque appareil a des champs=fields 
 _name = 'medical.device'     #Le nom technique du modéle càd ce modéle s'appelle medical.device dans le systéme interne d'Odoo
 _description= 'Appareil Médical'   



 name=fields.Char(string="Nom")
 achat_date=fields.Date(string="Date d'achat")
 serial_number=fields.Char(string="Numéro de série")
 client_id=fields.Many2one('res.partner',string="client",required=True)
 garantie_duration=fields.Integer(string="durée de garantie (mois)")
 statut=fields.Selection([
 ('in_service','En service'),
 ('maintenance','En maintenance'),
 ('broken','Hors service')
 ],string="Etat de l'appareil",default='in_service')
 notes=fields.Text(string="Remarques")
#liste des maintenances faites sur l'appareil
#le champ maintenances_ids va chercher toutes les lignes de maintenances dans le modéle medical.device.maintenance qui ont device_id=cet appareil médical 
 maintenances_ids=fields.One2many(
    'medical.device.maintenance','device_id',string="Maintenances"
)