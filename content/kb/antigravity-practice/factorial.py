def factorial(n: int) -> int:
    """
    計算非負整數 n 的階乘 (Factorial)。

    Args:
        n (int): 非負整數。

    Returns:
        int: n 的階乘結果。

    Raises:
        ValueError: 當輸入為負數時。
        TypeError: 當輸入整數時。
    """
    if not isinstance(n, int):
        raise TypeError("輸入必須是整數 (Integer)。")
    if n < 0:
        raise ValueError("輸入必須是非負整數 (Non-negative integer)。")

    # 核心演算法
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # 測試程式碼
    test_values = [0, 1, 5, 10]
    print("開始測試階乘計算：")
    for val in test_values:
        print(f"factorial({val}) = {factorial(val)}")
