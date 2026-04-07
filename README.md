# Smart Energy OpenEnv

## Overview

This project implements a real-world OpenEnv environment where an AI agent learns how to optimize energy allocation.

The agent must decide how much energy to use from:

solar power
battery storage
grid supply

Goal:
efficiently satisfy demand while maximizing renewable energy usage.

---

## Environment API

reset() → initialize state

step(action) → apply decision

state() → return environment state

---

## Difficulty Levels

easy → fixed demand

medium → random demand

hard → high variability

---

## Reward Function

reward range: 0 to 1

reward encourages:

meeting demand
using renewable energy
reducing grid usage

---

## Run

pip install -r requirements.txt

python inference.py

---

## Real-world applications

smart grid optimization
renewable energy planning
AI based resource allocation
