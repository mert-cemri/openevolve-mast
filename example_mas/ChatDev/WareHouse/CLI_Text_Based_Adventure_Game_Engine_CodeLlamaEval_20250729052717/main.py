#!/usr/bin/env python3
import argparse
import json
import sys
from game_engine import GameEngine
def main():
    parser = argparse.ArgumentParser(description='CLI engine for a simple text-based adventure game')
    parser.add_argument('--data', help='JSON or YAML file containing game data', required=True)
    args = parser.parse_args()
    with open(args.data, 'r') as f:
        game_data = json.load(f)
    game_engine = GameEngine(game_data)
    game_engine.run()
if __name__ == '__main__':
    main()