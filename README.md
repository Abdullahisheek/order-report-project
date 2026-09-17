# Order Report Project

Detta projekt är en refaktorering av ett befintligt Python-program som
analyserar orderdata från en CSV-fil och skapar flera rapporter.

Syftet med refaktoreringen är att göra programmet mer strukturerat,
testbart och lättare att underhålla.

## Funktionalitet

Programmet:

- läser orderdata från `data/orders.csv`
- validerar att obligatoriska kolumner finns
- rensar och normaliserar data
- beräknar ordervärden och rabatterade värden
- skapar en övergripande sammanställning
- sammanställer försäljning per produktkategori
- sammanställer försäljning per region
- beräknar returer per produktkategori
- sparar rapporterna som CSV-filer i `output/`

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