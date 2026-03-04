# Python Method Types — `self`, `cls`, and `@staticmethod`

---

# 1️⃣ Instance Methods (`self`)

## What is `self`?

- `self` represents **one specific object (instance)**.
- It gives access to that object's attributes.
- It is used in **instance methods**.
- It is always the first parameter.

---

## Example

```python
class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
```

Usage:

```python
account = BankAccount("Alice", 100.0)
account.deposit(50.0)
```

Here:

- `self` refers to `account`
- `self.balance` modifies this specific account

---

## When to Use an Instance Method

Use `self` when:

- The method reads object data
- The method modifies object state
- The behavior depends on that specific object

If the method needs `self.attribute`, it must be an instance method.

---

# 2️⃣ Class Methods (`@classmethod`, `cls`)

## What is `cls`?

- `cls` represents the **class itself**
- Not an instance
- The blueprint used to create objects
- It is always the first parameter of a `@classmethod`

---

## Example

```python
class Library:
    total_books = 0

    def __init__(self, title: str) -> None:
        self.title = title
        Library.total_books += 1

    @classmethod
    def get_total_books(cls) -> int:
        return cls.total_books
```

Usage:

```python
Library.get_total_books()
```

Here:

- `cls` refers to `Library`
- `cls.total_books` accesses class-level data

---

## Factory Example

```python
class User:
    def __init__(self, username: str, active: bool) -> None:
        self.username = username
        self.active = active

    @classmethod
    def create_guest(cls):
        return cls("Guest", False)
```

Why use `cls("Guest", False)` instead of `User("Guest", False)`?

Because if `User` is subclassed, this method still works correctly.

---

## When to Use `@classmethod`

Use it when:

- You need access to class variables
- You are creating alternative constructors
- The method should support inheritance
- The logic belongs to the class, not a specific instance

---

# 3️⃣ Static Methods (`@staticmethod`)

## What is a Static Method?

- A function defined inside a class
- Does NOT receive `self`
- Does NOT receive `cls`
- Does NOT access instance or class data
- Used to logically group related helper functions

---

## Example

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32
```

Usage:

```python
TemperatureConverter.celsius_to_fahrenheit(25)
```

This method:

- Does not use `self`
- Does not use `cls`
- Simply performs a related utility calculation

---

## When to Use `@staticmethod`

Use it when:

- The method does not need instance data
- The method does not need class data
- The function logically belongs to the class
- It is conceptually related but independent

If the function is unrelated to the class, define it outside the class instead.

---

# 4️⃣ Quick Comparison Table

| Method Type      | First Parameter | Uses Instance Data | Uses Class Data | Typical Purpose |
|------------------|----------------|--------------------|-----------------|-----------------|
| Instance Method  | `self`        | ✅ Yes             | ⚠️ Indirectly   | Modify object state |
| Class Method     | `cls`         | ❌ No              | ✅ Yes          | Factories, shared counters |
| Static Method    | None          | ❌ No              | ❌ No           | Utility/helper logic |

---

# 5️⃣ Decision Rules

Ask these questions in order:

1. Does this method need to access or modify instance attributes?
   → Use an instance method (`self`).

2. Does this method need to access class-level data or support inheritance?
   → Use a class method (`@classmethod`, `cls`).

3. Does this method need neither instance nor class data, but still logically belongs to this class?
   → Use a static method (`@staticmethod`).

4. Is it completely unrelated to the class?
   → Make it a standalone function.

---

# 6️⃣ Mental Model

```
Class (Blueprint)  ← cls refers to this

   |
   ├── object1     ← self refers to this specific instance
   ├── object2
   └── object3
```

- `self` → one specific object
- `cls` → the class itself
- `@staticmethod` → grouped utility logic