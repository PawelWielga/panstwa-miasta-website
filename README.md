# Państwa Miasta Website

Oficjalny landing page gry **Państwa Miasta**.

Docelowy adres:

```text
https://panstwamiasta.dihor.pl
```

## Co zawiera strona

- opis gry i potwierdzonych funkcji aplikacji na Androida,
- zalety lokalnej rozgrywki przez Wi-Fi lub hotspot,
- proces tworzenia pokoju, rundy, oceniania i wyników,
- schematyczne makiety aktualnego UI aplikacji,
- informację o planowanym kliencie przeglądarkowym,
- FAQ, metadane SEO, Open Graph, favicon, `robots.txt` i `sitemap.xml`,
- publiczną politykę prywatności pod niezmiennym adresem `/privacy-policy/`.

Przycisk Google Play pozostaje nieaktywny i jest oznaczony jako „Wkrótce”, dopóki nie będzie dostępny prawdziwy adres karty aplikacji. Klient przeglądarkowy również nie jest przedstawiany jako gotowa funkcja.

## Technologia

Strona jest lekka i statyczna:

- semantyczny HTML5,
- CSS bez frameworka,
- niewielki, natywny JavaScript dla menu mobilnego i nagłówka,
- brak zależności produkcyjnych i zewnętrznych fontów,
- publikacja bezpośrednio z katalogu głównego przez GitHub Pages.

## Struktura

```text
.
├── .github/workflows/validate-site.yml
├── assets/
│   ├── favicon.svg
│   ├── logo-mark.svg
│   └── og-image.svg
├── docs/
│   ├── privacy-policy.md
│   └── screenshots/
├── privacy-policy/
│   └── index.html
├── tests/
│   └── validate_site.py
├── .nojekyll
├── CNAME
├── index.html
├── robots.txt
├── script.js
├── sitemap.xml
└── styles.css
```

## Uruchomienie lokalne

```bash
python3 -m http.server 8080
```

Następnie otwórz:

```text
http://localhost:8080
```

Nie otwieraj plików wyłącznie przez `file://`, ponieważ ścieżki bezwzględne i zachowanie nawigacji mogą różnić się od hostingu HTTP.

## Kontrole

```bash
python3 tests/validate_site.py
node --check script.js
```

Walidator bez zewnętrznych zależności sprawdza między innymi:

- wymagane pliki,
- pojedynczy nagłówek `h1`, język dokumentu i metadane,
- brak przekierowania strony głównej,
- poprawność linków lokalnych i kotwic,
- stały adres polityki prywatności,
- wartość pliku `CNAME`,
- brak przedwczesnych aktywnych linków do Google Play i klienta WWW.

Workflow `Validate static site` uruchamia te kontrole dla Pull Requestów oraz pushy do `main` i branchy `feature/**`.

## GitHub Pages

W **Settings → Pages** ustaw:

1. **Source:** `Deploy from a branch`.
2. **Branch:** `main`.
3. **Folder:** `/ (root)`.
4. W polu **Custom domain** wpisz `panstwamiasta.dihor.pl`.
5. Po poprawnym wykryciu DNS włącz **Enforce HTTPS**.

Repozytorium zawiera plik `CNAME`, więc domena zostanie zachowana przy publikacji z brancha.

### DNS / Cloudflare

Dla subdomeny dodaj rekord:

```text
Type: CNAME
Name: panstwamiasta
Target: pawelwielga.github.io
```

Na czas pierwszej weryfikacji domeny przez GitHub Pages warto ustawić rekord jako **DNS only**. Po prawidłowym wydaniu certyfikatu można ponownie ocenić użycie proxy Cloudflare, ale najprostsza i najmniej problematyczna konfiguracja Pages pozostaje bez proxy.

Propagacja DNS i wydanie certyfikatu TLS mogą potrwać. Opcję **Enforce HTTPS** należy włączyć dopiero, gdy GitHub oznaczy certyfikat jako gotowy.

## Polityka prywatności

Publiczny adres pozostaje bez zmian:

```text
https://panstwamiasta.dihor.pl/privacy-policy/
```

Plik `privacy-policy/index.html` jest wersją używaną publicznie. Nie należy usuwać ani przenosić tej ścieżki bez równoczesnej aktualizacji Google Play Console.

## Powiązane repozytoria

- [`PawelWielga/panstwa-miasta`](https://github.com/PawelWielga/panstwa-miasta) — aplikacja mobilna na Androida i logika gry.
- [`PawelWielga/panstwa-miasta-play`](https://github.com/PawelWielga/panstwa-miasta-play) — planowany klient przeglądarkowy.

## Materiały do uzupełnienia

Po udostępnieniu wersji sklepowej należy:

1. podmienić nieaktywne CTA na prawdziwy link Google Play,
2. potwierdzić informację o cenie w FAQ,
3. zastąpić schematyczne makiety prawdziwymi screenshotami z aktualnej wersji aplikacji,
4. aktywować link do `play.panstwamiasta.dihor.pl` dopiero po wdrożeniu działającego klienta WWW.
