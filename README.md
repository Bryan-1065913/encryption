# Encryptie & Decryptie

Voor het vak Security & Cyberwarfare was mij gevraagd een programma te schrijven dat een tekst kan encrypten en decrypten. Dit heb ik gedaan in Python. In dit document zal ik uitleggen hoe het programma werkt en hoe je het kan gebruiken. Daarnaast zal ik uitleggen met welke externe modules ik heb gewerkt.

## Hoe installeer je de modules?

Om het programma te kunnen gebruiken raad ik aan om een venv aan te maken. Dit kan je doen door de volgende commando's uit te voeren:

```bash
python -m venv venv
source venv/bin/activate
```
Daarna kun je de volgende commando's uitvoeren om de benodigde modules te installeren:

```bash
pip install -r requirements.txt
```

Als je dit hebt gedaan heb je alle benodigde modules geïnstalleerd en zou je het programma moeten kunnen gebruiken.

## Hoe werkt het programma?

Je kunt het programma starten door het bestand `main.py` uit te voeren. Vervolgens kun je kiezen of je een tekst wilt encrypten of decrypten. Als je kiest voor encrypten, dan wordt je gevraagd om een tekst in te voeren. Naast een tekst moet je ook een sleutel invoeren. Deze sleutel wordt gebruikt om de tekst te encrypten. Als je kiest voor decrypten, dan wordt je gevraagd om een tekst in te voeren. Naast een tekst moet je ook een sleutel invoeren. Deze sleutel wordt gebruikt om de tekst te decrypten. Als je de verkeerde sleutel invoert, dan zal de tekst niet correct worden gedecrypt.

## Welke externe modules heb ik gebruikt?

Ik heb gebruik gemaakt van de volgende externe modules:
- Tikinter: Dit is een module die je kunt gebruiken om een GUI te maken in Python. Ik heb deze module gebruikt om een GUI te maken voor het programma.
- Cryptography: Dit is een module die je kunt gebruiken om tekst te encrypten en decrypten. Ik heb deze module gebruikt om de tekst te encrypten en decrypten.
- pyperclip: Dit is een module die je kunt gebruiken om tekst te kopiëren en plakken. Ik heb deze module gebruikt om de geëncrypte en gedecrypte tekst te kopiëren naar het klembord.
- base64: Dit is een module die je kunt gebruiken om tekst te encoden en decoden. Ik heb deze module gebruikt om de geëncrypte en gedecrypte tekst te encoden en decoden.

## Hoe werkt Cryptography?

Cryptography maakt gebruik van een symmetrische encryptie. Dit betekent dat de tekst wordt geëncrypt met een sleutel en vervolgens weer wordt gedecrypt met dezelfde sleutel. Als je de verkeerde sleutel invoert, dan zal de tekst niet correct worden gedecrypt. Het is dus belangrijk dat je de juiste sleutel invoert.

Dit zorgt ervoor dat de tekst veilig wordt geëncrypt en gedecrypt. Als iemand anders de tekst probeert te decrypten zonder de juiste sleutel, dan zal de tekst niet correct worden gedecrypt.

## Bronnen

[Uitleg Cryptography](https://www.comparitech.com/blog/information-security/what-is-fernet/#:~:text=When%20a%20user%20wants%20to,the%20integrity%20of%20the%20message)

