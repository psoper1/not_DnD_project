class Combat:
    def __init__(self, success_hit, fail_hit, crit_hit, check_hp, check_alive):
        self.success_hit = success_hit
        self.fail_hit = fail_hit
        self.crit_hit = crit_hit
        self.check_hp = check_hp
        self.check_alive = check_alive