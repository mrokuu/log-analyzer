def get_log(invalid_logs=None, faulty_percentage=100, report_time=0, min_temp=None, max_temp=None, average_temp=None,
            longest_overheat_time=0, overhead_periods=0, high_em=False, damage_risk=False):
    if invalid_logs is None:
        invalid_logs = []

    def format_temp(temp):
        return str(round(temp, 1)) if temp is not None else None

    return {
        "wadliwe_logi": invalid_logs,
        "procent_wadliwych_logow": str(round(faulty_percentage, 1)),
        "czas_trwania_raportu": int(report_time),
        "temperatura": {
            "max": format_temp(max_temp),
            "min": format_temp(min_temp),
            "srednia": format_temp(average_temp)
        },
        "najdluzszy_czas_przegrzania": int(longest_overheat_time),
        "liczba_okresow_przegrzania": int(overhead_periods),
        "problemy": {
            "wysoki_poziom_zaklocen_EM": high_em,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": damage_risk
        }
    }