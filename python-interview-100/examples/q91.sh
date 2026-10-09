#!/usr/bin/env bash
# Q91 Python 程序慢，第一步该做什么？
python -m cProfile -o profile.out app.py
# 生产环境可进一步考虑采样 profiler，以降低侵入性。
