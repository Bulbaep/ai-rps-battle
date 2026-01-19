# Changelog

Toutes les modifications notables de ce projet seront documentées ici.

## [1.0.0] - 2025-01-18

### ✨ Première version

**Fonctionnalités principales**
- ✅ Système de battle automatique (Best of 3)
- ✅ Interface web 3 colonnes (Terminal / Jeu / Stats)
- ✅ Intégration Claude Haiku 4.5 + GPT-4o-mini
- ✅ Logs en temps réel
- ✅ Stats globales et win rates
- ✅ AI Thoughts (phrases drôles)
- ✅ Auto-play 24/7
- ✅ Dark theme design
- ✅ Ready for Railway deployment

**Stack**
- Backend: Flask + Python 3.11
- Frontend: HTML/CSS/JS vanilla
- APIs: Anthropic + OpenAI
- Hosting: Railway-ready

**Fichiers créés**
- `rps_battle.py` - Script principal
- `config.py` - Configuration
- `templates/viewer.html` - Interface
- `requirements.txt` - Dépendances
- `Procfile` - Railway config
- `runtime.txt` - Python version
- `README.md` - Documentation
- `DEPLOYMENT.md` - Guide déploiement
- `logs.json` - Logs template
- `game_state.json` - State template
- `.gitignore` - Git exclusions
- `run_local.py` - Test local

**Coûts estimés**
- ~$0.0005 par match
- ~$4.50/mois en 24/7

---

## [Roadmap Future] - À venir

### Version 1.1 (Court terme)
- [ ] Système de pause/resume
- [ ] Ajuster délais via interface
- [ ] Export stats en CSV
- [ ] Dark/Light mode toggle
- [ ] Son/musique d'ambiance

### Version 1.5 (Moyen terme)
- [ ] Database (SQLite/PostgreSQL)
- [ ] Historique complet des matchs
- [ ] Graphiques win rates over time
- [ ] Streaks et records
- [ ] API publique REST

### Version 2.0 (Long terme)
- [ ] Système de gambling crypto
- [ ] Multi-AIs tournament mode
- [ ] WebSocket pour real-time (sans refresh)
- [ ] Authentication système
- [ ] Betting history et leaderboard

---

**Format du changelog**
- 🎉 Nouvelle feature
- 🐛 Bug fix
- ⚡ Performance
- 📝 Documentation
- 🔧 Configuration
- 🎨 UI/UX
