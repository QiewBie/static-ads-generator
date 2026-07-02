"""Brand facts — the single home for the literal claims the pipeline both RENDERS and
GUARDS, so the two never drift. `prompt_builder` imports these to build the prompt;
`pb_validate` imports the same values to check rendered text against them. The facts test
(`tests/test_pipeline.py`) asserts CLAUDE.md states them too — closing the loop across all
three authorities (engine renders · validator guards · CLAUDE.md declares).

Add a fact here, reference it from both sides — never re-type a price or the customer count
as a bare literal in `prompt_builder` or `pb_validate`.
"""

# ── Price anchors (member, per the brand) ─────────────────────────────────────
PRICES = {
    "tea":   "From $37.40/month",
    "blend": "From $39/month",
}
# Bare price tokens the validator uses to catch cross-product leakage (a tea ad showing
# the blend price, or vice-versa). Derived from PRICES so they can't disagree.
BLEND_PRICE_TOKEN = "$39"      # belongs to PRICES["blend"]
TEA_PRICE_TOKEN   = "$37.40"   # belongs to PRICES["tea"]

# ── Customer-count trust line — a BLEND claim only ────────────────────────────
# Tea never uses a customer number (it uses "loved by thousands" / 4.9★).
CUSTOMER_COUNT     = "200,000+ customers"   # the rendered trust line
CUSTOMER_COUNT_NUM = "200,000"              # the bare number the validator guards
