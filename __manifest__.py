#c'est la fiche d'idendité de module 
#nom de module
#dépendances
#data:xml files(view) , security

{
 
 'name':'Device_Tracker',
 'version':'1.0',
 'depends':['sale','calendar'], 
 'data':[
     'views/device_views.xml',
     'views/maintenance_views.xml',
     'security/ir.model.access.csv'
 ],
 #Données de démonstration facultatifs
 #'demo':[
  #   'demo/demo_data.xml'
 #],
 'installable':True,  #le module peut étre installé
 'application':True,  #Apparait dans la liste des apps


}
 
 
 
 
 
 
 
 
 
 
 
 