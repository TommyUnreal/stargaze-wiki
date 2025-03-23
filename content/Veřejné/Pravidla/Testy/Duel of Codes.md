Duel of Codes je mechanika pro simulaci hackování počítačových systémů. Představuje střet mezi Hackerem a zabezpečeným Systémem, kde každý používá různé taktiky k dosažení svých cílů.

### Použitelné schopnosti:
- **Security Rigging**: [[#Code Injection (Injekce kódu)]], [[#Defensive Routing (Defenzivní přesměrování)]], [[#Exploit Execution (Provedení exploitu)]]
- **Signals**: [[#Signal Masking (Maskování signálu)]]
- **Security**: [[#Patch Analysis (Analýza záplat)]]
- **Science**: [[#Patch Analysis (Analýza záplat)]], [[#Deep Scan (Hluboký sken)]]
- **Engineering**: [[#System Misdirection (Systémové odvedení pozornosti)]], [[#Short Circuit (Zkrat)]]
- **Jurry-Riging**: [[#Short Circuit (Zkrat)]], [[#Manual Override]]
## Pravidla
### State Your Case (Prohlášení záměru)
- Hacker musí definovat svůj cíl (např. získat data, převzít kontrolu nad subsystémem, zanechat zadní vrátka).
- GM definuje, co se stane, pokud Systém vyhraje (např. spustí alarm, zablokuje účet, zavolá bezpečnostní personál). U systémů se sílou 5 a vyšší může být skrytý.

### Timeframe (Čas na hackování)
 - Hacker provede test statu *Perception* a počet úspěchů přičte k exponentu *Security Rigging*. Výsledek představuje  jeho čas na proniknutí do systému před tím, než bude odhalen nebo vyhozen.

### System's Strength
- Určí základní exponent *Security* systému. Připočte +1 za každý vybavený *Node*.
- Následuje seznam příkladů vybavení systému:
	- **Subsystem Layer**: Pouze přidá bod Síly Systému. Muže jich být vybaveno více.
	- **Firewall**: [[#Firewall Response (Reakce firewallu)]], [[#Proxy (Prostředník)]]
	- **Datový modul**: [[#Data Encryption (Šifrování dat)]], [[#System Lockdown (Uzamčení systému)]]
	- **Bezpečnostní modul**: [[#Trace Algorithm (Trasovací algoritmus)]], [[#Counter-Measure (Protiopatření)]]
	- **AI**: [[#Counter-Measure (Protiopatření)]], [[#Honeypot (Návnada)]]
	- **Zdroj energie**: [[#Power Surge (Výboj)]]
### Hacking
- Hackování probíhá v *výměnách*, každá obsahuje tři *akce*. V každém *výměně* si Hacker i Systém tajně vyberou tři akce.
- Pokud Síla Systému nebo čas klesne na 0 nebo níže duel končí.

### Akce Hackera
#### Code Injection (Injekce kódu)
**Test:** *Security Rigging* 
**Popis:** Hacker se pokusí vložit zlomyslný kód do systému. 
**Účinek:** _Útok_. Úspěchy se odečtou od Síly Systému.
#### Defensive Routing (Defenzivní přesměrování)
**Test:** *Security Rigging* 
**Popis:** Hacker přesměruje svou datovou stopu přes několik serverů. 
**Účinek:** _Obrana_. Proti oponentově akci se provede test a úspěchy se odečtou od jeho hodu. Poskytuje imunitu proti _Power Surge_.
#### Exploit Execution (Provedení exploitu)
**Test:** *Security Rigging*
**Popis:** Hacker objeví a využije kritickou zranitelnost. 
**Účinek:** _Speciální_. Test proti obtížnosti rovné exponentu Security systému. Úspěch způsobí, že Systém vynechá svou další akci a obdrží 1 zásah.
#### Signal Masking (Maskování signálu)
**Test:** *Signals*
**Popis:** Hacker skrývá svou digitální stopu. 
**Účinek:** _Obrana_. Úspěchy se odečtou od útočné akce Systému. Úspěšná obrana přidá +1 k Času Hackera. Poskytuje imunitu proti _Power Surge_.
#### Patch Analysis (Analýza záplat)
**Test:** *Security* / *Science* 
**Popis:** Hacker analyzuje systémové záplaty a hledá slabá místa. 
**Účinek:** _Útok/Obrana_. Rozdělte kostky na dva pooly. Obranné úspěchy se odečtou od útoku Systému, útočné úspěchy fungují jako *Code Injection*.
#### Deep Scan (Hluboký sken)
**Test:** *Science*
**Popis:** Hacker provede důkladnou analýzu systémových procesů. 
**Účinek:** _Speciální_. Versus test proti jakékoliv akci Systému. Pokud je úspěšný, Hacker získá +1🎲 na své další akce a také se dozví seznam Nodů v systému. Poskytuje imunitu proti _Honeypot_.
#### System Misdirection (Systémové odvedení pozornosti)
**Test:** *Engineering*
**Popis:** Hacker odvede pozornost systému falešnými hrozbami. 
**Účinek:** _Obrana_. Úspěchy se odečtou od útočné akce Systému. Poskytuje imunitu proti _Counter-Measure_. Úspěch umožňuje volný zásah v příští akci.
#### Short Circuit (Zkrat)
**Test:** *Engineering* / *Jury-Rigging*
**Popis:** Hacker zkratuje nějaký z podsystémů.
**Účinek:** _Speciální_. Versus test proti jakékoliv akci Systému. Pokud je úspěšný, Systém obdrží jeden zásah a Hacker deaktivuje jeden náhodný node.
#### Manual Override
**Test:** *Jury-Rigging*
**Popis:** Hacker ručně převede ovládání některých podsystémů.
**Účinek:** _Útok_. Úspěchy se odečtou od Síly Systému. Je-li útok úspěšní, dá 1 zranění navíc. Je-li provedena proti *System Lockdown*, hacker ztratí dvě akce. Je-li provedena proti *Power Surge*, Hacker obdrží 2 body [[Zranění]].

### Akce Systému
#### Autorecovery (Automatická Obnova)
**Test:** Security
**Node:** -
**Popis:** Systém se pokusí obnovit své systémy.
**Účinek:** _Obrana_. Versus test proti akci Hackera. Pokud Systém uspěje, Systém si obnoví 1 body Síly Systému.
#### Firewall Response (Reakce firewallu)
**Test:** Security 
**Node:** Firewall
**Popis:** Systém aktivuje obranný firewall k blokování škodlivých příkazů. 
**Účinek:** _Obrana_. Úspěchy se odečtou od útočné akce Hackera.
#### Proxy (Prostředník)
**Test:** Security
**Node:** Firewall
**Popis:** Hacker se musí dostat skrz proxy k dalším systémům.
**Účinek:** _Obrana_. Systém nemůže být zraněn za více než 1 bod Síly Systému.
#### Data Encryption (Šifrování dat)
**Test:** Security
**Node:** Datový modul
**Popis:** Systém rychle zašifruje citlivá data. **Účinek:** _Speciální_. Versus test proti akci Hackera. Pokud Systém uspěje, Hacker ztrácí -1🎲 na své další akce.
#### System Lockdown (Uzamčení systému)
**Test:** Security
**Node:** Datový modul
**Popis:** Systém uzamkne napadené části. 
**Účinek:** _Speciální_. Versus test proti akci Hackera. Pokud obránce prohraje, zaváhá a ztratí příští akci.
#### Trace Algorithm (Trasovací algoritmus)
**Test:** Security 
**Node:** Bezpečnostní modul
**Popis:** Systém se pokusí vystopovat zdroj útoku. 
**Účinek:** _Útok_. Testuje se proti obtížnosti rovné exponentu Security Rigging Hackera. Úspěch zkrátí čas o 3.
#### Counter-Measure (Protiopatření)
**Test:** Security 
**Node:** Bezpečnostní modul / AI
**Popis:** Systém spustí aktivní protiopatření. 
**Účinek:** _Útok_. Úspěchy se odečtou od Síly Hackera.
#### Honeypot (Návnada)
**Test:** Security
**Node:** AI
**Popis:** Systém naláká Hackera do falešné části systému. 
**Účinek:** _Speciální/obrana_. Versus test proti jakékoliv akci Hackera. Je-li systém úspěšný, Hacker ztratí polovinu času (zaokrouhleno nahoru) a Systém 3 body Síly Systému.
#### Power Surge (Výboj)
**Test:** Security
**Node:** Zdroj energie
**Popis:** Systém záměrně nechá projít útok, ale vyšle zpětný výboj. **Účinek:** _Speciální_. Systém ignoruje útok Hackera, ale způsobí fyzické [[Zranění]]. a odečte z Času Hackera.

## Vyhodnocení
- Pokud Síla Systému klesne na 0 nebo níže před vypršením Času, Hacker získává to, co bylo stanoveno v Prohlášení záměru.
- Pokud vyprší Čas vyhrává Systém.
- Pokud obě hodnoty klesnou na 0 čí níže ve stejné akci, je to remíza. V té obě strany získávají svůj záměr. Např. Hacker stáhne data ale Systém spustí tichý alarm.