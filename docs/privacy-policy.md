# Polityka prywatności aplikacji Państwa Miasta

Data ostatniej aktualizacji: 23 sierpnia 2026 r.

Ta polityka opisuje dane przetwarzane podczas korzystania z aplikacji **Państwa Miasta**, lokalnego multiplayera oraz trybu online dostępnego od wersji 1.2.0.

- Aplikacja: **Państwa Miasta**
- Identyfikator aplikacji Android: `app.dihor.panstwamiasta`
- Administrator / wydawca: **Paweł Wielga**
- Kontakt w sprawach prywatności: przez dane kontaktowe wydawcy podane w Google Play albo przez publiczny profil GitHub [PawelWielga](https://github.com/PawelWielga).

## 1. Jak działa aplikacja

**Państwa Miasta** to gra słowna z hostem działającym na Androidzie. Gra może działać lokalnie w tej samej sieci Wi-Fi lub przez hotspot. Od wersji 1.2.0 host może również udostępnić pokój online, a pozostali gracze mogą dołączyć przez zgodny klient WWW.

Aplikacja nie wymaga konta użytkownika, logowania ani rejestracji. Nie utrzymujemy własnego backendu przechowującego stan rozgrywki ani bazy aktywnych pokojów. Aplikacja Android hosta pozostaje źródłem prawdy dla stanu gry, rund, odpowiedzi, ocen i punktacji.

W trybie online publiczna usługa PeerJS służy do sygnalizacji potrzebnej do zestawienia połączenia WebRTC. Po zestawieniu połączenia dane gry są przesyłane bezpośrednio między uczestnikami przez WebRTC DataChannel. Projekt nie używa własnego serwera TURN.

Aplikacja może dodatkowo korzystać z internetu do wyświetlania reklam, obsługi zgód reklamowych oraz pobrania zdalnej konfiguracji reklam, jeśli reklamy są włączone w danym buildzie.

## 2. Jakie dane mogą być przetwarzane

### Dane podane przez użytkownika

- nazwa gracza albo pseudonim wpisany w aplikacji lub kliencie WWW,
- odpowiedzi wpisywane w trakcie rundy,
- decyzje i oceny związane z odpowiedziami,
- ustawienia aplikacji oraz rozgrywki.

Nie wymagamy podawania imienia i nazwiska, adresu e-mail, numeru telefonu ani innych danych kontaktowych.

### Dane lokalnej rozgrywki multiplayer

Podczas gry w sieci lokalnej aplikacja może przetwarzać i przesyłać między urządzeniami uczestników:

- nazwę i identyfikator gracza używany przez grę,
- kod i identyfikator pokoju,
- adres IP i port hosta potrzebne do połączenia lokalnego,
- stan gry, kategorie, literę, odpowiedzi, oceny, statystyki i wyniki,
- informacje techniczne potrzebne do utrzymania połączenia, takie jak heartbeat, identyfikatory żądań i status połączenia.

### Dane rozgrywki online i WebRTC

W trybie online mogą być przetwarzane dane potrzebne do odnalezienia hosta, uwierzytelnienia sesji i zestawienia bezpośredniego połączenia:

- sześci znakowy kod pokoju i wyprowadzone z niego techniczne identyfikatory sesji PeerJS,
- identyfikatory połączeń i dane sygnalizacyjne PeerJS,
- informacje ICE i sieciowe wymagane przez WebRTC, które zgodnie z działaniem tej technologii mogą obejmować adresy IP lub inne dane potrzebne do zestawienia połączenia,
- nazwę i identyfikator gracza, dane reconnectu aktywnej sesji oraz dane rozgrywki wymienione wyżej.

Publiczna usługa PeerJS uczestniczy w sygnalizacji połączenia. Dane samej rozgrywki po zestawieniu bezpośredniego DataChannel nie są przekazywane przez własny backend gry. Informacje o działaniu PeerJS Cloud są dostępne w [dokumentacji PeerJS](https://peerjs.com/server/cloud).

### Dane zapisane na urządzeniu

Aplikacja może zapisywać lokalnie nazwę gracza, ustawienia, dane aktywnej lub ostatniej sesji, dane potrzebne do reconnectu oraz lokalny draft odpowiedzi. Dane te służą do działania aplikacji i wznowienia niedokończonej gry.

### Dane klienta WWW i hostingu GitHub Pages

Produkcyjny klient WWW jest statyczną stroną hostowaną przez GitHub Pages. Podczas otwierania strony dostawca hostingu może przetwarzać standardowe dane techniczne żądania internetowego zgodnie ze swoimi zasadami, na przykład adres IP, informacje o przeglądarce, czas żądania i informacje potrzebne do zapewnienia bezpieczeństwa oraz działania usługi. Aktualne zasady GitHub są dostępne w [centrum polityk prywatności GitHub](https://docs.github.com/en/site-policy/privacy-policies).

### Dane techniczne urządzenia i reklam

Jeżeli reklamy są włączone, aplikacja korzysta z Google Mobile Ads SDK / Google AdMob. W takim przypadku Google i jego partnerzy reklamowi mogą przetwarzać dane techniczne urządzenia i użycia aplikacji, na przykład identyfikator reklamowy urządzenia, adres IP, przybliżoną lokalizację wynikającą z adresu IP, informacje o urządzeniu, informacje o aplikacji oraz interakcje z reklamami.

Zakres danych przetwarzanych przez Google zależy od konfiguracji reklam, regionu użytkownika, ustawień prywatności oraz zgód. Więcej informacji:

- [Polityka prywatności Google](https://policies.google.com/privacy)
- [Technologie reklamowe Google](https://policies.google.com/technologies/ads)

## 3. Kamera i skanowanie kodów QR

Aplikacja może poprosić o dostęp do aparatu, gdy użytkownik wybierze dołączanie do pokoju przez zeskanowanie kodu QR.

Kod QR może zawierać dane potrzebne do dołączenia do pokoju lokalnego lub online. Aplikacja nie zapisuje zdjęć ani nagrań z aparatu i nie wysyła obrazu z kamery do wydawcy aplikacji.

Skanowanie QR jest opcjonalne. Użytkownik może skorzystać z innych dostępnych metod dołączenia.

## 4. Powiadomienia i działanie gry w tle

Podczas aktywnej gry multiplayer aplikacja Android może uruchomić Foreground Service, aby utrzymać aktywną sesję po zminimalizowaniu aplikacji.

System Android pokazuje wtedy stałe powiadomienie dotyczące aktywnej gry. Powiadomienie może zawierać podstawowe informacje o pokoju, hoście, liczbie graczy lub statusie rozgrywki.

Usługa działa tylko podczas aktywnej sesji gry i jest zatrzymywana po opuszczeniu pokoju albo zakończeniu sesji.

## 5. Reklamy i zgody użytkownika

Aplikacja może wyświetlać reklamy Google AdMob. Reklamy mogą być personalizowane albo niepersonalizowane, zależnie od regionu, konfiguracji oraz zgód użytkownika.

Aplikacja może używać Google User Messaging Platform, aby wyświetlić formularz zgody lub opcje prywatności wymagane dla reklam. Jeżeli wymagane warunki nie są spełnione, aplikacja może nie ładować reklam lub wyświetlać je w ograniczonym zakresie zgodnie z konfiguracją Google i aplikacji.

## 6. Zdalna konfiguracja reklam

Aplikacja może pobrać z publicznego adresu HTTPS konfigurację reklam, na przykład informację, czy reklamy są włączone oraz jaki identyfikator jednostki reklamowej ma zostać użyty.

Podczas pobierania konfiguracji serwer obsługujący ten adres może otrzymać standardowe dane techniczne połączenia, takie jak adres IP, czas żądania i informacje o kliencie HTTP, zgodnie z konfiguracją użytego hostingu.

## 7. Komu mogą być udostępniane dane

Dane rozgrywki są udostępniane uczestnikom tego samego pokoju w zakresie potrzebnym do wspólnej gry. Inni gracze mogą widzieć między innymi nazwę gracza, odpowiedzi, oceny i wyniki.

W trybie online techniczne dane sygnalizacyjne i połączeniowe są przetwarzane z udziałem publicznej usługi PeerJS oraz infrastruktury sieciowej potrzebnej do zestawienia WebRTC. Klient WWW jest dostarczany przez GitHub Pages.

Dane techniczne i reklamowe mogą być przetwarzane przez Google i jego partnerów reklamowych, jeżeli reklamy są włączone.

Nie sprzedajemy danych osobowych użytkowników.

## 8. Uprawnienia Androida używane przez aplikację

Aplikacja może korzystać z następujących uprawnień Androida:

- `INTERNET` - do komunikacji multiplayer lokalnej i online oraz, zależnie od wariantu, reklam i konfiguracji reklam,
- `ACCESS_NETWORK_STATE` - do sprawdzenia stanu połączenia sieciowego,
- `CHANGE_NETWORK_STATE` - jako warunek systemowy dla foreground service utrzymującego połączenie sieciowe z innymi urządzeniami,
- `CAMERA` - do opcjonalnego skanowania kodu QR pokoju,
- `POST_NOTIFICATIONS` - do pokazania powiadomienia aktywnej gry na Androidzie 13 i nowszych,
- `FOREGROUND_SERVICE` oraz `FOREGROUND_SERVICE_CONNECTED_DEVICE` - do utrzymania aktywnej sesji multiplayer wymagającej ciągłego połączenia z innymi urządzeniami.

## 9. Jak długo przechowujemy dane

Dane zapisane lokalnie w aplikacji są przechowywane tak długo, jak jest to potrzebne do działania aplikacji albo do czasu ich usunięcia przez użytkownika, na przykład przez wyczyszczenie danych aplikacji lub odinstalowanie aplikacji.

Dane aktywnej gry są używane podczas sesji. Część minimalnych danych potrzebnych do reconnectu lub wznowienia niedokończonej sesji może pozostać lokalnie po restarcie procesu aplikacji.

Retencja danych przetwarzanych przez PeerJS Cloud, GitHub Pages, Google Mobile Ads oraz inne usługi zewnętrzne podlega zasadom tych usług.

## 10. Bezpieczeństwo

W trybie LAN/hotspot komunikacja może korzystać z lokalnego cleartext WebSocket bez TLS. Z tego powodu nie należy używać lokalnej gry w niezaufanej sieci, jeśli użytkownik nie chce ujawniać danych pokoju lub rozgrywki osobom mającym dostęp do tej sieci.

Połączenia WebRTC używane w trybie online są szyfrowane przez mechanizmy transportowe WebRTC. Sygnalizacja potrzebna do zestawienia połączenia odbywa się przez publiczną usługę PeerJS. Projekt używa bezpośredniego P2P i nie utrzymuje własnego serwera TURN.

Połączenia do klienta WWW i zdalnej konfiguracji używają HTTPS.

## 11. Dzieci i rodziny

Aplikacja jest prostą grą słowną, która może być używana przez graczy w różnym wieku. Nie prosimy użytkowników o podawanie danych kontaktowych ani o zakładanie konta.

Konfiguracja Google Play, grupy odbiorców oraz reklam musi odpowiadać faktycznemu wariantowi opublikowanej aplikacji i obowiązującym wymaganiom Google Play.

Rodzic lub opiekun może skontaktować się z wydawcą przez dane kontaktowe podane w tej polityce, jeśli uważa, że dziecko przekazało dane, które powinny zostać usunięte.

## 12. Prawa użytkownika

W zależności od miejsca zamieszkania użytkownik może mieć prawo do uzyskania informacji o przetwarzaniu danych, dostępu do danych, sprostowania danych, usunięcia danych, ograniczenia przetwarzania albo sprzeciwu wobec przetwarzania.

W sprawach dotyczących prywatności można skontaktować się z wydawcą przez dane kontaktowe podane w Google Play albo przez publiczny profil GitHub [PawelWielga](https://github.com/PawelWielga).

Dane zapisane lokalnie w aplikacji można usunąć przez wyczyszczenie danych aplikacji w ustawieniach Androida albo przez odinstalowanie aplikacji.

## 13. Zmiany polityki prywatności

Polityka prywatności może być aktualizowana, gdy zmieni się działanie aplikacji, multiplayer, zakres przetwarzanych danych, dostawcy usług, konfiguracja reklam albo wymagania prawne. Aktualna wersja polityki pozostaje dostępna pod tym samym publicznym adresem używanym w Google Play Console.
