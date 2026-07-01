# Polityka prywatności aplikacji Państwa Miasta

Data ostatniej aktualizacji: 1 lipca 2026 r.

Ta polityka prywatności opisuje, jakie dane mogą być przetwarzane podczas korzystania z aplikacji **Państwa Miasta** oraz w jakim celu są używane.

Przed opublikowaniem tej treści jako publicznej polityki prywatności uzupełnij dane wydawcy i kontakt.

- Aplikacja: **Państwa Miasta**
- Identyfikator aplikacji Android: `app.dihor.panstwamiasta`
- Administrator / wydawca: **[UZUPEŁNIJ NAZWĘ WYDAWCY LUB IMIĘ I NAZWISKO]**
- Kontakt w sprawach prywatności: **[UZUPEŁNIJ ADRES E-MAIL]**

## 1. Jak działa aplikacja

**Państwa Miasta** to gra słowna na Androida. Podstawowa rozgrywka multiplayer działa lokalnie, w tej samej sieci Wi-Fi albo przez hotspot. Aplikacja nie wymaga konta użytkownika, logowania ani rejestracji.

Aplikacja nie posiada własnego systemu kont i nie wysyła danych rozgrywki na backend gry. Dane potrzebne do gry są przetwarzane lokalnie na urządzeniu oraz, w trybie multiplayer, przesyłane między urządzeniami uczestników znajdujących się w tym samym pokoju gry.

Aplikacja może korzystać z internetu do wyświetlania reklam, obsługi zgód reklamowych oraz pobrania zdalnej konfiguracji reklam, jeśli reklamy są włączone w danym buildzie.

## 2. Jakie dane mogą być przetwarzane

Aplikacja może przetwarzać następujące dane:

### Dane podane przez użytkownika

- nazwa gracza albo pseudonim wpisany w aplikacji,
- odpowiedzi wpisywane w trakcie rundy,
- decyzje dotyczące oceny odpowiedzi innych graczy,
- ustawienia aplikacji, na przykład preferencje gry lub dźwięku.

Nie wymagamy podawania imienia i nazwiska, adresu e-mail, numeru telefonu ani innych danych kontaktowych.

### Dane lokalnej rozgrywki multiplayer

Podczas gry w sieci lokalnej aplikacja może przetwarzać i przesyłać między urządzeniami uczestników:

- nazwę gracza,
- identyfikator gracza używany w bieżącej sesji,
- kod pokoju,
- identyfikator pokoju,
- adres IP i port hosta potrzebne do połączenia lokalnego,
- stan gry, kategorię, literę, odpowiedzi, oceny i wyniki,
- informacje techniczne potrzebne do utrzymania połączenia, takie jak heartbeat i status połączenia.

Te dane są używane po to, aby uczestnicy mogli dołączyć do tej samej gry, widzieć wspólny stan rozgrywki i kontynuować grę po chwilowej utracie połączenia.

### Dane zapisane na urządzeniu

Aplikacja może zapisywać lokalnie na urządzeniu dane potrzebne do działania gry, na przykład nazwę gracza, ustawienia oraz dane aktywnej lub ostatniej sesji. Dane te pozostają na urządzeniu użytkownika i mogą zostać usunięte przez wyczyszczenie danych aplikacji albo odinstalowanie aplikacji.

### Dane techniczne urządzenia i reklam

Jeżeli reklamy są włączone, aplikacja korzysta z Google Mobile Ads SDK / Google AdMob. W takim przypadku Google i jego partnerzy reklamowi mogą przetwarzać dane techniczne urządzenia i użycia aplikacji, na przykład identyfikator reklamowy urządzenia, adres IP, przybliżoną lokalizację wynikającą z adresu IP, informacje o urządzeniu, informacje o aplikacji oraz interakcje z reklamami.

Zakres danych przetwarzanych przez Google zależy od konfiguracji reklam, regionu użytkownika, ustawień prywatności oraz zgód wyrażonych przez użytkownika. Więcej informacji znajduje się w politykach Google:

- https://policies.google.com/privacy
- https://policies.google.com/technologies/ads

## 3. Kamera i skanowanie kodów QR

Aplikacja może poprosić o dostęp do aparatu, gdy użytkownik wybierze dołączanie do pokoju przez zeskanowanie kodu QR.

Kamera jest używana wyłącznie do odczytania kodu QR z danymi pokoju gry, takimi jak adres hosta, port i kod pokoju. Aplikacja nie zapisuje zdjęć ani nagrań z aparatu i nie wysyła obrazu z kamery do wydawcy aplikacji.

Skanowanie QR jest opcjonalne. Użytkownik może dołączyć do gry ręcznie, wpisując dane pokoju.

## 4. Powiadomienia i działanie gry w tle

Podczas aktywnej gry multiplayer aplikacja może uruchomić usługę działającą w tle jako Android Foreground Service. Służy ona do utrzymania lokalnego pokoju gry i połączenia między urządzeniami, gdy aplikacja zostanie zminimalizowana.

W takim przypadku system Android pokazuje stałe powiadomienie dotyczące aktywnej gry. Powiadomienie może zawierać podstawowe informacje o pokoju, hoście, liczbie graczy lub statusie rozgrywki.

Usługa działa tylko podczas aktywnej sesji gry i jest zatrzymywana po opuszczeniu pokoju albo zakończeniu aktywnej sesji.

## 5. Reklamy i zgody użytkownika

Aplikacja może wyświetlać reklamy Google AdMob. Reklamy mogą być personalizowane albo niepersonalizowane, zależnie od regionu, konfiguracji oraz zgód użytkownika.

Aplikacja może używać Google User Messaging Platform, aby wyświetlić formularz zgody lub opcje prywatności wymagane dla reklam. Użytkownik może zobaczyć komunikat dotyczący prywatności przed załadowaniem reklam albo w innym momencie wymaganym przez konfigurację Google.

Jeżeli użytkownik nie wyrazi wymaganej zgody albo zgoda nie jest dostępna, aplikacja może nie ładować reklam lub wyświetlać reklamy w ograniczonym zakresie, zależnie od konfiguracji Google i aplikacji.

## 6. Zdalna konfiguracja reklam

Aplikacja może pobrać z publicznego adresu HTTPS konfigurację reklam, na przykład informację, czy reklamy są włączone oraz jaki identyfikator jednostki reklamowej ma zostać użyty.

Taka konfiguracja nie wymaga konta użytkownika. Podczas pobierania konfiguracji serwer obsługujący ten adres może otrzymać standardowe dane techniczne połączenia, takie jak adres IP, czas żądania i informacje o kliencie HTTP. Dane te mogą pojawić się w logach technicznych serwera zgodnie z konfiguracją hostingu używanego przez wydawcę.

## 7. Komu mogą być udostępniane dane

Dane rozgrywki multiplayer są udostępniane uczestnikom tego samego pokoju gry w lokalnej sieci. Przykładowo inni gracze mogą widzieć nazwę gracza, odpowiedzi, oceny i wyniki.

Dane techniczne i reklamowe mogą być przetwarzane przez Google i jego partnerów reklamowych, jeżeli reklamy są włączone. Szczegóły opisują polityki Google wskazane wyżej.

Nie sprzedajemy danych osobowych użytkowników.

## 8. Uprawnienia Androida używane przez aplikację

Aplikacja może korzystać z następujących uprawnień Androida:

- `INTERNET` - do komunikacji sieciowej, w tym połączeń lokalnych multiplayer, reklam oraz pobrania konfiguracji reklam,
- `ACCESS_NETWORK_STATE` - do sprawdzenia stanu połączenia sieciowego,
- `CAMERA` - do opcjonalnego skanowania kodu QR pokoju,
- `POST_NOTIFICATIONS` - do pokazania powiadomienia aktywnej gry na Androidzie 13 i nowszych,
- `FOREGROUND_SERVICE` oraz `FOREGROUND_SERVICE_DATA_SYNC` - do utrzymania aktywnej gry multiplayer podczas działania aplikacji w tle.

## 9. Jak długo przechowujemy dane

Dane zapisane lokalnie w aplikacji są przechowywane tak długo, jak jest to potrzebne do działania aplikacji albo do czasu ich usunięcia przez użytkownika, na przykład przez wyczyszczenie danych aplikacji lub odinstalowanie aplikacji.

Dane aktywnej gry są używane w czasie trwania sesji. Po opuszczeniu pokoju albo zakończeniu gry aplikacja nie potrzebuje ich do dalszego działania, z wyjątkiem danych, które mogą zostać zapisane lokalnie jako ustawienia lub dane ułatwiające ponowne połączenie z aktywną sesją.

Dane przetwarzane przez Google w ramach reklam są przechowywane zgodnie z politykami i ustawieniami Google.

## 10. Bezpieczeństwo

Aplikacja ogranicza przetwarzanie danych do funkcji potrzebnych do gry, lokalnej komunikacji multiplayer, reklam i podstawowej konfiguracji. Dane lokalnej rozgrywki są przesyłane między urządzeniami w tej samej sieci lokalnej.

Połączenia w lokalnej sieci LAN/hotspot mogą nie korzystać z szyfrowania TLS, ponieważ służą bezpośredniej komunikacji między urządzeniami graczy w tej samej sieci. Nie należy używać gry w niezaufanych sieciach, jeśli użytkownik nie chce ujawniać nazwy gracza, odpowiedzi lub danych pokoju innym osobom mającym dostęp do tej sieci.

Połączenia do zdalnej konfiguracji reklam powinny używać HTTPS.

## 11. Dzieci i rodziny

Aplikacja jest prostą grą słowną, która może być używana przez graczy w różnym wieku. Nie prosimy użytkowników o podawanie danych kontaktowych ani danych identyfikujących.

Jeżeli aplikacja jest publikowana jako skierowana do dzieci lub rodzin, wydawca powinien skonfigurować Google Play Console, AdMob oraz reklamy zgodnie z faktyczną grupą odbiorców i obowiązującymi wymaganiami Google Play.

Rodzic lub opiekun może skontaktować się z wydawcą pod adresem wskazanym w tej polityce, jeśli uważa, że dziecko przekazało dane, które powinny zostać usunięte.

## 12. Prawa użytkownika

W zależności od miejsca zamieszkania użytkownik może mieć prawo do uzyskania informacji o przetwarzaniu danych, dostępu do danych, sprostowania danych, usunięcia danych, ograniczenia przetwarzania albo sprzeciwu wobec przetwarzania.

W sprawach dotyczących prywatności można skontaktować się z wydawcą aplikacji pod adresem: **[UZUPEŁNIJ ADRES E-MAIL]**.

Dane zapisane lokalnie w aplikacji można usunąć przez wyczyszczenie danych aplikacji w ustawieniach Androida albo przez odinstalowanie aplikacji.

## 13. Zmiany polityki prywatności

Polityka prywatności może być aktualizowana, gdy zmieni się działanie aplikacji, zakres przetwarzanych danych, konfiguracja reklam albo wymagania prawne. Aktualna wersja polityki powinna być dostępna publicznie pod linkiem podanym w Google Play Console.
