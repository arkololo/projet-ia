# Installation : « HelpDesk-AI » (Windows d'abord)

Ce kit s'exécute **entièrement en local**, hors ligne. Aucune clé d'API cloud.
Comptez ~5 Go d'espace disque (modèles Ollama compris) et un CPU récent ; aucun
GPU n'est nécessaire.

La procédure **Windows (PowerShell)** est la référence. Les sections **macOS** et
**Linux** suivent.

---

## 0. Contenu du kit

Après décompression du `.zip` de votre équipe :

```
helpdesk_kit_team_XX/
  helpdesk_agent/         # l'application cible (bytecode uniquement, + team.cfg)
  student/                # lettre de mission, RoE, doc client, modèle de rapport, ce fichier, notebook
  pyproject.toml
```

> Le paquet est livré en **bytecode** (`.pyc`) et sa configuration est chiffrée.
> C'est voulu : la mission est en **boîte grise** (voir les Règles d'engagement).

---

## 1. Windows (PowerShell) : référence

### 1.1 Installer `uv`

`uv` gère Python et les dépendances. Dans PowerShell :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Fermez puis rouvrez PowerShell, et vérifiez :

```powershell
uv --version
```

### 1.2 Installer Ollama

Téléchargez et installez **Ollama pour Windows** depuis <https://ollama.com/download>.
Après installation, Ollama tourne en tâche de fond. Vérifiez :

```powershell
ollama --version
```

Si le service n'est pas démarré, lancez-le (une fenêtre suffit, laissez-la
ouverte) :

```powershell
ollama serve
```

### 1.3 Télécharger les modèles

Dans un **autre** onglet PowerShell (en laissant `ollama serve` tourner si vous
l'avez lancé à la main) :

```powershell
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

### 1.4 Installer les dépendances du kit

Placez-vous dans le dossier du kit décompressé :

```powershell
cd C:\chemin\vers\helpdesk_kit_team_XX
uv sync
```

`uv` installera automatiquement **Python 3.12** (version épinglée du kit) et les
dépendances.

### 1.5 Test de fumée

```powershell
uv run python -c "from helpdesk_agent import HelpdeskAgent; a = HelpdeskAgent.for_team(); print(a.chat('Bonjour'))"
```

Une réponse en langage naturel de l'agent confirme que tout fonctionne.

### 1.6 Lancer le notebook

```powershell
uv run jupyter lab student\engagement.ipynb
```

---

## 2. macOS

```bash
# uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# Ollama : télécharger l'app depuis https://ollama.com/download, puis :
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
# Dépendances + test de fumée (depuis le dossier du kit)
uv sync
uv run python -c "from helpdesk_agent import HelpdeskAgent; a = HelpdeskAgent.for_team(); print(a.chat('Bonjour'))"
uv run jupyter lab student/engagement.ipynb
```

## 3. Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
uv sync
uv run python -c "from helpdesk_agent import HelpdeskAgent; a = HelpdeskAgent.for_team(); print(a.chat('Bonjour'))"
uv run jupyter lab student/engagement.ipynb
```

---

## 4. Dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| `ConnectionError` / *connection refused* au premier `chat` | Ollama n'est pas démarré. | Lancez `ollama serve` (Windows/Linux) ou ouvrez l'app (macOS). |
| `model 'qwen2.5:3b' not found` | Modèle non téléchargé. | `ollama pull qwen2.5:3b`. |
| Erreur d'embeddings / RAG vide | `nomic-embed-text` manquant. | `ollama pull nomic-embed-text`. |
| Première réponse très lente | Chargement du modèle en mémoire. | Normal au premier appel ; les suivants sont plus rapides. |
| `uv: command not found` | Terminal non rechargé. | Fermez/rouvrez le terminal après l'installation de `uv`. |
| Réponses lentes sur portable | Inférence CPU. | Fermez les applications lourdes ; réduisez la longueur des invites. |

## 5. Outillage de pentest (optionnel, à votre charge)

Le kit ne fournit **que** la cible et son API. Ajoutez vos propres outils dans
votre environnement, par exemple :

```powershell
uv pip install garak promptfoo picklescan modelscan
```

Ces outils s'utilisent dans le respect des Règles d'engagement (analyse des
artefacts livrés et de l'API de l'agent ; **pas** de rétro-ingénierie du paquet).
