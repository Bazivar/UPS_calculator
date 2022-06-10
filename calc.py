

def UPS_calc(power, battery_cap, battery_num, ext_bat_num, ext_bat_cap, ext_num, efficiency):
    pre_result = (battery_cap * 12 * battery_num + ext_bat_cap * 12 * ext_bat_num * ext_num) * efficiency/100 / power
    if pre_result > 20:
        correction_qt = 1
    else:
        correction_qt = 0.529 * pre_result ** 0.207

    result = pre_result * correction_qt
    return round(result*60)


def UPS_unrounded_calc(power, battery_cap, battery_num, ext_bat_num, ext_bat_cap, ext_num, efficiency):
    pre_result = (battery_cap * 12 * battery_num + ext_bat_cap * 12 * ext_bat_num * ext_num) * efficiency/100 / power
    if pre_result > 20:
        correction_qt = 1
    else:
        correction_qt = 0.529 * pre_result ** 0.207

    result = pre_result * correction_qt
    return result*60

