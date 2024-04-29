# PAC-MAN 👻
Dezvoltarea în CLIPS a unui sistem decizional pentru jocul Pac-Man

## Descriere
Proiectul prezintă dezvoltarea unui sistem decizional pentru jocul Pac-Man. Baza de fapte descrie mediul de joc în care agentul inteligent Pac-Man se deplasează și are dimensiunile unei matrice de 11x11 căsuțe. În joc se regăsesc, pe lângă Pac-Man, bile albe, fructe și fantome. Scopul lui Pac-Man este de a mânca toate fructele fără a fi prins de fantome. Pentru a mânca fantomele și a ajunge la fructe, Pac-Man trebuie să mănânce o bilă albă. Regulile create vizează mișcarea agentului, mâncarea bilelor albe, a fructelor și a fantomelor și excepțiile care apar. La fiecare pas Pac-Man verifică dacă, în căsuțele adiacente locului în care se află, se regăsește o fantomă, un fruct, o bilă albă sau un perete. După verificare, acesta execută mișcarea. Jocul se termină când Pac-Man fie mănâncă toate fructele și toate bilele albe, fie toate fructele, dar nu și toate bilele albe. Dacă Pac-Man intră într-un perete sau este mâncat de o fantomă, jocul se consideră pierdut.

## Obiectiv & Reguli
- Jocul se termină când Pac-Man reușește să mănânce toate fructele. Jucătorul pierde jocul când se lovește de o fantomă sau intră în perete.
- Pac-Man se deplasează doar pe direcție verticală și orizontală, cu ajutorul indicațiilor: sus, jos, stânga, dreapta;
Dacă Pac-Man găsește fruct, îl mănâncă. Dacă fructul este protejat de un obstacol (fantomă), Pac-Man trebuie să mănânce o bilă albă pentru a elimina obstacolul.

## Tehnologii utilizate
- CLIPS: pentru dezvoltarea sistemului expert, a bazei de fapte și a regulilor;
- Python: 
  - Tkinter: Biblioteca Tkinter este folosită pentru a crea elemente GUI precum ferestre și casete de text;
  - Clipspy: Această bibliotecă facilitează integrarea sistemului CLIPS în aplicații Python. Permite evaluarea instrucțiunilor CLIPS și utilizarea acestora în aplicație.
  - PIL (Python Imaging Library): Modulele PIL, în special Image și ImageTk, sunt folosite pentru manipularea imaginilor și afișarea acestora în interfața grafică Tkinter. Aceste module permit conversia imaginilor PIL într-un format compatibil cu Tkinter.

## Screenshots
* GUI-ul conține două ipostaze ale jocului: starea inițială din care pleacă Pac-Man (Fig. 3)  și starea finală în care Pac-Man ajunge (Fig. 4), după ce mănâncă fructele (kiwi), bilele albe și fantomele. În ambele ipostaze sunt prezentate și mișcările mai importante pe care acesta le realizează în partea dreaptă a GUI-ului.

![image](https://github.com/StefaniaPaduraru/pac-man-game/assets/100425781/0104b9c0-ee08-44b8-a969-e2d012de2ec4)
![image](https://github.com/StefaniaPaduraru/pac-man-game/assets/100425781/52be8c84-b44e-4df2-b412-9132c1a89c67)
