# Object Types / Data Types in Python

Python has built-in object types for different kinds of data. Here’s a concise overview with examples.

---

## 1. Number

- **int:** `1234`
- **float:** `3.1415`
- **complex:** `3+4j`
- **binary literal:** `0b111`
- **Decimal:** `Decimal()` — exact decimal arithmetic (e.g. money)
- **Fraction:** `Fraction()` — exact rationals (e.g. 1/3)

---

## 2. String

- **str:** `'spam'`, `"Bob's"`
- **bytes:** `b'a\x01c'` — raw bytes
- **Unicode:** `u'sp\xc4m'` (Python 3 strings are Unicode by default)

---

## 3. List

- **list:** `[1, [2, 'three'], 4.5]` — ordered, mutable sequence
- **from range:** `list(range(10))` — e.g. `[0, 1, 2, ..., 9]`

---

## 4. Tuple

- **tuple:** `(1, 'spam', 4, 'U')` — ordered, immutable sequence
- **from iterable:** `tuple('spam')` → `('s', 'p', 'a', 'm')`
- **namedtuple** — tuple with named fields (like a light-weight record)

---

## 5. Dictionary

- **dict literal:** `{'food': 'spam', 'taste': 'yum'}`
- **dict constructor:** `dict(hours=10)` → `{'hours': 10}`  
  Key–value pairs; keys must be hashable (e.g. immutable).

---

## 6. Set

- **set:** `set('abc')` or `{'a', 'b', 'c'}` — unordered, unique items, mutable
- **frozenset** — immutable set (hashable)

---

## 7. File

- **open:** `open('eggs.txt')` — text mode (read/write strings)
- **binary:** `open(r'C:\ham.bin', 'wb')` — binary mode (read/write bytes)  
  Use `with open(...) as f:` so the file is closed automatically.

---

## 8. Boolean

- **bool:** `True`, `False`  
  Used in conditions, comparisons, and logical operations.

---

## 9. None

- **NoneType:** `None`  
  Represents “no value” or missing value; often used as default or placeholder.

---

## 10. Functions, modules, classes

- **Functions** — callable objects defined with `def` or `lambda`
- **Modules** — Python files you `import` (e.g. `import os`)
- **Classes** — blueprints for objects; instances are objects with attributes and methods

---

## 11. Advanced types

- **Decorators** — modify or wrap functions/classes (e.g. `@staticmethod`, `@property`)
- **Generators** — functions that `yield`; produce values one at a time (memory-efficient)
- **Iterators** — objects that support `next()`; used in `for` loops
- **MetaProgramming** — code that creates or modifies code (e.g. metaclasses, dynamic attributes)

---

## Which data types are used most, and where?

| Data type   | Use frequency | Where you’ll see them |
|------------|----------------|------------------------|
| **list**   | Very high      | Loops, APIs, parsing, any sequence of items (e.g. rows, options, results). |
| **dict**   | Very high      | JSON, config, caches, key–value data, API requests/responses, settings. |
| **str**    | Very high      | Input/output, file content, URLs, messages, logging, formatting. |
| **int / float** | High  | Counts, IDs, math, metrics, prices, coordinates. |
| **bool**   | High           | Conditions, flags, feature toggles, validation results. |
| **None**   | High           | Default return value, “no value”, optional arguments. |
| **tuple**  | Medium         | Fixed-size data, return multiple values, dict keys, coordinates, DB rows. |
| **set**    | Medium         | Unique items, membership tests, removing duplicates, tags, categories. |
| **File (open)** | Medium   | Reading/writing files, CSV/JSON/text processing. |
| **bytes**  | Lower          | Binary data, network, encoding/decoding. |
| **Decimal / Fraction** | Niche | Finance, exact math when float is not enough. |
| **complex** | Niche         | Science, engineering, signal processing. |
| **Generators / iterators** | Medium–high | Large data, streams, `range()`, comprehensions, pipelines. |
| **Decorators / classes**  | Grows with codebase | Structure, reuse, frameworks (Flask, Django, etc.). |

**In practice:** In most apps and scripts you’ll use **list**, **dict**, **str**, **int**, **float**, **bool**, and **None** most of the time. **Tuple** and **set** show up when you need immutability or uniqueness. **Files**, **generators**, and **classes** become important as soon as you work with I/O, large data, or bigger projects.
