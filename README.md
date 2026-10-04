# Archivio Carte Fedeltà - Database

Database pubblico condiviso utilizzato dall'app **Archivio Carte Fedeltà**.

Contiene esclusivamente dati generici necessari al riconoscimento delle tessere:
- prefissi dei codici;
- nome dell'insegna;
- categoria;
- tipo e lunghezza del barcode;
- logo pubblico;
- eventuale immagine generica del fronte della tessera.

## Privacy

Questo repository **non deve contenere numeri completi di tessere personali**, nomi dei titolari o altri dati identificativi.

Le immagini condivise devono rappresentare soltanto il modello della tessera e non devono mostrare:
- nome del titolare;
- numero completo della tessera;
- barcode personale;
- QR code personale;
- altri dati identificativi.

## Database

Il file principale è:

`loyalty_prefixes.json`

Le nuove tessere possono essere proposte dall'app tramite issue `[PREFIX]` e `[PHOTO]`.
Una GitHub Action riservata all'account proprietario valida i dati e aggiorna automaticamente il database.

## Regola PREFIX

Per le nuove tessere, il prefisso corrisponde alla **prima metà del codice completo**, arrotondata per difetto quando la lunghezza è dispari.

Esempio:

`0403603405089` → prefisso `040360`
