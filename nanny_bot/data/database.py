nannies = {}

def add_nanny(user_id, nanny_data):
    nannies[user_id] = nanny_data

def get_nanny(user_id):
    return nannies.get(user_id)

def get_all_nannies():
    return list(nannies.values())


# бд постгрес или что-то другое
