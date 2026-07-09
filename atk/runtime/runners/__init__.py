"""Layer 4 - runners: the runtime's public face, one module per language.

A runner answers one question for one language: given a source file, what
image do we need and what command runs it? Language modules (see
atk/languages/) plug their `run_solution` and `run_code` fields into the
functions here - nothing outside the runtime should import the lower
layers directly.

The symmetry is deliberate: a supported language has one module in
atk/languages/ (what to generate and review), one module here (how to
execute), and one recipe in runtime/containerfiles/ (the environment).

Every runner returns (ran_ok, output): True/False when the code actually
executed, or None when it could not be executed at all.
"""
