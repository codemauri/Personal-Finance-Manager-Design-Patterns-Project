# Design Patterns Reflection

## Singleton (Balance)

There should be only one Balance instance in the application. Without the Singleton pattern, different parts of the program could create separate instances, each tracking its own balance. This leads to inconsistent state and hard-to-debug issues where transactions appear to vanish or duplicate depending on which instance is being referenced.

## Adapter (TransactionAdapter)

ExternalFreelanceIncome is a third-party object with a different structure — it carries invoice IDs and project descriptions that our internal system doesn't use. Because it's external, we can't modify it. Our system relies on the Transaction interface across multiple methods. The Adapter pattern translates the foreign, immutable object into the interface our system understands, without requiring changes to either side.

## Observer (PrintObserver + LowBalanceAlertObserver)

Without the Observer pattern, notification logic would live directly inside `apply_transaction`, tightly coupling the Balance class to every dependent object. Adding or removing dependents would require modifying the subject, and as the system grows, this dependency web becomes fragile and prone to break. The Observer pattern decouples business logic (Balance) from notification logic (PrintObserver, LowBalanceAlertObserver). Multiple observers can subscribe to the subject and receive broadcasts when it changes. We can add or remove observers without modifying the Balance class at all.

## Command (CommandManager + ApplyTransactionCommand)

Calling `apply_transaction` directly couples the caller to the implementation. The Command pattern encapsulates each request as a self-contained object, turning an action and its receiver into an independent unit. The invoker (CommandManager) triggers commands without knowing implementation details. This supports undo/redo operations, command history, and queueing — capabilities that would be difficult to retrofit into direct method calls. In this project, `CommandManager.undo_last()` demonstrates reversing the last transaction with no changes to the Balance class.

## Trade-offs and Challenges

- The Singleton pattern complicated unit testing: because `Balance()` always returns the same instance, state accumulated across tests. Each test required a `setUp` method calling `reset()` to ensure a clean starting point — a friction that wouldn't exist with regular classes.
- The Observer's `LowBalanceAlertObserver` needed to reflect *current* state, not just trigger once. The `alert_triggered` flag had to reset to `False` when the balance recovered above the threshold, which was easy to overlook.
- The Command pattern introduces additional classes and indirection for what could be a single method call. In a small application like this, the overhead may not seem justified — its value becomes clearer as the system scales and features like undo, logging, or command queueing are needed.
- The Adapter adds a translation layer that, in this case, is a simple conversion. The trade-off is worthwhile when the external interface is truly outside your control, but it can feel like unnecessary ceremony for trivial conversions.
