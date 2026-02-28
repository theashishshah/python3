# Python Internal Memory — How It Works (Basics)
- python ref variable doesn't has type but where the value is stored is done using types
Understanding how Python uses memory helps you avoid bugs and write clearer code. Here are the main ideas.

---

## Variables are references, not boxes

- In Python, **variables do not “hold” values**. A variable is a **name** (reference) that **points to an object** in memory.
- The **object** has the type and the value; the variable is just a label.
- You can have many names pointing to the **same object**.

```python
a = [1, 2, 3]
b = a          # b points to the SAME list as a (not a copy)
b.append(4)
print(a)       # [1, 2, 3, 4] — same object, so a “sees” the change
```

---

## Assignment: rebinding the name

- **Assignment** (`x = something`) makes the name `x` point to a (possibly new) object. It does **not** change the old object.
- For **immutable** values (e.g. numbers, strings), “changing” a variable just points it to a new object. Other names still point to the old one.

```python
a = 10
b = a          # b points to the same 10 as a
a = 14         # a now points to 14; b still points to 10
# So: a == 14, b == 10
```

---

## Identity vs equality

- **`==`** — Compares **values** (are they equal?).
- **`is`** — Compares **identity** (do they refer to the **same object** in memory?).

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same contents
print(a is b)   # False — different objects in memory

x = [1, 2, 3]
y = x
print(x is y)   # True  — same object
```

So: **same value** does **not** mean **same object**. Only when you assign one name to another (`y = x`) do they point to the same object.

---

## Finding the object: `id()` and `is`

- **`id(x)`** — Returns the **memory address** (identity) of the object `x` points to. Two names pointing to the same object have the same `id`.
- **`x is y`** is equivalent to **`id(x) == id(y)`**.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))   # True — same object
```

---

## Reference counting and garbage collection

- Python keeps track of **how many references** point to each object (**reference count**).
- When the count drops to **zero**, no name uses that object anymore, so Python can **free the memory** (garbage collection).
- You can see the current reference count with **`sys.getrefcount(x)`** (the count is often 1 higher than you expect, because passing `x` to `getrefcount` adds a temporary reference).

```python
import sys
my_list = [1, 2, 3]
your_list = my_list
hello_list = your_list
# Three names point to the same list
print(sys.getrefcount(my_list))   # e.g. 4 (3 names + 1 from the function argument)
```

- For **small integers** and **some strings**, Python may **reuse** the same object (interning/caching) for efficiency. So their reference count stays higher longer, and they are freed later.

---

## Same value vs same object (creating new objects)

| Code              | Same value? | Same object? |
|-------------------|------------|--------------|
| `a = [1,2,3]`     | —          | —            |
| `b = a`           | Yes        | **Yes**      |
| `b = [1,2,3]`     | Yes        | **No**       |

- **`b = a`** → one object, two names (aliasing).
- **`b = [1, 2, 3]`** (new literal) → two objects, same value. Use **`b = a.copy()`** or **`b = list(a)`** when you want a **copy** of a list.

---

## Why this matters

1. **Mutable aliasing** — If two names point to the same list/dict, changing one “changes” the other. Prefer copies when you need independent data.
2. **Default arguments** — A mutable default (e.g. `def f(x, lst=[])`) is **one** object shared by all calls. Use `None` and create a new list inside the function instead.
3. **`is` vs `==`** — Use `is` only when you care about “same object” (e.g. `if x is None`). For values, use `==`.

---

## Quick mental model

- **Objects** live in memory and have type and value.
- **Variables** are names that **reference** those objects.
- **Assignment** rebinds a name to an object; it does not copy the object (for mutable types, that’s why aliasing happens).
- **Reference counting** decides when an object can be freed; **`id()`** and **`is`** tell you whether two names point to the same object.

---

## Summary

Variables are **references** to **objects**. Assignment makes a name point to an object; it does not copy it. Use **`==`** for value equality and **`is`** (or **`id()`**) for identity. Multiple names can point to one object (reference counting); when no name points to it, Python can reclaim the memory. This is why mutable aliasing and default arguments can surprise you — always keep “same object” vs “same value” in mind.
