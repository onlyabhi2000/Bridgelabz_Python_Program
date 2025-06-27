```Pytest : Is an testting framework for python  , which supports auto discovery of tests . it also supports parameterized and fixture based testing```

✅ Rule of Mocking: Patch "where it is used, not where it is defined."

===================
Topics covered :
- basic syntax
- function based test
- class based test
- fixtures  
- confest
- parametrize and mark
- mocking
===================





============================================
The assert statement checks if the expression after it is truthy.

assert True is like saying:

"I expect True to be True"

That’s always correct, so the test passes.

============================================

🔍 What is a Fixture?
A fixture in pytest is a way to define reusable, setup-and-teardown logic outside of test classes — for:
Creating test data
Connecting to databases
Initializing objects
Cleaning up after tests
It replaces setup_method / setup_class with a more modular and flexible approach.

============================================

@pytest.mark.parametrize: Multiple test cases, one test function

@pytest.mark: Tagging & Grouping Tests
You can tag tests for:
Selective running
Skipping
Expecting failures
Custom labels



| Mark                 | Description                                  |
| -------------------- | -------------------------------------------- |
| `@pytest.mark.skip`  | Skip this test                               |
| `@pytest.mark.xfail` | Test is expected to fail (won’t break suite) |
| `@pytest.mark.slow`  | Custom marker to run only some tests         |


============================================

Mocking

🧪 What is Mocking?
Mocking is the process of replacing parts of your code (like a function, method, or object) with a fake version during tests, so you can:

Control what it returns
Track if it was called
Avoid side effects like real API calls, DB writes, file reads, etc.

When Should You Use Mocking------>

| Scenario                      | Why Mock?                            |
| ----------------------------- | ------------------------------------ |
| External APIs                 | Avoid hitting real services          |
| Database operations           | Don't modify real data               |
| File system access            | Avoid creating files                 |
| Slow or random logic          | Make tests fast & deterministic      |
| Inter-component communication | Check if functions interact properly |
