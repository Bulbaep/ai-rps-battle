# ⚡ Démarrage Rapide (5 Minutes)

Guide ultra-rapide pour lancer AI RPS Battle en local ou sur Railway.

---

## 🏃 Option 1 : Test Local (2 minutes)

### Étape 1 : Setup
```bash
# Extraire le ZIP
unzip ai-rps-battle.zip
cd ai-rps-battle

# Installer les dépendances
pip install -r requirements.txt
```

### Étape 2 : Config API Keys

Ouvrir `config.py` et mettre tes clés :

```python
ANTHROPIC_API_KEY = "sk-ant-api03-xxxxx"  # Ta clé Anthropic
OPENAI_API_KEY = "sk-xxxxx"               # Ta clé OpenAI
```

### Étape 3 : Lancer !

```bash
python rps_battle.py
```

Ouvrir http://localhost:5000 → **C'est parti ! 🎮**

---

## ☁️ Option 2 : Deploy Railway (5 minutes)

### Étape 1 : GitHub

```bash
# Dans le dossier du projet
git init
git add .
git commit -m "Initial commit"

# Créer repo sur GitHub puis :
git remote add origin https://github.com/TON-USERNAME/ai-rps-battle.git
git push -u origin main
```

### Étape 2 : Railway

1. Aller sur https://railway.app
2. **New Project** → **Deploy from GitHub repo**
3. Sélectionner `ai-rps-battle`
4. Railway commence le build automatiquement

### Étape 3 : Variables d'environnement

Dans Railway, onglet **Variables** :

```
ANTHROPIC_API_KEY = sk-ant-api03-xxxxx
OPENAI_API_KEY = sk-xxxxx
```

### Étape 4 : Accéder

1. Onglet **Settings** → **Domains**
2. Copier l'URL : `https://ai-rps-battle-production.up.railway.app`
3. Ouvrir dans le navigateur → **Live ! 🚀**

---

## 🔑 Où Trouver les API Keys ?

### Anthropic (Claude)
1. https://console.anthropic.com
2. **API Keys** → **Create Key**
3. Copier la clé `sk-ant-api03-xxxxx...`

### OpenAI (GPT)
1. https://platform.openai.com/api-keys
2. **Create new secret key**
3. Copier la clé `sk-xxxxx...`

**⚠️ Important** : Ne JAMAIS commit les clés dans Git !

---

## 📱 Vérifier que ça Marche

### ✅ Checklist

Si l'app fonctionne, tu dois voir :

**Dans les logs (terminal ou Railway)** :
```
🚀 AI RPS BATTLE - System Initialized
🤖 Claude Haiku 4.5 vs GPT-4o-mini
📡 Continuous play mode: ACTIVE
🏁 MATCH #1 - STARTING
🎮 ROUND 1 - START
💙 Claude chose: 👊 ROCK
🧡 GPT chose: ✋ PAPER
🎉 GPT WINS Round 1!
...
```

**Dans l'interface web** :
- [ ] Terminal affiche des logs
- [ ] Zone de jeu montre les choix (👊 ✋ ✌️)
- [ ] Scores se mettent à jour
- [ ] Stats globales augmentent
- [ ] AI Thoughts changent

---

## 🐛 Problèmes Courants

### ❌ `ModuleNotFoundError: No module named 'flask'`
```bash
pip install -r requirements.txt
```

### ❌ `AuthenticationError: Invalid API key`
- Vérifie que tes clés sont correctes
- Anthropic : commence par `sk-ant-`
- OpenAI : commence par `sk-`

### ❌ `Address already in use (port 5000)`
```bash
# Changer le port dans config.py
PORT = 5001  # Au lieu de 5000
```

### ❌ Railway : App crash au démarrage
1. Vérifier les logs dans Railway
2. S'assurer que les **Variables** sont bien set
3. Vérifier que tous les fichiers sont dans le repo

### ❌ Interface se charge mais pas de matchs
1. Vérifier dans `config.py` : `AUTO_PLAY = True`
2. Check les logs pour erreurs API
3. Vérifier les API keys

---

## 🎯 Commandes Essentielles

### Test Local
```bash
python rps_battle.py                    # Lancer l'app
python run_local.py                     # Mode debug
```

### Git
```bash
git status                              # Voir les changements
git add .                               # Ajouter tous les fichiers
git commit -m "Message"                 # Commit
git push                                # Push vers GitHub
```

### Railway
```
Auto-deploy activé → Push = Deploy automatique
```

---

## 📊 Monitoring

### Local
```
Logs dans le terminal en temps réel
```

### Railway
1. Onglet **Deployments**
2. Cliquer sur le deployment actif
3. Voir les logs live

---

## 💰 Coûts

### APIs (à payer toi-même)
- **Par match** : ~$0.0005
- **Par jour (24/7)** : ~$0.15
- **Par mois** : ~$4.50

### Railway
- **Plan Hobby** : 500h/mois gratuit (~20 jours)
- **Plan Developer** : $5/mois (illimité)

**Total pour 24/7** : ~$9.50/mois

---

## 🎮 Prochaines Étapes

Une fois que ça tourne :

1. **Partager** : Envoie l'URL à tes amis
2. **Monitor** : Regarde les stats augmenter
3. **Customiser** : Change les AI thoughts dans `config.py`
4. **Améliorer** : Check le CHANGELOG.md pour la roadmap

---

## 📞 Besoin d'Aide ?

**Docs complètes** :
- `README.md` - Vue d'ensemble
- `DEPLOYMENT.md` - Guide Railway détaillé
- `PROJECT_STRUCTURE.md` - Architecture

**Support Railway** :
- Discord : https://discord.gg/railway
- Docs : https://docs.railway.app

---

## ⏱️ Timeline Réaliste

| Tâche | Temps |
|-------|-------|
| Extraire ZIP + installer deps | 1 min |
| Config API keys | 30 sec |
| Test local | 30 sec |
| Créer repo GitHub | 1 min |
| Deploy Railway | 2 min |
| Config variables | 30 sec |
| Vérifier que ça marche | 30 sec |

**TOTAL** : ~6 minutes max ! ⚡

---

**Let's go ! 🚀👊✋✌️**
