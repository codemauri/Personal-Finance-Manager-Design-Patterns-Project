# Code Review Summary

## Changes Applied from Code Review Feedback

1. **Command undo routing through `apply_transaction()`** — So observers get notified on undo, not just on execute. Uses compensating transactions instead of mutating the original transaction (immutability for accounting integrity).

2. **Import fix** — `from transaction import transaction` (module) changed to `from transaction.transaction import Transaction` (class). Fixed `UnboundLocalError` caused by local variable shadowing the module name.

3. **Hardcoded amount in undo** — Replaced `200` with `self.transaction.amount` so undo works for any transaction, not just the test case.

4. **Removed debug `print`** from `Balance.__new__` — Useful during development, not in finished code.

5. **`reset()` now clears `_observers`** — Singleton was leaking registered observers across test classes. Fixed for proper test isolation.

6. **Removed stale TODO comments** — Three fully-implemented sections still had TODO markers.

7. **Added print to `LowBalanceAlertObserver`** — The alert flag was correct but silent. An alert observer should actually alert.

All 16 tests passing throughout. Every fix was a polish/correctness improvement — pattern implementations were structurally sound from the start.
