# 🚀 Guide de Déploiement Railway

Guide complet pour déployer AI RPS Battle sur Railway avec domaine custom.

## 📋 Prérequis

- [ ] Compte Railway (https://railway.app)
- [ ] Compte GitHub
- [ ] API Key Anthropic (https://console.anthropic.com)
- [ ] API Key OpenAI (https://platform.openai.com)
- [ ] Domaine custom (optionnel)

## 🔧 Étape 1 : Préparer le Projet

### 1.1 Créer un repo GitHub

```bash
# Initialiser git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit - AI RPS Battle"

# Créer le repo sur GitHub (via l'interface web)
# Puis lier le repo local

git remote add origin https://github.com/TON-USERNAME/ai-rps-battle.git
git branch -M main
git push -u origin main
```

### 1.2 Vérifier les fichiers essentiels

Assure-toi d'avoir ces fichiers dans ton repo :

```
✅ rps_battle.py
✅ config.py
✅ templates/viewer.html
✅ requirements.txt
✅ Procfile
✅ runtime.txt
✅ README.md
✅ .gitignore
```

## ☁️ Étape 2 : Déploiement sur Railway

### 2.1 Créer un nouveau projet

1. Aller sur https://railway.app
2. Cliquer sur **"New Project"**
3. Sélectionner **"Deploy from GitHub repo"**
4. Autoriser Railway à accéder à ton GitHub si ce n'est pas déjà fait
5. Sélectionner le repo **ai-rps-battle**

### 2.2 Configuration automatique

Railway va automatiquement :
- ✅ Détecter que c'est un projet Python
- ✅ Lire le `Procfile` pour savoir comment lancer l'app
- ✅ Installer les dépendances depuis `requirements.txt`
- ✅ Utiliser Python 3.11.7 (spécifié dans `runtime.txt`)

### 2.3 Ajouter les variables d'environnement

Dans Railway, aller dans ton project :

1. Cliquer sur l'onglet **"Variables"**
2. Ajouter ces variables :

```
ANTHROPIC_API_KEY = sk-ant-api03-xxxxx...
OPENAI_API_KEY = sk-xxxxx...
PORT = 5000 (Railway le définit auto, mais tu peux le forcer)
```

**Important** : Ne JAMAIS commit tes API keys dans le code !

### 2.4 Déployer

1. Railway va automatiquement déployer après avoir ajouté les variables
2. Ou cliquer sur **"Deploy"** manuellement
3. Attendre 1-2 minutes que le build soit terminé

### 2.5 Vérifier le déploiement

1. Aller dans l'onglet **"Deployments"**
2. Cliquer sur le dernier deployment
3. Voir les logs pour vérifier qu'il n'y a pas d'erreurs
4. Chercher le message : `🚀 AI RPS BATTLE - System Initialized`

## 🌐 Étape 3 : Accéder à l'App

### 3.1 URL Railway (temporaire)

Railway te donne une URL automatique :

1. Dans ton projet, aller dans **"Settings"**
2. Section **"Domains"**
3. Tu verras une URL type : `https://ai-rps-battle-production.up.railway.app`
4. Cliquer dessus pour ouvrir ton app ! 🎮

### 3.2 Domaine Custom (optionnel)

Si tu as ton propre domaine :

#### A. Configuration Railway

1. Dans **"Settings"** → **"Domains"**
2. Cliquer sur **"Custom Domain"**
3. Entrer ton domaine : `rps.tondomaine.com`
4. Railway te donnera des instructions DNS

#### B. Configuration DNS

Chez ton registrar (Namecheap, Cloudflare, etc.) :

**Option 1 - CNAME (recommandé)**
```
Type: CNAME
Name: rps (ou @)
Value: [fourni par Railway]
TTL: Auto
```

**Option 2 - A Record**
```
Type: A
Name: rps (ou @)
Value: [IP fournie par Railway]
TTL: Auto
```

#### C. Vérification

1. Attendre 5-30 minutes pour la propagation DNS
2. Visiter `https://rps.tondomaine.com`
3. Railway génère automatiquement un certificat SSL ! 🔒

## 📊 Étape 4 : Monitoring

### 4.1 Voir les logs en temps réel

Dans Railway :
1. Aller dans **"Deployments"**
2. Cliquer sur le deployment actif
3. Voir les logs live :
   - Matchs en cours
   - Erreurs éventuelles
   - Stats d'utilisation

### 4.2 Métriques

Railway montre automatiquement :
- CPU usage
- Memory usage
- Network traffic

## 🔄 Étape 5 : Mises à Jour

### 5.1 Déploiement automatique

Railway redéploie automatiquement à chaque push sur `main` :

```bash
# Faire des modifications
nano rps_battle.py

# Commit et push
git add .
git commit -m "Amélioration du système de logs"
git push origin main

# Railway redéploie automatiquement ! 🚀
```

### 5.2 Rollback

Si un deployment échoue :

1. Aller dans **"Deployments"**
2. Trouver le dernier deployment qui fonctionnait
3. Cliquer sur **"Redeploy"**

## 💰 Coûts Railway

### Plan Gratuit (Hobby)

- **500h d'exécution/mois** (gratuit)
- Suffisant pour tester et développer
- L'app peut tourner ~20 jours/mois gratuitement

### Plan Developer ($5/mois)

- **Exécution illimitée**
- Recommandé pour production 24/7
- + Domaines customs illimités

### Coûts API

En plus de Railway, tu paies les APIs :

- **Claude Haiku 4.5** : ~$0.0003/match
- **GPT-4o-mini** : ~$0.0002/match
- **Total** : ~$0.0005/match

**24/7 continu** :
- ~300 matches/jour = ~$0.15/jour
- ~$4.50/mois

**Total projet (Railway + APIs)** : ~$9.50/mois pour 24/7

## 🐛 Troubleshooting

### L'app crash au démarrage

**Problème** : Logs montrent `ModuleNotFoundError`

**Solution** :
```bash
# Vérifier requirements.txt
cat requirements.txt

# Re-push si besoin
git add requirements.txt
git commit -m "Fix dependencies"
git push
```

### API Keys invalides

**Problème** : `AuthenticationError`

**Solution** :
1. Vérifier les keys dans Railway Variables
2. Elles doivent commencer par `sk-ant-` (Anthropic) et `sk-` (OpenAI)
3. Pas d'espaces avant/après

### L'app démarre mais pas de matchs

**Problème** : Interface s'affiche mais rien ne se passe

**Solution** :
1. Voir les logs Railway
2. Vérifier que `AUTO_PLAY = True` dans config.py
3. Check les erreurs API dans les logs

### Domaine custom ne fonctionne pas

**Problème** : `DNS_PROBE_FINISHED_NXDOMAIN`

**Solution** :
1. Attendre 30min-2h (propagation DNS)
2. Vérifier les records DNS chez ton registrar
3. Utiliser https://dnschecker.org pour tester

### Memory overflow

**Problème** : App crash avec `Out of Memory`

**Solution** :
```python
# Dans rps_battle.py, limiter les logs en mémoire
if len(logs) > 100:  # Au lieu de 1000
    logs.pop(0)
```

## 📞 Support Railway

Si problème personne :

1. Discord Railway : https://discord.gg/railway
2. Docs : https://docs.railway.app
3. Status : https://status.railway.app

## ✅ Checklist Finale

Avant de considérer le déploiement terminé :

- [ ] L'app est accessible via l'URL Railway
- [ ] Les matchs démarrent automatiquement
- [ ] Les logs s'affichent en temps réel
- [ ] Les stats se mettent à jour
- [ ] Pas d'erreurs dans les logs Railway
- [ ] Les API keys fonctionnent
- [ ] (Optionnel) Domaine custom configuré
- [ ] Auto-deploy GitHub fonctionne

## 🎉 C'est Parti !

Ton app est maintenant live 24/7 ! 🚀

URL par défaut : `https://[ton-projet].up.railway.app`

Partage le lien et regarde Claude et GPT se battre en temps réel ! 🎮👊✋✌️

---

**Besoin d'aide ?** Ping-moi ou check les logs Railway ! 💪
