# A2A Server Template For Claude-Side Agent

This template is a minimal skeleton for exposing a Claude Agent SDK-based agent through an A2A-compliant HTTP service boundary.

## Purpose

- publish an agent card
- accept A2A-style task submission
- return task state and results
- preserve task ids and trace ids across the delegation boundary

## Files

- `agent_card.json`: starter agent metadata
- `app.py`: minimal HTTP skeleton
- `tasks.py`: in-memory task lifecycle stub
- `models.py`: simple request and response models

## Notes

- This is a protocol-facing scaffold, not a complete A2A implementation.
- Replace placeholder request and response models with the exact A2A binding you standardize on.
- Keep destructive actions behind downstream approval even if the remote agent recommends them.
