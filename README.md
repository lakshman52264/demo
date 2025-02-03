# Calculator Repository

This repository contains a simple calculator class that provides basic arithmetic operations. The purpose of this repository is to demonstrate the implementation of a calculator class in Python.

## Calculator Class

The `calculator` class provides the following methods:

- `add(a, b)`: Returns the sum of `a` and `b`.
- `sub(a, b)`: Returns the difference between `a` and `b`.
- `mul(a, b)`: Returns the product of `a` and `b`.
- `div(a, b)`: Returns the quotient of `a` divided by `b`.
- `pow(a, b)`: Returns `a` raised to the power of `b`.

## Usage Instructions

To use the `calculator` class, follow these steps:

1. Import the `calculator` class from the `calc` module.
2. Create an instance of the `calculator` class.
3. Call the desired method on the instance with the appropriate arguments.

Example:

```python
from calc import calculator

calc = calculator()

result_add = calc.add(5, 3)
result_sub = calc.sub(5, 3)
result_mul = calc.mul(5, 3)
result_div = calc.div(5, 3)
result_pow = calc.pow(5, 3)

print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)
print("Power:", result_pow)
```

## Examples

Here are some examples of how to use the `calculator` class:

### Example 1: Addition

```python
from calc import calculator

calc = calculator()
result = calc.add(10, 5)
print("Addition:", result)
```

### Example 2: Subtraction

```python
from calc import calculator

calc = calculator()
result = calc.sub(10, 5)
print("Subtraction:", result)
```

### Example 3: Multiplication

```python
from calc import calculator

calc = calculator()
result = calc.mul(10, 5)
print("Multiplication:", result)
```

### Example 4: Division

```python
from calc import calculator

calc = calculator()
result = calc.div(10, 5)
print("Division:", result)
```

### Example 5: Power

```python
from calc import calculator

calc = calculator()
result = calc.pow(2, 3)
print("Power:", result)
```
