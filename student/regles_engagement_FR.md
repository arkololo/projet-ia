# Règles d'engagement (RoE) : « HelpDesk-AI »

**Référence :** CPE-2026-REDTEAM-HELPDESK
**Statut :** contractuel ; fait partie de la lettre de mission.

Ces règles définissent ce qui est **autorisé** et **interdit** pendant la
mission. Toute violation est sanctionnée (voir `grille_FR.md`, pénalités). En cas
de doute, l'action est **hors périmètre** tant que l'enseignant ne l'a pas
confirmée.

---

## 1. Périmètre autorisé (in-scope)

Vous êtes autorisés à :

- Interagir avec l'agent **uniquement via son API publique** documentée dans
  `doc_client_FR.md` : `chat`, `submit_ticket`, `process_ticket_queue`,
  `suggest_kb`, `render`, et la lecture des points d'observation
  (`outbox`, `usage_alerts`, `attacker.log`, `renderer.findings`).
- Concevoir des **entrées adverses** (invites, tickets, suggestions de base de
  connaissances, contenus à rendre) pour tester le comportement de l'agent.
- Observer et enregistrer tous les effets de bord exposés par le kit.
- Utiliser des **outils d'analyse de sécurité** sur les artefacts que le kit vous
  livre légitimement (par exemple `picklescan` / `ModelScan` sur un modèle
  vendu avec l'application, `garak` / `promptfoo` contre l'API de l'agent).

## 2. Hors périmètre : strictement interdit (out-of-scope)

Vous **ne devez pas** :

1. **Rétro-ingénierie de l'application.** Le kit est livré en **bytecode**
   (`.pyc`), sans sources. Il est interdit de décompiler, désassembler,
   reconstruire ou lire les internes du paquet `helpdesk_agent` (y compris via
   `inspect.getsource`, `dis`, `uncompyle`/`decompyle`, `marshal`, ou l'ouverture
   des `.pyc`).
2. **Déchiffrer ou lire la configuration d'équipe** (`team.cfg`). La clé est un
   simple *dissuasif*, pas une frontière de sécurité : l'exploiter pour lire la
   configuration, la liste des vulnérabilités actives ou les jetons **est une
   violation**. Les jetons doivent être obtenus **par exploitation applicative**,
   jamais en lisant la configuration.
3. **Attaquer l'infrastructure du modèle.** Ollama, le runtime, le système
   d'exploitation, le réseau et le matériel sont hors périmètre. Pas de
   fine-tuning, pas de modification des poids, pas d'attaque sur le serveur
   Ollama lui-même. La cible est **l'application**, pas le moteur d'inférence.
4. **Sortir du bac à sable.** Aucune attaque contre des systèmes réels, aucun
   trafic réseau réel : le « serveur attaquant » est simulé **en local**
   (`attacker.example` n'existe pas ; ses réceptions sont journalisées en
   mémoire). N'essayez pas d'ouvrir de vraies connexions sortantes.
5. **Falsifier des preuves.** N'inventez pas de jetons, ne recopiez pas ceux
   d'une autre équipe, ne dérivez pas un jeton par calcul plutôt que par
   exploitation.

## 3. Règle de preuve (canary)

- Un finding n'est **confirmé** que si vous produisez le **jeton `CPE{…}`**
  correspondant, obtenu **par le chemin d'attaque applicatif** que vous décrivez.
- Vos étapes de reproduction doivent permettre à l'enseignant d'obtenir le
  **même** jeton en les rejouant.
- Un jeton présenté sans chemin de reproduction reproductible, ou obtenu par un
  moyen hors périmètre, **ne compte pas** et peut entraîner une pénalité s'il est
  présenté comme un finding confirmé.

## 4. Honnêteté et qualité

- Ne présentez comme **confirmé** que ce que vous pouvez reproduire. Une
  hypothèse non prouvée se documente comme telle (piste, non confirmée).
- Les **résultats négatifs** (vulnérabilités testées et absentes) sont attendus
  et notés. Documentez-les honnêtement.
- Le modèle étant petit et non déterministe à la marge, un exploit peut échouer
  occasionnellement. Indiquez le **taux de réussite** observé si pertinent, et
  rejouez pour confirmer.

## 5. Confidentialité

Le kit, ses jetons et son contenu sont propres à votre équipe et destinés au
seul cadre pédagogique. Ne partagez pas votre kit, vos jetons ni votre rapport
avec d'autres équipes.

---

*En menant la mission, votre équipe accepte ces règles d'engagement.*
