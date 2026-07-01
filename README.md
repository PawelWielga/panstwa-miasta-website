# Państwa Miasta Website

Publiczna strona dla aplikacji **Państwa Miasta**.

Repozytorium udostępnia politykę prywatności potrzebną do Google Play Console.

## Jak włączyć GitHub Pages

1. Wejdź w repozytorium `PawelWielga/panstwa-miasta-website`.
2. Otwórz **Settings**.
3. Wejdź w **Pages**.
4. W sekcji **Build and deployment** ustaw:
   - **Source**: `Deploy from a branch`,
   - **Branch**: `main`,
   - folder: `/ (root)`.
5. Kliknij **Save**.
6. Odczekaj chwilę, aż GitHub opublikuje stronę.

## Struktura

```text
index.html
privacy-policy/index.html
docs/privacy-policy.md
.nojekyll
```

`index.html` przekierowuje do publicznej strony polityki prywatności.

Bezpośredni URL do polityki po włączeniu GitHub Pages ma postać:

```text
https://pawelwielga.github.io/panstwa-miasta-website/privacy-policy/
```

Ten adres najlepiej wkleić w Google Play Console jako URL polityki prywatności.
