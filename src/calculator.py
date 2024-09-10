from __future__ import annotations

from typing import Union

class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both args should be numeric")
        return x/y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        return x + y

if __name__ == "__main__":
    calculator = Calculator()