def solution(bandage, health, attacks):
    current_health = health

    attack_idx = 0
    second = 1
    band_second = 0
    while True:
        print(current_health)
        if attack_idx == len(attacks):
            break
            
        if attacks[attack_idx][0] == second:
            current_health -= attacks[attack_idx][1]
            attack_idx += 1
            second += 1
            band_second = 0
        else:
            if current_health < health:
                if band_second == bandage[0] - 1:
                    current_health += bandage[2] + bandage[1]
                    second += 1
                    band_second = 0
                else:
                    current_health += bandage[1]
                    band_second += 1
                    second += 1
            else:
                second += 1
    
        if current_health <= 0:
            current_health = -1
            break
    
        if current_health > health:
            current_health = health
        
    return current_health