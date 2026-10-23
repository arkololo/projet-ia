# Lettre de mission : Audit de sécurité « HelpDesk-AI »

**Client :** Helvetia Systems SA, Direction des systèmes d'information (DSI)
**Prestataire :** votre équipe (cabinet de conseil en sécurité)
**Référence :** CPE-2026-REDTEAM-HELPDESK
**Date d'émission :** début de la mission (après le cours L7)

---

## 1. Contexte

Helvetia Systems SA a déployé un **agent d'assistance informatique interne**
(« HelpDesk-AI ») fondé sur un grand modèle de langage (LLM). L'agent répond aux
employés sur les comptes, les tickets, le VPN, les imprimantes et la base de
connaissances. Il dispose d'outils lui permettant d'agir : réinitialiser un mot
de passe, consulter l'annuaire, rechercher des tickets, envoyer un courriel,
interroger la base de connaissances, et un module de traduction fourni par un
prestataire tiers.

Avant une mise en production plus large, la DSI mandate votre cabinet pour
réaliser une **évaluation de sécurité offensive (red team)** de l'application.

## 2. Objet de la mission

Identifier, démontrer et documenter les vulnérabilités de l'application agentique
« HelpDesk-AI » et de sa chaîne d'approvisionnement logicielle, puis proposer des
remédiations.

L'évaluation doit s'appuyer sur les référentiels **OWASP Top 10 for LLM
Applications (2025)** et **MITRE ATLAS**.

> Le périmètre exact, les autorisations et les interdits sont définis dans le
> document **Règles d'engagement** (`regles_engagement_FR.md`), qui fait partie
> intégrante de la présente mission. Toute action doit y être conforme.

## 3. Cible et environnement

- Une **bibliothèque Python** livrée sous forme de kit (voir `INSTALL_FR.md`).
  L'agent s'utilise depuis un notebook via son API (`agent.chat(...)` et les
  points d'entrée décrits dans `doc_client_FR.md`).
- Modèle exécuté **en local** via Ollama (`qwen2.5:3b`), sans aucune clé d'API
  cloud ni accès réseau sortant réel.
- Approche **boîte grise** : vous disposez de la documentation client
  (`doc_client_FR.md`) mais **pas** du code source de l'application.

## 4. Preuve d'exploitation : les jetons « canary »

Chaque vulnérabilité réellement exploitée révèle un **jeton de preuve** propre à
votre équipe, au format :

```
CPE{xxxxxxxxxxxx}
```

(12 caractères hexadécimaux). Ce jeton est caché dans la ressource que la
vulnérabilité est censée protéger (une réponse, un enregistrement, un journal,
un fichier…). **Une vulnérabilité n'est considérée comme confirmée que si vous
produisez le jeton correspondant.** Les jetons sont uniques par équipe : un jeton
d'une autre équipe ne vaudra pas preuve.

Votre kit contient **8 vulnérabilités actives** tirées d'un catalogue plus large.
Les autres chemins sont sécurisés : les tester donnera un **résultat négatif
documenté** (et non un jeton). Ces résultats négatifs sont attendus et valorisés
(voir la grille).

## 5. Livrables

Un **rapport de pentest unique** (PDF ou Markdown), rédigé en français à partir du
modèle fourni (`modele_rapport_FR.md`), comprenant :

1. **Résumé exécutif** actionnable, destiné à un décideur non technique.
2. **Tableau de synthèse des findings**, chacun rattaché à une catégorie OWASP
   LLM (2025) et à une (ou plusieurs) technique(s) MITRE ATLAS.
3. **Fiche détaillée par finding** : description, sévérité justifiée
   (impact × exploitabilité), **étapes de reproduction** exécutables, **jeton de
   preuve**, et remédiation distinguant **correctifs structurels** et
   **mesures d'atténuation**.
4. **Attribution modèle vs application** : pour chaque finding, indiquez si la
   cause racine tient au modèle ou à l'application qui l'entoure.
5. **Résultats négatifs** : les vulnérabilités testées et non trouvées.

Un seul rapport par équipe. Joignez, si utile, le notebook de reproduction.

## 6. Équipes, délai et évaluation

- Équipes de **3 à 4 personnes**.
- Mission en **travail à la maison**, sur **deux semaines** après L7.
- Ce projet constitue **la totalité de la note** (sur 20, pas d'examen). Les
  critères sont détaillés dans `grille_FR.md`.

## 7. Contacts et remise

Remise du rapport à la date indiquée en cours, par le canal indiqué en cours.
Pour toute question de périmètre, référez-vous d'abord aux Règles d'engagement.

---

*Bonne mission. Restez dans le périmètre, prouvez ce que vous avancez, et
n'affirmez rien que vous ne puissiez reproduire.*
