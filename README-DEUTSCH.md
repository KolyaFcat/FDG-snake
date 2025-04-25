## Hallo, ich bin Nikolai Fedorov.
### Schlange-Spiel für das FDG-Gymnasium in Aschaffenburg.

Dateiname            | Inhalt der Datei
---------------------|------------------------
pics                 | Ordner mit Bildern
sound                | Ordner mit Sounds
fdg_snake_main.py    | Python-Programm

Technologie-Stack: pygame 2.6.1, sys, time, random, itertools

Klasse/Funktion             | Beschreibung
----------------------------|-------------------------------
Funktion `load_image`       | Lädt ein Bild und stellt dessen Größe ein
Klasse `Game`               | Spielklasse, beschreibt die Hauptparameter des Spiels: Spielfeld, Bilder, Sounds, Schrift
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `__init__`         | Initialisiert die Klasse  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `main`             | Hauptmethode/Hauptschleife des Spiels  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `pickup`           | Wenn der Kopf den Burhschtarbe trifft, erhöht sich der Punktestand und ein neuer Burhschtarbe wird gezeichnet  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `text_on_screen`   | Gibt Text auf dem Bildschirm aus  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `gameover`         | Setzt `self.game_play = False`, wenn der Schlangenkopf den Körper trifft  
Klasse `Snake`              | Schlange-Klasse, speichert Parameter der Schlange  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `__init__`         | Initialisiert die Klasse  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `move`             | Bewegt die Schlange, prüft Tasteneingaben und ändert die Richtung  

Screenshot des Spiels:  
<img width="405" alt="Screenshot 2025-04-19  Snake" src="https://github.com/user-attachments/assets/cef5d5bf-5f61-40a1-ae37-43f062128a21" />

Ich hoffe, es hat dir gefallen. Viel Spaß beim Spielen!
