# Alcami ad pipeline — common tasks.
.PHONY: check verify update-golden policy

# Contract tests: campaigns validate, prompts unchanged, CLAUDE.md <-> engine consistent.
check:
	python3 tests/test_pipeline.py

# Always-true invariants only (validation + facts, no golden) — what the enforcement hook runs.
verify:
	python3 tests/test_pipeline.py --invariants

# Regenerate the golden prompt hashes AFTER a deliberate engine change (review the diff first).
update-golden:
	python3 tests/test_pipeline.py --update

# The live format / archetype / audience / lever matrix.
policy:
	python3 gen.py --policy
