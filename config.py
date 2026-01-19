import os

# API Configuration
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', 'your-anthropic-key-here')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-key-here')

# Model Configuration
CLAUDE_MODEL = "claude-haiku-4-5-20251001"
GPT_MODEL = "gpt-4o-mini"

# Game Configuration
BEST_OF = 3  # Best of 3 rounds
ROUND_DELAY = 4  # Seconds between rounds
MATCH_DELAY = 5  # Seconds between matches
AUTO_PLAY = True  # Continuous play

# Server Configuration
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', 5000))
DEBUG = False

# Game Choices
CHOICES = ['rock', 'paper', 'scissors']
CHOICE_EMOJIS = {
    'rock': '👊',
    'paper': '✋',
    'scissors': '✌️'
}

# AI Thoughts (phrases drôles/originales)
CLAUDE_THOUGHTS = [
    "Claude is analyzing quantum probabilities...",
    "Claude feels the energy of victory",
    "Claude is channeling ancient wisdom",
    "Claude's circuits are tingling",
    "Claude senses a disturbance in the force",
    "Claude is feeling lucky today",
    "Claude's neural networks are firing",
    "Claude is in the zone"
]

GPT_THOUGHTS = [
    "GPT is calculating optimal strategy...",
    "GPT smells victory in the air",
    "GPT's confidence level: MAXIMUM",
    "GPT is ready to dominate",
    "GPT senses an opportunity",
    "GPT is feeling unstoppable",
    "GPT's algorithms are optimized",
    "GPT is locked in"
]
