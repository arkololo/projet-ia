# Rapport d'audit de sécurité : « HelpDesk-AI »

> **Modèle de rapport.** Remplacez chaque champ entre chevrons `< >` et
> supprimez les notes d'aide en italique. Rédigez en français. Un seul rapport
> par équipe. Rendu attendu : PDF ou Markdown (joindre le notebook de
> reproduction si utile).

**Client :** Helvetia Systems SA
**Prestataire (équipe) :** `<noms des 3-4 membres>`
**Référence de mission :** CPE-2026-REDTEAM-HELPDESK
**Identifiant d'équipe / kit :** `<team_XX>`
**Date :** `<date>`
**Référentiels :** OWASP Top 10 for LLM Applications (2025), MITRE ATLAS

---

## 1. Résumé exécutif

*Une page maximum, pour un décideur non technique. Que fait l'application, quel
est le risque global, combien de findings et de quelle gravité, quelles sont les
2-3 actions prioritaires. Pas de jargon inutile.*

`<résumé>`

## 2. Périmètre et méthode

- **Cible :** `<rappel de la cible et de l'interface utilisée>`
- **Approche :** boîte grise, via l'API documentée ; conforme aux Règles
  d'engagement.
- **Environnement :** `<modèle, OS, versions>`
- **Méthode :** `<comment vous avez procédé : reconnaissance de la surface,
  familles d'attaques testées, outillage>`

## 3. Synthèse des findings

| # | Titre | Catégorie OWASP LLM (2025) | MITRE ATLAS | Sévérité | Confirmé (jeton) | Cause : modèle / appli |
|---|---|---|---|---|---|---|
| F-01 | `<titre>` | `<LLMxx>` | `<AML.Txxxx>` | `<Critique/Élevée/Moyenne/Faible>` | `<CPE{…}>` | `<modèle / application>` |
| F-02 | | | | | | |
| … | | | | | | |

*Classez par sévérité décroissante. N'y faites figurer que des findings
**confirmés** (jeton produit).*

## 4. Fiches détaillées

*Une fiche par finding. Dupliquez le bloc ci-dessous.*

### F-0X : `<titre du finding>`

- **Catégorie OWASP LLM 2025 :** `<LLMxx - nom>`
- **Technique(s) MITRE ATLAS :** `<AML.Txxxx - nom>`
- **Sévérité :** `<niveau>`, *justification par impact × exploitabilité :*
  `<pourquoi ce niveau>`
- **Cause racine (modèle ou application) :** `<attribution + justification>`

**Description.** `<en quoi consiste la vulnérabilité, quelle ressource est
exposée, quel est l'impact métier>`

**Étapes de reproduction.** *Numérotées, exécutables telles quelles (invites
exactes, appels d'API, code du notebook). L'enseignant doit obtenir le même
jeton en les rejouant.*

```python
<code / invites de reproduction>
```

**Preuve (jeton).** `CPE{…}`, *où le jeton est apparu (réponse, journal, fichier,
outbox…) :* `<emplacement observé>`

**Remédiation.**
- **Correctif structurel :** `<la correction de fond qui supprime la cause>`
- **Mesures d'atténuation :** `<mesures complémentaires / défense en profondeur>`

---

## 5. Résultats négatifs

*Vulnérabilités que vous avez testées et **non** trouvées (chemins sécurisés).
Décrivez brièvement le test mené et le résultat obtenu (résultat négatif
documenté). Ceci est attendu et noté.*

| Famille testée | Test mené | Résultat |
|---|---|---|
| `<ex. réinitialisation de mot de passe non autorisée>` | `<invite / démarche>` | `<négatif : accès refusé, pas de jeton>` |

## 6. Conclusion et recommandations prioritaires

`<vue d'ensemble, priorisation des remédiations, éventuelles limites de
l'évaluation>`

---

*Rappel : ne présentez comme confirmé que ce que vous pouvez reproduire. Toute
affirmation non prouvée présentée comme un finding confirmé, et toute violation
des Règles d'engagement, sont pénalisées.*
