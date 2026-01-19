# 📁 Structure du Projet AI RPS Battle

```
ai-rps-battle/
│
├── 🐍 BACKEND (Python/Flask)
│   ├── rps_battle.py          ⭐ SCRIPT PRINCIPAL
│   │   └── Game loop, Flask server, API calls
│   │
│   ├── config.py              ⚙️ CONFIGURATION
│   │   └── API keys, modèles, timing, thoughts
│   │
│   └── run_local.py           🧪 TEST LOCAL
│       └── Script pour tester en local (debug mode)
│
├── 🎨 FRONTEND
│   └── templates/
│       └── viewer.html        💻 INTERFACE WEB
│           └── 3 colonnes: Terminal / Jeu / Stats
│
├── 📊 DATA (générés auto au runtime)
│   ├── logs.json              📝 LOGS TEMPS RÉEL
│   │   └── [HH:MM:SS] messages
│   │
│   └── game_state.json        🎮 ÉTAT DU JEU
│       └── Scores, choix, stats actuelles
│
├── ☁️ DEPLOYMENT
│   ├── Procfile               🚀 RAILWAY CONFIG
│   │   └── Comment lancer l'app (gunicorn)
│   │
│   ├── requirements.txt       📦 DÉPENDANCES
│   │   └── Flask, anthropic, openai, gunicorn
│   │
│   └── runtime.txt            🐍 PYTHON VERSION
│       └── python-3.11.7
│
├── 📚 DOCUMENTATION
│   ├── README.md              📖 DOC PRINCIPALE
│   │   └── Overview, installation, utilisation
│   │
│   ├── DEPLOYMENT.md          🚀 GUIDE RAILWAY
│   │   └── Step-by-step deployment
│   │
│   └── CHANGELOG.md           📝 HISTORIQUE
│       └── Versions et roadmap
│
└── 🔧 CONFIG
    └── .gitignore             🚫 EXCLUSIONS GIT
        └── Fichiers à ne pas commit

```

---

## 🔍 Détails des Fichiers Principaux

### 1️⃣ `rps_battle.py` (Script Principal - 230 lignes)

**Responsabilités:**
- Initialiser Flask server
- Créer clients API (Anthropic + OpenAI)
- Game loop (matches en continu)
- Fonctions de jeu (play_round, play_match)
- Routes API (/api/state, /api/logs, /api/stats)
- Logging système

**Flow:**
```
Démarrage → Init Flask → Start game_loop thread → Loop infini
    └──> Match → Round 1 → Round 2 → Round 3 (si besoin) → Winner
         └──> Pause 5s → Nouveau match
```

**API Endpoints:**
```
GET /              → Serve viewer.html
GET /api/state     → État du jeu (JSON)
GET /api/logs      → 50 derniers logs (JSON)
GET /api/stats     → Statistiques globales (JSON)
```

---

### 2️⃣ `config.py` (Configuration - 60 lignes)

**Variables importantes:**
```python
# API Keys (set via ENV vars)
ANTHROPIC_API_KEY
OPENAI_API_KEY

# Modèles
CLAUDE_MODEL = "claude-haiku-4-5-20251001"
GPT_MODEL = "gpt-4o-mini"

# Timing
ROUND_DELAY = 4    # Secondes entre rounds
MATCH_DELAY = 5    # Secondes entre matches
AUTO_PLAY = True   # Continuous play

# Game
BEST_OF = 3        # Best of 3 rounds
CHOICES = ['rock', 'paper', 'scissors']

# AI Thoughts (8 phrases chacun)
CLAUDE_THOUGHTS = [...]
GPT_THOUGHTS = [...]
```

---

### 3️⃣ `templates/viewer.html` (Interface - 600 lignes)

**Structure CSS Grid:**
```
┌──────────────┬────────────────────┬──────────────┐
│              │                    │              │
│   TERMINAL   │     GAME AREA      │   SIDEBAR    │
│   (Logs)     │   (Battle Zone)    │  (Thoughts)  │
│              │                    │              │
│   - Logs     │   - Title          │  - Claude    │
│   - Real     │   - Match Info     │    Thought   │
│     time     │   - Battle         │  - GPT       │
│   - Auto     │   - Choices        │    Thought   │
│     scroll   │   - Score          │  - Stats     │
│              │   - Result         │              │
│              │   - Overall        │              │
│              │     Stats          │              │
└──────────────┴────────────────────┴──────────────┘
```

**JavaScript:**
- Auto-refresh toutes les 2 secondes
- Fetch /api/state, /api/logs, /api/stats
- Update DOM avec nouvelles données
- Animations CSS pour les choix

---

### 4️⃣ `requirements.txt` (Dépendances)

```
Flask==3.0.0          → Web framework
flask-cors==4.0.0     → CORS support
anthropic==0.39.0     → Claude API
openai==1.54.0        → GPT API
gunicorn==21.2.0      → Production server
```

**Installation:**
```bash
pip install -r requirements.txt
```

---

### 5️⃣ `Procfile` (Railway Config)

```
web: gunicorn rps_battle:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120
```

**Explications:**
- `web:` → Type de process Railway
- `gunicorn` → Production WSGI server
- `rps_battle:app` → Module:application
- `--bind 0.0.0.0:$PORT` → Listen sur tous interfaces
- `--workers 1` → 1 worker (suffisant)
- `--threads 2` → 2 threads par worker
- `--timeout 120` → Timeout 2min (pour API calls)

---

## 🎯 Flow Complet de l'Application

```
┌─────────────────────────────────────────────────┐
│  1. Railway Start                               │
│     └─> Lit Procfile                           │
│         └─> Lance gunicorn                      │
│             └─> Charge rps_battle.py           │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  2. Init Phase                                  │
│     ├─> Load config.py                         │
│     ├─> Init Anthropic client                  │
│     ├─> Init OpenAI client                     │
│     ├─> Create logs.json (if not exists)       │
│     └─> Create game_state.json (if not exists) │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  3. Start Services                              │
│     ├─> Flask server (port $PORT)              │
│     └─> Game loop thread (background)          │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  4. Game Loop (Infinite)                        │
│     └─> Match                                   │
│         ├─> Round 1                            │
│         │   ├─> Claude chooses (API call)      │
│         │   ├─> GPT chooses (API call)         │
│         │   ├─> Compare & log result           │
│         │   └─> Update game_state.json         │
│         │                                        │
│         ├─> Round 2                            │
│         │   └─> (same as Round 1)              │
│         │                                        │
│         ├─> Round 3 (if needed)                │
│         │   └─> (same as Round 1)              │
│         │                                        │
│         ├─> Determine winner                   │
│         ├─> Update total stats                 │
│         ├─> Wait 5 seconds                     │
│         └─> Loop to new match                  │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│  5. User Access                                 │
│     └─> Visit https://yourapp.railway.app      │
│         ├─> GET / → Serve viewer.html          │
│         └─> JavaScript fetches:                 │
│             ├─> /api/state (every 2s)          │
│             ├─> /api/logs (every 2s)           │
│             └─> /api/stats (every 2s)          │
└─────────────────────────────────────────────────┘
```

---

## 🚀 Commandes Rapides

### Local Development
```bash
# Installer dépendances
pip install -r requirements.txt

# Lancer en mode test
python run_local.py

# Ou directement
python rps_battle.py
```

### Git Setup
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/ai-rps-battle.git
git push -u origin main
```

### Railway Deploy
```bash
# 1. Link repo to Railway (via web interface)
# 2. Set environment variables:
#    - ANTHROPIC_API_KEY
#    - OPENAI_API_KEY
# 3. Railway auto-deploys on push
```

---

## 📊 Taille des Fichiers

```
rps_battle.py      →  8.7 KB  (code principal)
viewer.html        → 17.7 KB  (interface)
config.py          →  1.4 KB  (config)
README.md          →  6.4 KB  (doc)
DEPLOYMENT.md      →  6.8 KB  (guide)
requirements.txt   →  81 B    (deps)
Procfile           →  88 B    (railway)
.gitignore         → ~500 B   (git)

TOTAL             → ~42 KB   (très léger!)
```

---

## ✅ Checklist Avant Deploy

- [ ] Tous les fichiers présents
- [ ] API keys configurées (pas dans le code!)
- [ ] .gitignore en place
- [ ] README.md à jour
- [ ] Git repo créé
- [ ] Pushed to GitHub
- [ ] Railway project créé
- [ ] Environment variables set
- [ ] Premier deploy réussi
- [ ] URL accessible
- [ ] Matchs démarrent auto
- [ ] Pas d'erreurs dans logs

---

**Projet ready to deploy! 🚀🎮**
