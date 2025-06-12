# 🎓 Gestion Formation ORM

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/AniceGit/gestion-formation-orm)](https://github.com/AniceGit/gestion-formation-orm/commits/main)
[![Issues](https://img.shields.io/github/issues/AniceGit/gestion-formation-orm)](https://github.com/AniceGit/gestion-formation-orm/issues)

**Gestion Formation ORM** est une application Python basée sur **SQLModel** et **Streamlit** pour gérer des formations, des formateurs, des apprenants et des sessions. Elle utilise une base SQLite, permet de créer et manipuler des objets via une interface Streamlit, et propose des migrations via Alembic.

---

## 📦 Installation

1. Cloner le projet :
```bash
git clone https://github.com/AniceGit/gestion-formation-orm.git
cd gestion-formation-orm
```
2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
```
3. Installer les dépendances :
```bash
pip install -r requirements.txt
```
4. Initialiser la base de données (via Alembic) :
```bash
alembic upgrade head
```
5. Lancer l'application :
```bash
streamlit run app/main.py
```

## ⚙️ Dépendances principales
- sqlmodel==0.0.24
- SQLAlchemy==2.0.41
- Streamlit
- Alembic==1.16.1
- Faker==37.3.0
- email_validator, phonenumbers, pydantic, etc.
Toutes les dépendances sont listées dans requirements.txt.

## 🧱 Stack technique
- Langage : Python 3.10+
- Base de données : SQLite
- ORM : SQLModel (SQLAlchemy + Pydantic)
- Frontend : Streamlit (web UI simple et rapide)
- Migrations : Alembic
- Génération de données : Faker

## 📊 Guide d’utilisation
L’application expose une interface web accessible à l’adresse http://localhost:8501. Voici les fonctionnalités principales :
- Utilisateur
  - add_utilisateur()
  - update_utilisateur()
  - delete_utilisateur()
  - get_utilisateurs()
- Salle
  - add_salle()
  - update_salle()
  - delete_salle()
  - get_salles()
- Inscription
  - add_inscription()
  - update_inscription()
  - delete_inscription()
  - get_inscriptions()
- Session
  - add_session()
  - update_session()
  - delete_session()
  - get_sessions()
