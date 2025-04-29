## Hallo, ich bin Nikolai Fedorov.
### Schlange-Spiel für das Friedrich-Dessauer-Gymnasium in Aschaffenburg.

Dateiname            | Inhalt der Datei
---------------------|------------------------
pics                 | Ordner mit Bildern
sound                | Ordner mit Sounds
fdg_snake_main.py    | Python-Programm

Technologie-Stack: pygame 2.6.1, python 3.13.3,sys, time, random, itertools

Klasse/Funktion             | Beschreibung
----------------------------|-------------------------------
Funktion `load_image`       | Sie lädt ein Bild und stellt dessen Größe ein
Klasse `Game`               | Spielklasse, die die Hauptparameter des Spiels: Spielfeld, Bilder, Sounds, Schrift beschreibt
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `__init__`         | Sie initialisiert die Klasse  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `main`             | Hauptmethode/Hauptschleife des Spiels  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `pickup`           | Wenn der Kopf den Burhschtarbe trifft, erhöht sich der Punktestand und ein neuer Burhschtarbe wird gezeichnet  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `text_on_screen`   | Sie gibt Text auf dem Bildschirm aus  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `gameover`         | Sie setzt `self.game_play = False`, wenn der Schlangenkopf den Körper trifft  
Klasse `Snake`              | Schlange-Klasse, die Parameter der Schlange speichert
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `__init__`         | Sie initialisiert die Klasse  
&nbsp; &nbsp; &nbsp; &nbsp; Funktion `move`             | Sie bewegt die Schlange, prüft Tasteneingaben und ändert die Richtung  

Screenshot des Spiels:  
<p align="center">
  <img src="https://github.com/KolyaFcat/FDG-snake/blob/master/pics/screen_01.png" width="45%" />
  <img src="https://github.com/KolyaFcat/FDG-snake/blob/master/pics/screen%2002.png" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/KolyaFcat/FDG-snake/blob/master/pics/screen%2004.png" width="45%" />
  <img src="https://github.com/KolyaFcat/FDG-snake/blob/master/pics/screen%2005.png" width="45%" />
</p>

Ich hoffe, es hat dir gefallen. Viel Spaß beim Spielen!!!
