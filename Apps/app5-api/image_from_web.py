import requests

# per recuperare le immagini bisogna agire in maniera diversa rispetto ai metodi
#  precedenti in quanto si tratta di file binari

response = requests.get("https://cdn.discordapp.com/avatars/392445914163445781/9e8a2fc0b5af2174a14b0023a39f0641.png?size=4096")

# scrivo il contenuto in un file: utilizzare la modalità "wb" in quanto trattasi di file binari
with open("image.png", "wb") as file:
    file.write(response.content)