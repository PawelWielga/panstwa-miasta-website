# Państwa Miasta Website

Oficjalny landing page gry **Państwa Miasta**.

Publiczny adres:

```text
https://pawelwielga.github.io/panstwa-miasta-website/
```

## Co zawiera strona

- opis gry i potwierdzonych funkcji aplikacji na Androida,
- lokalną rozgrywkę przez Wi-Fi lub hotspot,
- przygotowany do wydania 1.2.0 tryb online z hostem Android i klientem WWW,
- proces tworzenia pokoju, rundy, oceniania i wyników,
- schematyczne makiety aktualnego UI aplikacji,
- FAQ, metadane SEO, Open Graph, favicon, `robots.txt` i `sitemap.xml`,
- publiczną politykę prywatności pod niezmiennym adresem `/privacy-policy/`.

Przycisk Google Play pozostaje nieaktywny i jest oznaczony jako „Wkrótce”, dopóki nie będzie dostępny prawdziwy adres karty aplikacji. Produkcyjny klient WWW jest już wdrożony pod adresem:

```text
https://pawelwielga.github.io/panstwa-miasta-play/
```

Landing opisuje online jako funkcję wydania Android 1.2.0, żeby nie sugerować, że nieopublikowana jeszcze wersja Androida jest już dostępna w Google Play.

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

Nie otwieraj plików wyłącznie przez `file://`, ponieważ ścieżki i zachowanie nawigacji mogą różnić się od hostingu HTTP.

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
- standardowy adres projektu GitHub Pages,
- brak przedwczesnego aktywnego linku Google Play,
- obecność właściwego produkcyjnego adresu klienta WWW,
- brak starego, niewdrożonego adresu klienta,
- opis PeerJS/WebRTC i GitHub Pages w publicznej polityce prywatności.

Workflow `Validate static site` uruchamia te kontrole dla Pull Requestów oraz pushy do `main` i branchy `feature/**`.

## GitHub Pages

Strona korzysta z dotychczasowej konfiguracji GitHub Pages:

1. **Source:** `Deploy from a branch`.
2. **Branch:** `main`.
3. **Folder:** `/ (root)`.

Aktualny publiczny adres:

```text
https://pawelwielga.github.io/panstwa-miasta-website/
```

Własna domena nie jest obecnie wymagana ani konfigurowana. Pliku `CNAME` nie należy dodawać, dopóki rekord DNS i ustawienie **Custom domain** nie będą gotowe.

## Polityka prywatności

Publiczny adres pozostaje bez zmian:

```text
https://pawelwielga.github.io/panstwa-miasta-website/privacy-policy/
```

Plik `privacy-policy/index.html` jest wersją używaną publicznie. Nie należy usuwać ani przenosić tej ścieżki bez równoczesnej aktualizacji Google Play Console.

Polityka opisuje zarówno LAN/hotspot, jak i tryb online 1.2.0: publiczną sygnalizację PeerJS, bezpośredni WebRTC DataChannel, brak własnego TURN, hosting klienta WWW na GitHub Pages oraz zależny od wariantu release zakres reklam Google AdMob.

## Powiązane repozytoria

- [`PawelWielga/panstwa-miasta`](https://github.com/PawelWielga/panstwa-miasta) — aplikacja Android, host i źródło prawdy dla gry.
- [`PawelWielga/panstwa-miasta-play`](https://github.com/PawelWielga/panstwa-miasta-play) — produkcyjny klient WWW dołączający do hosta Android.

## Materiały do uzupełnienia przy publikacji Androida

Po udostępnieniu wersji sklepowej należy:

1. podmienić nieaktywne CTA na prawdziwy link Google Play,
2. potwierdzić informację o cenie w FAQ,
3. zastąpić schematyczne makiety prawdziwymi screenshotami z aktualnej wersji aplikacji.
