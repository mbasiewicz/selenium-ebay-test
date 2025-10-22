# Selenium eBay Test - Kodilla

Test automatyczny wyszukiwania na stronie eBay wykonany w ramach kursu Kodilla.

## Opis testu

Test `test_search` sprawdza:

- Wyszukiwanie frazy "laptop" na eBay
- Weryfikację kolejności wyświetlania kategorii w wynikach
- Poprawność pozycjonowania: "Computers/Tablets & Networking" powinno być wyżej niż "Laptops & Netbooks"

## Wymagania

- Python 3.8+
- Przeglądarka Chrome lub Firefox
- ChromeDriver / GeckoDriver

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/mbasiewicz/selenium-ebay-test.git
cd selenium-ebay-test
```

2. Utwórz wirtualne środowisko:

```bash
python -m venv .venv
```

3. Aktywuj środowisko:

- **Windows**: `.venv\Scripts\activate`
- **Linux/Mac**: `source .venv/bin/activate`

4. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

## Uruchomienie testów

```bash
pytest test_ebay.py --driver Chrome -v
```

Lub z przeglądarką Firefox:

```bash
pytest test_ebay.py --driver Firefox -v
```

## Technologie

- Python
- Selenium WebDriver
- Pytest
- Pytest-Selenium

## Autor

Projekt wykonany w ramach kursu Kodilla
Moduł 2.3
