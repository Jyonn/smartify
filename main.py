from smartify import E, P, Analyse


@E.register()
class MathError:
    DIV_ZERO = E("除数不能为0")
    POSITIVE = E("需要为正数")


def positive_check(v):
    """check if value is positive"""

    if v < 0:
        raise MathError.POSITIVE


def not_zero(v):
    """check if value is zero"""

    if v == 0:
        raise MathError.DIV_ZERO


pos_num = P('positive', '正数').process(float).validate(positive_check)
divided_num = pos_num.clone().rename('divided').validate(not_zero)


@Analyse.p(pos_num, divided_num)
def div(positive, divided):
    return positive // divided


print(div(999.9, '-0.2'))
