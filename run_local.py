#!/usr/bin/env python3
"""
Script de test local pour AI RPS Battle
Lance le serveur en mode debug
"""

import os
import sys

# Set debug mode for local testing
os.environ['DEBUG'] = 'True'

# Import and run the main app
from rps_battle import app, init_files, game_loop
from threading import Thread

if __name__ == '__main__':
    print("🎮 AI RPS BATTLE - Local Test Mode")
    print("=" * 60)
    print("📡 Starting server on http://localhost:5000")
    print("🤖 Claude Haiku 4.5 vs GPT-4o-mini")
    print("=" * 60)
    
    # Initialize files
    init_files()
    
    # Start game loop in background
    game_thread = Thread(target=game_loop, daemon=True)
    game_thread.start()
    
    # Start Flask in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)
