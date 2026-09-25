# Changelog

Alle nennenswerten Änderungen am CSS-Atlas. Die Einträge beschreiben, was das Projekt
danach kann bzw. was sich für den Nutzer ändert – kein Commit-Protokoll.

**Regel:** Jeder Commit bekommt seinen Eintrag, im selben Commit. Neues kommt oben unter
„Unveröffentlicht“ dazu; beim Release wird daraus ein Abschnitt mit Versionsnummer und Datum.

Kategorien: **Neu** (neue Funktionen), **Verbessert** (bestehendes Verhalten), **Behoben**
(Fehler), **Intern** (Struktur, Tooling, nicht sichtbar).

## Unveröffentlicht

### Neu
- Abschnitt „Die Schwester-Apps“ im Überblick: Kacheln zu Daumenregel und ARIA-Kompass,
  beide mit Symbol für externe Links. Auch der Daumenregel-Link oben trägt das Symbol.
- Zweisprachig: alle Einträge, Vorschauen, Hinweise und Messwerte auf Deutsch und Englisch.
  Ein Link oben rechts wechselt die Sprache; sie steht als `?lang=en` in der Adresse und wird
  gemerkt. Links zur Daumenregel tragen die Sprache mit.
- Ein Klick auf das Logo führt zum Überblick.
- CSS-Atlas als eigene App: 53 CSS-Eigenschaften und Selektoren in neun Kapiteln, jeweils
  mit Live-Vorschau, CSS-Code mit hervorgehobener Zeile, Tailwind-Klasse und MDN-Link,
  fast immer auch mit einer Stolperfalle.
- Seitenleiste wie in einer Doku: Kapitel als Überschrift, jede Eigenschaft direkt
  anspringbar, Suche mit `Strg+K`.
- Eigene Adresse für jeden Eintrag (`#flex/justify-content`), Kurzform `#gap` springt ins
  richtige Kapitel.
- Überblick mit durchsuchbarer Tabelle aller Einträge.

### Verbessert
- Klassennamen in den Vorschauen sind jetzt englisch (`.card` statt `.karte`), wie in
  echtem Code üblich.

### Behoben
- Auf schmalen Bildschirmen ist die Kopfleiste wieder so breit wie das Display: Das Symbol für
  externe Links am Daumenregel-Link ließ „CSS-Atlas“ umbrechen und die Seite 14 px seitlich
  überstehen. Unter 480 px entfällt das Symbol dort; „(andere App)“ bleibt für Screenreader.
- Fachliche Durchsicht aller 53 Einträge: Hinweise, die noch aus der Daumenregel stammten
  (Markenwechsel, `.seg`), `scroll-snap-type` statt `scroll-snap`, eine gültige
  `:nth-child`-Stolperfalle, fehlende Farbe bei einer Outline-Klasse und der MDN-Link zu den
  Kombinatoren.

