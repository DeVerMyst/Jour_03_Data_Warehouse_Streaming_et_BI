# Jour 3 : Modélisation Data Warehouse (Star Schema, SCD2), Ingestion Streaming & Restitution BI (Metabase)
## Master 1 IA & Data · YNOV Campus (7 heures)

---

### Objectifs de la journée :
* **Matinée (08h45 - 12h45 · 4h) :**
  1. Ingestion asynchrone haute cadence (`asyncio`, `aiohttp`) et streaming sans saturation RAM (`datasets streaming=True`).
  2. Modélisation dimensionnelle de Ralph Kimball : Schéma en Étoile (Star Schema), table de temps `dim_date`.
  3. Gestion de l'historique avec les Slowly Changing Dimensions Type 2 (SCD2) et `dbt snapshot`.
* **Après-midi (13h45 - 16h45 · 3h) :**
  * **Grand Projet de Synthèse E-Commerce & Restitution BI :**
    - Ingestion des flux de commandes et produits.
    - Pipeline dbt complet (`stg_`, `dim_`, `fct_orders`) avec clés de substitution (Surrogate Keys).
    - Validation par tests d'intégrité référentielle (`relationships`).
    - Déploiement et création du Dashboard exécutif sur **Metabase (port 3000)**.

---

### Démarrage en 2 minutes :

#### 1. Lancer PostgreSQL, pgweb et Metabase avec Docker :
```bash
docker compose up -d
```
* PostgreSQL 16 : port `5432`
* pgweb : `http://localhost:8081`
* Metabase BI : `http://localhost:3000`

#### 2. Installer les dépendances avec `uv` :
```bash
uv sync
```

#### 3. Ouvrir les Notebooks :
* **Matin (Streaming, Star Schema & SCD2) :** `03_Data_Warehouse_Streaming_et_SCD2_exercices.ipynb`
* **Après-Midi (Projet de Synthèse & Metabase) :** `03_TP_ApresMidi_Projet_Synthese_Metabase_Exercices.ipynb`

---

### Arrêter l'environnement :
```bash
docker compose down
```
