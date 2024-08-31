N = float(input())

def decimal_normalize(value):
    """
    浮動小数点数の場合、末尾の不要な0を削除する。
    整数値の場合、そのまま整数として返す。

    Parameters
    ----------
    value : float or int
        対象となる数値。

    Returns
    -------
    int or float
        不要な末尾の0が削除された数値。
    """
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

print(decimal_normalize(N))