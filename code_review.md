# Code Review – Order Report

## Nuvarande lösning

Programmet läser in orderdata från en CSV-fil med hjälp av pandas. 
Datan kontrolleras och rensas innan olika beräkningar görs. 
Programmet skapar sedan fyra CSV-rapporter i mappen `output`.

Jag körde originalprogrammet innan några ändringar gjordes. 
Programmet läste in 80 rader och skapade alla fyra rapporterna utan fel.

## Förbättringsområden

### 1. All kod ligger i samma fil
Hela programmet ligger i `order_report.py`. Det gör koden lång och svårare 
att underhålla. Koden kan delas upp i mindre moduler och funktioner med 
tydliga ansvarsområden.

### 2. Mycket kod körs direkt
Programmet börjar köra direkt när filen startas. Det finns ingen `main()`-funktion. 
En `main()`-funktion skulle göra programmets flöde tydligare och göra koden 
enklare att testa.

### 3. För generell felhantering
Programmet använder `except Exception`, vilket fångar alla typer av fel på 
samma sätt. Det är bättre att hantera specifika fel, till exempel om CSV-filen 
saknas eller om datan har fel format.

### 4. Otydligt felmeddelande vid saknade kolumner
Om en obligatorisk kolumn saknas används `raise Exception("Fel data")`. 
Felmeddelandet berättar inte vilka kolumner som saknas. Valideringen kan 
förbättras genom tydligare felmeddelanden.

### 5. Print används istället för logging
Programmet använder `print()` för att visa vad som händer. Logging skulle 
göra det lättare att följa programmets körning och skilja mellan information, 
varningar och fel.

### 6. Duplicerad kod
Beräkningarna för `sales_by_category` och `sales_by_region` är väldigt lika. 
Den duplicerade koden kan flyttas till en gemensam funktion som kan användas 
för båda rapporterna.

### 7. Svårt att testa delar av programmet
Eftersom stora delar av logiken ligger direkt i samma `try`-block är det svårt 
att testa enskilda delar. Genom att skapa mindre funktioner blir det möjligt 
att skriva enhetstester för exempelvis datarensning, validering och beräkningar.

## Planerad refaktorering

Jag planerar att dela upp programmet i mindre moduler och funktioner. 
Jag kommer även att förbättra validering och felhantering, använda logging 
och skapa tester med pytest. Målet är att behålla programmets nuvarande 
funktionalitet samtidigt som koden blir tydligare, mer återanvändbar och 
enklare att testa.