from flask import Flask, render_template, jsonify
from flask_cors import CORS
import anthropic
import openai
import random
import time
import json
import os
from datetime import datetime
from threading import Thread
import config

app = Flask(__name__)
CORS(app)

# Initialize API clients
anthropic_client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
openai.api_key = config.OPENAI_API_KEY

# Game state
game_state = {
    'current_match': 0,
    'current_round': 0,
    'claude_score': 0,
    'gpt_score': 0,
    'total_claude_wins': 0,
    'total_gpt_wins': 0,
    'total_matches': 0,
    'current_status': 'Initializing...',
    'last_claude_choice': None,
    'last_gpt_choice': None,
    'last_result': None,
    'last_winner': None,
    'claude_thought': '',
    'gpt_thought': '',
    'is_playing': False,
    'claude_history': [],  # Track last choices for anti-repetition
    'gpt_history': []      # Track last choices for anti-repetition
}

logs = []

def log_message(message):
    """Add timestamped log message"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    logs.append(log_entry)
    
    # Keep only last 100 logs in memory
    if len(logs) > 100:
        logs.pop(0)
    
    # Save to file
    try:
        with open('logs.json', 'w') as f:
            json.dump(logs, f, indent=2)
    except:
        pass
    
    print(log_entry)

def save_game_state():
    """Save current game state to JSON"""
    try:
        with open('game_state.json', 'w') as f:
            json.dump(game_state, f, indent=2)
    except:
        pass

def get_claude_choice():
    """Get Claude's choice with history context and anti-repetition rule"""
    try:
        # Random thought
        game_state['claude_thought'] = random.choice(config.CLAUDE_THOUGHTS)
        
        # Build history context
        history_text = ""
        if len(game_state['claude_history']) > 0:
            recent = game_state['claude_history'][-2:]  # Last 2 choices
            history_text = f"Your last choices were: {', '.join(recent)}. "
        
        # Build opponent history
        opponent_text = ""
        if len(game_state['gpt_history']) > 0:
            recent_opp = game_state['gpt_history'][-2:]
            opponent_text = f"Your opponent's last choices were: {', '.join(recent_opp)}. "
        
        # Anti-repetition rule
        forbidden = None
        if len(game_state['claude_history']) >= 2:
            if game_state['claude_history'][-1] == game_state['claude_history'][-2]:
                # Same choice twice in a row - can't do it again
                forbidden = game_state['claude_history'][-1]
        
        forbidden_text = ""
        if forbidden:
            forbidden_text = f"IMPORTANT: You have chosen {forbidden} twice in a row. You MUST choose something different this time (not {forbidden}). "
        
        # Build full prompt
        prompt = f"{history_text}{opponent_text}{forbidden_text}You are playing rock-paper-scissors. Make a strategic choice: rock, paper, or scissors. Reply with ONLY one word."
        
        message = anthropic_client.messages.create(
            model=config.CLAUDE_MODEL,
            max_tokens=20,
            temperature=1.0,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        choice = message.content[0].text.strip().lower()
        
        # Validate choice
        if choice not in config.CHOICES:
            # Try to extract valid choice from response
            for valid_choice in config.CHOICES:
                if valid_choice in choice:
                    choice = valid_choice
                    break
            else:
                # Fallback to random
                choice = random.choice(config.CHOICES)
                log_message(f"⚠️ Claude returned invalid choice, using random: {choice}")
        
        # Validate anti-repetition rule
        if forbidden and choice == forbidden:
            # AI broke the rule, force different choice
            available = [c for c in config.CHOICES if c != forbidden]
            choice = random.choice(available)
            log_message(f"⚠️ Claude tried to pick {forbidden} again, forcing: {choice}")
        
        # Update history
        game_state['claude_history'].append(choice)
        if len(game_state['claude_history']) > 5:  # Keep only last 5
            game_state['claude_history'].pop(0)
        
        return choice
        
    except Exception as e:
        log_message(f"❌ Error getting Claude's choice: {str(e)}")
        return random.choice(config.CHOICES)

def get_gpt_choice():
    """Get GPT's choice with history context and anti-repetition rule"""
    try:
        # Random thought
        game_state['gpt_thought'] = random.choice(config.GPT_THOUGHTS)
        
        # Build history context
        history_text = ""
        if len(game_state['gpt_history']) > 0:
            recent = game_state['gpt_history'][-2:]  # Last 2 choices
            history_text = f"Your last choices were: {', '.join(recent)}. "
        
        # Build opponent history
        opponent_text = ""
        if len(game_state['claude_history']) > 0:
            recent_opp = game_state['claude_history'][-2:]
            opponent_text = f"Your opponent's last choices were: {', '.join(recent_opp)}. "
        
        # Anti-repetition rule
        forbidden = None
        if len(game_state['gpt_history']) >= 2:
            if game_state['gpt_history'][-1] == game_state['gpt_history'][-2]:
                # Same choice twice in a row - can't do it again
                forbidden = game_state['gpt_history'][-1]
        
        forbidden_text = ""
        if forbidden:
            forbidden_text = f"IMPORTANT: You have chosen {forbidden} twice in a row. You MUST choose something different this time (not {forbidden}). "
        
        # Build full prompt
        prompt = f"{history_text}{opponent_text}{forbidden_text}You are playing rock-paper-scissors. Make a strategic choice: rock, paper, or scissors. Reply with ONLY one word."
        
        response = openai.chat.completions.create(
            model=config.GPT_MODEL,
            max_tokens=20,
            temperature=2.0,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        choice = response.choices[0].message.content.strip().lower()
        
        # Validate choice
        if choice not in config.CHOICES:
            # Try to extract valid choice from response
            for valid_choice in config.CHOICES:
                if valid_choice in choice:
                    choice = valid_choice
                    break
            else:
                # Fallback to random
                choice = random.choice(config.CHOICES)
                log_message(f"⚠️ GPT returned invalid choice, using random: {choice}")
        
        # Validate anti-repetition rule
        if forbidden and choice == forbidden:
            # AI broke the rule, force different choice
            available = [c for c in config.CHOICES if c != forbidden]
            choice = random.choice(available)
            log_message(f"⚠️ GPT tried to pick {forbidden} again, forcing: {choice}")
        
        # Update history
        game_state['gpt_history'].append(choice)
        if len(game_state['gpt_history']) > 5:  # Keep only last 5
            game_state['gpt_history'].pop(0)
        
        return choice
        
    except Exception as e:
        log_message(f"❌ Error getting GPT's choice: {str(e)}")
        return random.choice(config.CHOICES)

def determine_winner(claude_choice, gpt_choice):
    """Determine round winner"""
    if claude_choice == gpt_choice:
        return 'tie'
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[claude_choice] == gpt_choice:
        return 'claude'
    else:
        return 'gpt'

def play_round():
    """Play a single round"""
    game_state['current_round'] += 1
    round_num = game_state['current_round']
    
    log_message(f"🎮 ROUND {round_num} - START")
    game_state['current_status'] = f'Round {round_num} in progress...'
    save_game_state()
    
    # Get choices
    log_message("⏳ Claude is choosing...")
    claude_choice = get_claude_choice()
    game_state['last_claude_choice'] = claude_choice
    
    time.sleep(1)
    
    log_message("⏳ GPT is choosing...")
    gpt_choice = get_gpt_choice()
    game_state['last_gpt_choice'] = gpt_choice
    
    time.sleep(1)
    
    # Reveal choices
    claude_emoji = config.CHOICE_EMOJIS[claude_choice]
    gpt_emoji = config.CHOICE_EMOJIS[gpt_choice]
    
    log_message(f"💙 Claude chose: {claude_emoji} {claude_choice.upper()}")
    log_message(f"🧡 GPT chose: {gpt_emoji} {gpt_choice.upper()}")
    
    # Determine winner
    result = determine_winner(claude_choice, gpt_choice)
    game_state['last_result'] = result
    
    if result == 'tie':
        log_message("🤝 It's a TIE! Round doesn't count.")
        game_state['current_round'] -= 1  # Don't count ties
    elif result == 'claude':
        game_state['claude_score'] += 1
        log_message(f"🎉 Claude WINS Round {round_num}! Score: Claude {game_state['claude_score']} - {game_state['gpt_score']} GPT")
    else:
        game_state['gpt_score'] += 1
        log_message(f"🎉 GPT WINS Round {round_num}! Score: Claude {game_state['claude_score']} - {game_state['gpt_score']} GPT")
    
    save_game_state()
    time.sleep(config.ROUND_DELAY)

def play_match():
    """Play a full match (Best of 3)"""
    game_state['current_match'] += 1
    game_state['current_round'] = 0
    game_state['claude_score'] = 0
    game_state['gpt_score'] = 0
    game_state['last_claude_choice'] = None
    game_state['last_gpt_choice'] = None
    game_state['last_result'] = None
    # Reset history at start of each match
    game_state['claude_history'] = []
    game_state['gpt_history'] = []
    
    match_num = game_state['current_match']
    
    log_message("=" * 60)
    log_message(f"🏁 MATCH #{match_num} - STARTING (Best of {config.BEST_OF})")
    log_message("=" * 60)
    
    # Play rounds until someone wins
    while game_state['claude_score'] < 2 and game_state['gpt_score'] < 2:
        play_round()
    
    # Determine match winner
    if game_state['claude_score'] > game_state['gpt_score']:
        winner = 'claude'
        game_state['total_claude_wins'] += 1
        log_message("🏆 CLAUDE WINS THE MATCH!")
    else:
        winner = 'gpt'
        game_state['total_gpt_wins'] += 1
        log_message("🏆 GPT WINS THE MATCH!")
    
    game_state['last_winner'] = winner
    game_state['total_matches'] += 1
    
    log_message(f"📊 OVERALL STATS - Total Matches: {game_state['total_matches']} | Claude: {game_state['total_claude_wins']} - GPT: {game_state['total_gpt_wins']}")
    log_message("=" * 60)
    
    save_game_state()
    time.sleep(config.MATCH_DELAY)

def game_loop():
    """Main game loop"""
    log_message("🚀 AI RPS BATTLE - System Initialized")
    log_message("🤖 Claude Haiku 4.5 vs GPT-4o-mini")
    log_message("📡 Continuous play mode: ACTIVE")
    
    game_state['is_playing'] = True
    
    while config.AUTO_PLAY:
        try:
            play_match()
        except Exception as e:
            log_message(f"❌ Error in game loop: {str(e)}")
            time.sleep(5)

# Flask routes
@app.route('/')
def index():
    """Serve main page"""
    return render_template('viewer.html')

@app.route('/api/state')
def get_state():
    """Get current game state"""
    return jsonify(game_state)

@app.route('/api/logs')
def get_logs():
    """Get recent logs"""
    return jsonify(logs[-50:])  # Last 50 logs

@app.route('/api/stats')
def get_stats():
    """Get game statistics"""
    total_matches = game_state['total_matches']
    
    stats = {
        'total_matches': total_matches,
        'claude_wins': game_state['total_claude_wins'],
        'gpt_wins': game_state['total_gpt_wins'],
        'claude_win_rate': round((game_state['total_claude_wins'] / total_matches * 100), 1) if total_matches > 0 else 0,
        'gpt_win_rate': round((game_state['total_gpt_wins'] / total_matches * 100), 1) if total_matches > 0 else 0
    }
    
    return jsonify(stats)

# Initialize files on startup
def init_files():
    """Initialize JSON files if they don't exist"""
    if not os.path.exists('logs.json'):
        with open('logs.json', 'w') as f:
            json.dump([], f)
    
    if not os.path.exists('game_state.json'):
        save_game_state()

if __name__ == '__main__':
    # Initialize files
    init_files()
    
    # Start game loop in background thread
    game_thread = Thread(target=game_loop, daemon=True)
    game_thread.start()
    
    # Start Flask server
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
