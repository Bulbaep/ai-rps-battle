# 🎮 AI Rock-Paper-Scissors Battle

**Claude Haiku 4.5 vs GPT-4o-mini** - Battles automatiques 24/7

## 🎯 Description

Un système de bataille automatique où deux IA s'affrontent au pierre-papier-ciseaux en continu. Les matchs tournent 24/7 avec une interface web en temps réel pour suivre l'action.

### Fonctionnalités

- ⚡ **Matchs automatiques** : Best of 3, nouveau match démarre automatiquement
- 🎨 **Interface professionnelle** : Dark theme, 3 colonnes (Terminal / Jeu / Stats)
- 📊 **Stats en temps réel** : Win rates, total matches, streaks
- 🧠 **AI Thoughts** : Phrases drôles/originales pour chaque IA
- 📡 **Live terminal** : Logs en temps réel, auto-scroll
- 💰 **Économique** : ~$0.0005 par match, peut tourner en continu

## 🏗️ Stack Technique

- **Backend** : Python 3.11+ (Flask)
- **Frontend** : HTML/CSS/JavaScript vanilla
- **APIs** : Anthropic (Claude Haiku 4.5) + OpenAI (GPT-4o-mini)
- **Hébergement** : Railway
- **Data** : JSON files (logs.json, game_state.json)

## 📁 Structure du Projet

```
ai-rps-battle/
├── rps_battle.py           # Script principal Flask
├── config.py               # Configuration (API keys, modèles)
├── templates/
│   └── viewer.html         # Interface web
├── requirements.txt        # Dépendances Python
├── Procfile               # Configuration Railway
├── logs.json              # Logs temps réel (généré auto)
├── game_state.json        # État du jeu (généré auto)
└── README.md              # Cette doc
```

## 🚀 Installation Locale

### 1. Cloner et Setup

```bash
# Créer un dossier
mkdir ai-rps-battle
cd ai-rps-battle

# Copier tous les fichiers du projet ici
```

### 2. Configuration des API Keys

Créer un fichier `.env` :

```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

Ou modifier directement `config.py` :

```python
ANTHROPIC_API_KEY = "sk-ant-..."
OPENAI_API_KEY = "sk-..."
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer le serveur

```bash
python rps_battle.py
```

Ouvrir http://localhost:5000 dans ton navigateur

## ☁️ Déploiement Railway

### 1. Préparer le projet

Assure-toi d'avoir tous les fichiers :
- `rps_battle.py`
- `config.py`
- `templates/viewer.html`
- `requirements.txt`
- `Procfile`

### 2. Créer un repo GitHub

```bash
git init
git add .
git commit -m "Initial commit - AI RPS Battle"
git remote add origin https://github.com/ton-username/ai-rps-battle.git
git push -u origin main
```

### 3. Déployer sur Railway

1. Aller sur https://railway.app
2. New Project → Deploy from GitHub repo
3. Sélectionner ton repo `ai-rps-battle`
4. Ajouter les variables d'environnement :
   - `ANTHROPIC_API_KEY` : ta clé Anthropic
   - `OPENAI_API_KEY` : ta clé OpenAI
5. Railway va automatiquement :
   - Détecter le `Procfile`
   - Installer les `requirements.txt`
   - Lancer l'app avec gunicorn

### 4. Domaine custom (optionnel)

Dans Railway :
- Settings → Domains
- Add Custom Domain
- Configurer ton DNS

## 🎮 Comment ça marche

### Flow du jeu

1. **Initialisation** : Backend démarre, crée les fichiers JSON
2. **Match démarre** : Best of 3
3. **Round** :
   - Claude fait un choix random (via API)
   - GPT fait un choix random (via API)
   - Comparaison des choix
   - Résultat loggé
4. **Match complet** : Premier à 2 victoires gagne
5. **Pause** : 5 secondes
6. **Nouveau match** : Redémarre automatiquement

### Règles

- **Rock** 👊 bat **Scissors** ✌️
- **Paper** ✋ bat **Rock** 👊
- **Scissors** ✌️ bat **Paper** ✋
- **Tie** = rejoue le round (ne compte pas)

## 💰 Coûts Estimés

### Par match (Best of 3)

- **Tokens** : ~50 tokens par choix × 6 choix max = ~300 tokens
- **Claude Haiku 4.5** : $0.001 / 1k input tokens
- **GPT-4o-mini** : $0.00015 / 1k input tokens
- **Coût par match** : ~$0.0005

### Par jour (en continu)

- **Matches** : ~10-15 par heure = ~300 matches/jour
- **Coût quotidien** : ~$0.15/jour
- **Coût mensuel** : ~$4.50/mois

**Conclusion** : Peut tourner 24/7 pour très peu cher ! 🚀

## 📊 Interface Web

### 3 Colonnes

**GAUCHE - Live Terminal**
- Logs en temps réel
- Format : `[HH:MM:SS] message`
- Auto-scroll
- Historique des 100 derniers logs

**CENTRE - Zone de jeu**
- Titre animé
- Info match/round
- Choix des AIs (👊 ✋ ✌️)
- Score actuel
- Résultat du round
- Stats globales

**DROITE - AI Thoughts & Stats**
- Pensées des AIs (phrases drôles)
- Stats rapides
- Last winner
- Win rates

## 🔧 Configuration

Dans `config.py` :

```python
# Modèles
CLAUDE_MODEL = "claude-haiku-4-5-20251001"
GPT_MODEL = "gpt-4o-mini"

# Timing
ROUND_DELAY = 4      # Secondes entre rounds
MATCH_DELAY = 5      # Secondes entre matches
AUTO_PLAY = True     # Play continu

# Best of X
BEST_OF = 3          # Best of 3 par défaut
```

## 🎨 Personnalisation

### Ajouter des AI Thoughts

Dans `config.py` :

```python
CLAUDE_THOUGHTS = [
    "Ta phrase custom ici",
    "Autre phrase drôle",
    # ...
]
```

### Changer les couleurs

Dans `viewer.html`, modifier les variables CSS ou les classes.

### Modifier le timing

Dans `config.py`, ajuster `ROUND_DELAY` et `MATCH_DELAY`.

## 📝 API Endpoints

- `GET /` : Page principale
- `GET /api/state` : État du jeu actuel
- `GET /api/logs` : 50 derniers logs
- `GET /api/stats` : Statistiques globales

## 🐛 Troubleshooting

### L'app ne démarre pas

- Vérifie que les API keys sont bien configurées
- Regarde les logs Railway
- Assure-toi que `templates/` existe avec `viewer.html`

### Les matchs ne démarrent pas

- Vérifie que `AUTO_PLAY = True` dans `config.py`
- Check les logs pour voir les erreurs API

### Les logs ne s'affichent pas

- Rafraîchis la page
- Vérifie que `logs.json` a bien été créé
- Check la console navigateur (F12)

## 🚀 Prochaines Features (Roadmap)

- [ ] Système de gambling crypto
- [ ] Historique des matchs en DB
- [ ] Graphiques des win rates
- [ ] Streaks et records
- [ ] Son/musique d'ambiance
- [ ] Mode "tournament" (plusieurs AIs)
- [ ] Webhooks pour notifications

## 📄 License

MIT License - Fait ce que tu veux avec !

## 🤝 Contribution

PR bienvenues ! C'est un projet fun et facilement extensible.

## 📞 Support

Si tu as des questions ou besoin d'aide pour le deploy, ping-moi !

---

**Bon game ! 🎮👊✋✌️**
