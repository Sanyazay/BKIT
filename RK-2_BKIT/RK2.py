from operator import itemgetter


class Microprocessor:
    def __init__(self, id, name, freq, computer_id):
        self.id = id
        self.name = name
        self.freq = freq
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class MicCom:
    def __init__(self, proc_id, comp_id):
        self.proc_id = proc_id
        self.comp_id = comp_id


micros = [
    Microprocessor(1, "intel1", 2300, 1),
    Microprocessor(2, "ryzen1", 2400, 3),
    Microprocessor(3, "ryzen3", 3500, 2),
    Microprocessor(4, "ryzen7", 4200, 4),
    Microprocessor(5, "ryzen5", 6500, 3),
    Microprocessor(6, "pentium1", 5643, 1),
    Microprocessor(7, "xenon9", 3456, 2),
    Microprocessor(8, "intel3", 2950, 1),
    Microprocessor(9, "intel9", 4053, 3),
]
comps = [
    Computer(1, "RussianButcher"),
    Computer(2, "Buster"),
    Computer(3, "Evelon"),
    Computer(4, "TORONTOTOKYO"),
]

miccomps = [
    MicCom(1, 1),
    MicCom(2, 3),
    MicCom(3, 2),
    MicCom(4, 4),
    MicCom(5, 3),
    MicCom(6, 1),
    MicCom(2, 1),
    MicCom(8, 1),
    MicCom(9, 3),
    MicCom(3, 1),
    MicCom(8, 3),
    MicCom(6, 4),
    MicCom(7, 1),
    MicCom(7, 3),
    MicCom(1, 2),
    MicCom(7, 3),
    MicCom(2, 2),
    MicCom(1, 4),
    MicCom(9, 4),
]

def sortingB1(one_to_many):
    one_to_many = sorted(one_to_many, key=lambda x: x[0])
    return one_to_many
def sortingB2(one_to_many):
    res_12_unsorted = []
    for c in comps:

        c_micros = list(filter(lambda i: i[2] == c.name, one_to_many))

        if len(c_micros) > 0:
            res_12_unsorted.append((c.name, len(c_micros)))
    res12 = sorted(res_12_unsorted, key=lambda x: x[1], reverse=True)
    return res12
def sortingB3(many_to_many):
    res_13 = {}
    for m in micros:
        if m.name.endswith("1"):
            m_comps = list(filter(lambda i: i[0] == m.name, many_to_many))
            m_comps_name = [x[2] for x in m_comps]
            res_13[m.name] = m_comps_name
    return res_13
def main():

    one_to_many = [
        (m.name, m.freq, c.name) for c in comps for m in micros if m.computer_id == c.id
    ]
    
    many_to_many = [
        (m.name, m.freq, c.name)
        for c in comps
        for m in micros
        for r in miccomps
        if c.id == r.comp_id and m.id == r.proc_id
    ]
    
    print("Задание Б1")

    res1 = sortingB1(one_to_many)
    [print(x) for x in res1]

    print("\nЗадание Б2")
    res12 = sortingB2(one_to_many)
    [print(x) for x in res12]

    print("\nЗадание Б3")
    res_13 = sortingB3(many_to_many)
    for k, v in res_13.items():
        print(k, v)


if __name__ == "__main__":
    main()