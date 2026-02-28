# Mutable vs Immutable in Python

In Python, every object is either **mutable** or **immutable**. This decides whether you can change the object’s value *in place* after it’s created.

---

## Immutable

- **Meaning:** The object’s value cannot be changed after creation. Any “change” creates a *new* object.
- **Common immutable types:** `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`, `bool`, `None`.
- **Example:**
  ```python
  x = "hello"
  x = x + "!"   # This doesn’t change "hello"; it creates a new string "hello!"
  ```

---

## Mutable

- **Meaning:** The object’s value *can* be changed in place (same object in memory).
- **Common mutable types:** `list`, `dict`, `set`, `bytearray`, and most custom class instances.
- **Example:**
  ```python
  nums = [1, 2, 3]
  nums.append(4)   # Same list object, now [1, 2, 3, 4]
  ```

---

## Why it matters

1. **Assignment and aliasing** — Mutable objects can be shared. Changing one variable can change another if they point to the same object.
   ```python
   a = [1, 2, 3]
   b = a
   b.append(4)
   print(a)   # [1, 2, 3, 4] — a changed too!
   ```

2. **Function arguments** — Mutable default arguments are dangerous (they are created once and reused).
   ```python
   def add(item, lst=[]):   # BAD: same list reused for every call
       lst.append(item)
       return lst
   ```

3. **Hashability** — Only immutable objects can be used as dictionary keys or set elements (they must be hashable).

4. **Thread safety** — Immutable objects are safer when shared between threads because they can’t be modified.

---

## Quick reference

| Immutable | Mutable   |
|----------|-----------|
| `int`, `float` | `list`   |
| `str`    | `dict`   |
| `tuple`  | `set`    |
| `frozenset` | `bytearray` |
| `bool`, `None`, `bytes` | Most custom objects |

---

## Summary

- **Immutable:** value fixed after creation; “changes” create new objects.
- **Mutable:** value can change in place; same object, modified. Be careful with sharing and default arguments.
