# Order Report Project

Detta projekt är en refaktorering av ett befintligt Python-program som analyserar orderdata från en CSV-fil och skapar flera rapporter.

Syftet med refaktoreringen är att göra programmet mer strukturerat, testbart och lättare att underhålla.

## Funktionalitet

Programmet:

* läser orderdata från `data/orders.csv`
* validerar att obligatoriska kolumner finns
* rensar och normaliserar data
* beräknar ordervärden och rabatterade värden
* skapar en övergripande sammanställning
* sammanställer försäljning per produktkategori
* sammanställer försäljning per region
* beräknar returer per produktkategori
* sparar rapporterna som CSV-filer i `output/`

## Projektstruktur

```text
order-report-project/
├── data/
│   └── orders.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_cleaner.py
│   ├── data_loader.py
│   ├── report_generator.py
│   └── report_writer.py
├── tests/
│   ├── test_data_cleaner.py
│   ├── test_data_loader.py
│   └── test_report_generator.py
├── .gitignore
├── code_review.md
├── order_report.py
├── README.md
└── requirements.txt
```

## Installation

Skapa en virtuell miljö:

```powershell
python -m venv .venv
```

Aktivera den virtuella miljön:

```powershell
.venv\Scripts\Activate.ps1
```

Installera projektets beroenden:

```powershell
pip install -r requirements.txt
```

## Kör programmet

Programmet körs med:

```powershell
python order_report.py
```

Rapporterna skapas i mappen `output/`:

* `overview.csv`
* `sales_by_category.csv`
* `sales_by_region.csv`
* `returns_by_category.csv`

## Tester

Projektet använder pytest för automatiska tester.

Kör alla tester med:

```powershell
python -m pytest -v
```

Testerna kontrollerar bland annat datainläsning, validering, datarensning, felhantering och rapportberäkningar.

## Reflektion

### 1. Vilka var de viktigaste problemen i originalkoden?

De största problemen var att nästan all kod låg i samma fil och kördes direkt. Det fanns också duplicerad kod, generell felhantering med `except Exception` och flera `print()`-satser istället för logging. Det gjorde programmet svårare att testa, underhålla och vidareutveckla.

### 2. Vilka förändringar tycker du förbättrade programmet mest?

Den största förbättringen var att dela upp programmet i mindre moduler och funktioner med tydliga ansvarsområden. Jag förbättrade också felhanteringen, lade till logging och tog bort duplicerad kod genom att återanvända samma funktion för rapporter per kategori och region.

### 3. Varför valde du den projektstruktur du använde?

Jag valde att lägga programmets olika delar i `src` och testerna i `tests`. I `src` har varje modul ett tydligt ansvar, till exempel inläsning, datarensning, rapportgenerering och sparning. Strukturen gör det enklare att hitta i projektet och att ändra en del utan att behöva ändra hela programmet.

### 4. Var använde du OOP/dataclass och varför passade det där?

Jag använde en `dataclass` som heter `ReportConfig` i `config.py`. Den innehåller sökvägen till inputfilen och outputmappen. Det passade bra eftersom dessa värden hör ihop som konfiguration för rapportprogrammet och kan samlas i ett objekt istället för att ligga som separata globala variabler.

### 5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?

Testerna kontrollerar bland annat att CSV-filen kan läsas, att obligatoriska kolumner valideras, att saknade filer hanteras, att data rensas korrekt och att försäljning, returer och andra rapportvärden beräknas rätt. Om programmet ändras i framtiden kan testerna snabbt visa om en förändring har gjort att någon av dessa funktioner inte längre fungerar som förväntat.

### 6. Vad var svårast?

Det svåraste var att dela upp originalkoden utan att förändra programmets ursprungliga resultat. Det var viktigt att förstå vilka delar som hörde ihop och hur funktionerna skulle kommunicera med varandra.

### 7. Vad hade du velat förbättra ytterligare om du haft mer tid?

Med mer tid hade jag lagt till fler tester för ovanliga och felaktiga datavärden. Jag hade också kunnat förbättra valideringen ytterligare, till exempel genom att kontrollera rimliga intervall för `quantity`, `discount` och `unit_price`.
