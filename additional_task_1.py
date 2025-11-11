types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

final_dict = {}

def del_duble(tickets):
    result = {}
    used_tickets = []
    for level in tickets:
        value = tickets[level]
        unique_tickets = []
        for i in value:
            if i not in used_tickets:
                unique_tickets.append(i)
                used_tickets.append(i)
        result[level] = unique_tickets
    return result


def link_level_tickets(types, tickets):
    new_tickets = del_duble(tickets)
    tickets_by_type = {}
    for key in types.keys():
        tickets_by_type[types[key]] = new_tickets[key]
    return tickets_by_type


print(link_level_tickets(types, tickets))