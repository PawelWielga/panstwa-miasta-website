# Państwa Miasta Website

Oficjalna strona internetowa gry **Państwa Miasta**.

Docelowy adres:

```text
https://panstwamiasta.dihor.pl
```

## Status projektu

Repozytorium udostępnia obecnie publiczną politykę prywatności wymaganą przez Google Play Console. Strona główna przekierowuje jeszcze do dokumentu polityki prywatności.

Docelowo repozytorium będzie zawierało pełny landing page gry.

## Zakres

Planowana strona będzie zawierać:

- opis gry i jej najważniejszych funkcji,
- instrukcję rozpoczęcia rozgrywki,
- zrzuty ekranu,
- odnośnik do aplikacji w Google Play,
- odnośnik do klienta przeglądarkowego,
- sekcję FAQ i pomoc,
- politykę prywatności.

Klient przeglądarkowy gry rozwijany jest osobno w repozytorium [`PawelWielga/panstwa-miasta-play`](https://github.com/PawelWielga/panstwa-miasta-play).

## Obecna struktura

```text
.
├── index.html
├── privacy-policy/
│   └── index.html
├── docs/
│   └── privacy-policy.md
├── .nojekyll
└── README.md
```

- `index.html` przekierowuje obecnie do polityki prywatności.
- `privacy-policy/index.html` jest publiczną wersją dokumentu.
- `docs/privacy-policy.md` zawiera źródłową wersję polityki.
- `.nojekyll` wyłącza przetwarzanie strony przez Jekyll.

## Uruchomienie lokalne

Strona jest statyczna. Można ją uruchomić dowolnym lokalnym serwerem HTTP, na przykład:

```bash
python -m http.server 8080
```

Następnie otwórz:

```text
http://localhost:8080
```

Nie otwieraj plików wyłącznie przez `file://`, ponieważ zachowanie ścieżek i przekierowań może różnić się od hostingu HTTP.

## GitHub Pages

Repozytorium jest przeznaczone do publikacji przez GitHub Pages.

Konfiguracja dla obecnej statycznej wersji:

1. Otwórz **Settings → Pages**.
2. W sekcji **Build and deployment** wybierz **Deploy from a branch**.
3. Wskaż branch `main` oraz katalog `/ (root)`.
4. Zapisz ustawienia i poczekaj na publikację.

Po podpięciu własnej domeny docelowym adresem strony będzie:

```text
https://panstwamiasta.dihor.pl
```

Rekord DNS i pole **Custom domain** w ustawieniach GitHub Pages wymagają ręcznej konfiguracji. Po podpięciu domeny należy również włączyć **Enforce HTTPS**.

## Polityka prywatności

Publiczna ścieżka polityki prywatności pozostaje częścią tego repozytorium:

```text
/privacy-policy/
```

Nie należy usuwać ani zmieniać tej ścieżki bez równoczesnego zaktualizowania adresu w Google Play Console.

## Powiązane repozytoria

- [`PawelWielga/panstwa-miasta`](https://github.com/PawelWielga/panstwa-miasta) — aplikacja mobilna na Androida i logika gry.
- [`PawelWielga/panstwa-miasta-play`](https://github.com/PawelWielga/panstwa-miasta-play) — klient przeglądarkowy do dołączania do rozgrywki.

## Plan rozwoju

1. Zastąpienie przekierowania pełnym landing page.
2. Zachowanie polityki prywatności pod stałą ścieżką.
3. Dodanie responsywnego układu, treści i materiałów promocyjnych.
4. Dodanie SEO, Open Graph, favicon, `robots.txt` i `sitemap.xml`.
5. Podpięcie domeny `panstwamiasta.dihor.pl`.
6. Dodanie odnośnika do Google Play i gry WWW, gdy będą gotowe.
