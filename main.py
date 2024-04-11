import requests

# Définir les clés
public_key = "959F4A67-A093-1358-5FE1-D1C9AF3F026F"
secret_key = "F6D427E3-C069-DE62-7E93-FB384DC18A30"

# Définir l'en-tête de la requête
headers = {
  "Authorization": "Bearer " + secret_key + ":" +  public_key
}

# Envoyer la requête
response = requests.get("https://s3p.smobilpay.staging.maviance.info/v2/merchant/", headers=headers)

# Vérifier le code de statut
if response.status_code == 200:
  # Traiter la réponse
  data = response.json()
else:
  # Gérer l'erreur
  print("Erreur : ", response.status_code)