# HelpDesk-AI — Red Team

**JNR 16K · `team_02` · Projet universitaire de cybersécurité**

Audit en boîte grise d'un agent d'assistance informatique fondé sur un LLM. Ce dépôt rassemble le kit pédagogique, les scripts d'expérimentation, les preuves et le rapport de l'équipe **team_02**.

L'application représente le support interne de l'entreprise fictive **Helvetia Systems SA**. Elle fonctionne localement avec Python et Ollama, sur des données fictives et avec des vulnérabilités intentionnelles.

**[Lire le rapport](audit/rapport_audit_helpdesk_team_02.md)** · **[Rapport PDF](audit/rapport_audit_helpdesk_team_02.pdf)** · **[Règles d'engagement](student/regles_engagement_FR.md)** · **[Documentation de l'API](student/doc_client_FR.md)**

## Objectifs

- Étudier les injections de prompt directes et indirectes.
- Vérifier les contrôles d'accès aux outils, aux tickets et aux données sensibles.
- Évaluer la sécurité de la base de connaissances RAG et du rendu des réponses.
- Examiner les risques liés aux composants tiers dans le périmètre autorisé.
- Produire des preuves reproductibles et proposer des remédiations.

Le rapport s'appuie sur les référentiels **OWASP Top 10 for LLM Applications (2025)** et **MITRE ATLAS**. Les jetons `CPE{…}` servent de preuves pédagogiques ; chaque finding doit être associé à un chemin de reproduction.

## Équipe

| Membre | Rôle dans l'équipe |
|---|---|
| Léo LECLERCQ | Membre |
| Edgar BOBILLON | Membre et contact |
| Tomy RULLIAT | Membre |
| Erwan AOUCHICHE | Membre |

**Nom :** JNR 16K — **Identifiant :** `team_02`

## Organisation du dépôt

```text
.
├── helpdesk_agent/     # Application fournie en bytecode et configuration d'équipe
├── student/            # Consignes, documentation et notebook de prise en main
├── audit/
│   ├── evidence/       # Preuves et résultats enregistrés
│   ├── recon*.py       # Scripts d'exploration du laboratoire
│   ├── reproduce.py   # Script de reproduction des findings du rapport
│   ├── build_pdf.py   # Génération du rapport PDF
│   └── rapport_audit_helpdesk_team_02.*
├── pyproject.toml      # Dépendances et contrainte Python 3.12
├── uv.lock             # Versions verrouillées des dépendances
└── README.md
```

## Démarrage rapide

Prérequis : **uv**, **Ollama**, environ **5 Go d'espace disque** et le kit de `team_02`. Le projet nécessite **Python 3.12**. Aucun GPU ni clé d'API cloud n'est requis.

Les étapes d'installation propres à Windows, Linux et macOS sont détaillées dans le [guide d'installation](student/INSTALL_FR.md).

Depuis la racine du dépôt, préparer les modèles et l'environnement :

```sh
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
uv sync
```

Ces étapes initiales peuvent nécessiter des téléchargements. Une fois les dépendances et les modèles disponibles, le laboratoire s'exécute localement.

Si Ollama n'est pas déjà démarré, lancer `ollama serve` dans un autre terminal. Vérifier ensuite le fonctionnement de l'agent :

```sh
uv run python -c "from helpdesk_agent import HelpdeskAgent; a = HelpdeskAgent.for_team(); print(a.chat('Bonjour'))"
```

Ouvrir le notebook de prise en main :

```sh
uv run jupyter lab student/engagement.ipynb
```

## Travaux d'audit

Le [rapport Markdown](audit/rapport_audit_helpdesk_team_02.md) présente les findings, leur sévérité, les preuves, les résultats négatifs et les recommandations. Il est également disponible en [PDF](audit/rapport_audit_helpdesk_team_02.pdf).

Le [script de reproduction](audit/reproduce.py) et les [preuves enregistrées](audit/evidence/) accompagnent les résultats. Consulter les étapes détaillées du rapport avant de rejouer les scénarios sur le kit local.

L'interface documentée expose `chat`, `submit_ticket`, `process_ticket_queue`, `suggest_kb` et `render`. Les effets de bord sont observables via `outbox`, `usage_alerts`, `attacker.log` et `renderer.findings`. Les courriels et le serveur `attacker.example` sont simulés par le laboratoire.

## Documents de référence

| Document | Contenu |
|---|---|
| [Lettre de mission](student/lettre_de_mission_FR.md) | Contexte, objectifs et livrables attendus |
| [Règles d'engagement](student/regles_engagement_FR.md) | Périmètre autorisé, interdictions et exigences de preuve |
| [Installation](student/INSTALL_FR.md) | Préparation de l'environnement et dépannage |
| [Documentation client](student/doc_client_FR.md) | Architecture, API publique et observateurs |
| [Notebook de prise en main](student/engagement.ipynb) | Exemples d'utilisation de l'agent |
| [Modèle de rapport](student/modele_rapport_FR.md) | Structure du livrable demandé |


