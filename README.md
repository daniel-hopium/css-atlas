# CSS-Atlas – CSS zum Anfassen

53 CSS-Eigenschaften und Selektoren im Stil der Tailwind-Doku: Wert anklicken, Wirkung in
der Live-Vorschau sehen, darunter das CSS mit hervorgehobener Zeile und die passende
Tailwind-Klasse. Auf Deutsch und Englisch.

Online: https://daniel-hopium.github.io/css-atlas/

## Starten

`index.html` im Browser öffnen, per Doppelklick. Kein Build, kein Server, keine
Abhängigkeiten. Internet braucht es nur für die Google-Schriften.

## Inhalt

Neun Kapitel:

| Kapitel | Beispiele |
|---|---|
| Layout & Position | `display`, `position`, `z-index`, `overflow` |
| Flexbox | `flex-direction`, `justify-content`, `align-items`, `gap`, `flex` |
| Grid | `grid-template-columns`, `grid-column`, `place-items` |
| Box & Größe | Box Model, Margin Collapsing, `max-width`, `aspect-ratio` |
| Typografie | `font-size`, `line-height`, `text-overflow`, `white-space` |
| Rahmen & Effekte | `border-radius`, `box-shadow`, `filter`, vier Arten zu verstecken |
| Transform & Transition | `transform`, `transform-origin`, `transition` |
| Interaktion | `cursor`, `pointer-events`, `scroll-snap-type`, `accent-color` |
| Selektoren | Kombinatoren, `:nth-child`, `:has()`, Attribute, Spezifität |

Jeder Eintrag hat einen MDN-Link und eine eigene Adresse (`#flex/justify-content`),
fast alle auch eine Stolperfalle. Die Kurzform `#gap` springt ins richtige Kapitel. Der
Überblick hat eine durchsuchbare Tabelle aller Einträge.

## Bedienung

- **Sprache:** Der Link oben rechts („English“ / „Deutsch“) wechselt die Sprache. Sie steht
  als `?lang=en` in der Adresse (teilbar), wird im `localStorage` gemerkt und folgt sonst der
  Browsersprache.
- `Strg+K` (Mac: `Cmd+K`) springt in die Suche der Seitenleiste.
- Jeder Eintrag und jedes Kapitel hat eine eigene Adresse; der Zurück-Button funktioniert.
- Hell und dunkel folgen der Systemeinstellung.
- Das Logo führt zum Überblick.

## Aufbau

Alles steckt in einer Datei:

- **`CA_CATS`**: die neun Kapitel.
- **`CSSA`**: ein Objekt pro Eintrag – Vorschau-HTML (`stage`), Werte (`vals`) mit
  Tailwind-Klasse und Hinweis, optional `measure()` für Messwerte und `mode` für
  Selektoren (`sel`) oder ganze Regeln (`css`).
- **`caApply()`**: setzt den gewählten Wert per `style.setProperty` oder als
  `<style>`-Regel auf die Vorschau und baut daraus den Code-Block.
- **Router**: Hash-Routing (`#kapitel/eintrag`), Fokus nach jedem Wechsel auf die
  Überschrift.
- **Zweisprachig:** `tx('Deutsch','English')` steht direkt neben jedem Text und liefert die
  Sprache des Seitenaufrufs. Der Umschalter lädt die Seite neu – so darf `tx()` auch in
  Daten stehen, die beim Start einmal ausgewertet werden. `LOCALE` (`de-AT` / `en-US`) steuert
  `Intl` für Zahlen und Daten. Wer einen deutschen Text ändert, sieht die englische Fassung
  daneben und passt sie mit an.
  Klassennamen in den Vorschauen sind englisch (`.card`, `.list`), weil sie als Code
  angezeigt werden und Code auf Englisch geschrieben wird.

Entstanden als Teil von [Daumenregel](https://daniel-hopium.github.io/pattern-library/),
der UI-Pattern-Library; einige Einträge verlinken dorthin.
