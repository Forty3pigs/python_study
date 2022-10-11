class Person:
    def __init__(self, name, sname, lname, phones: dict):
        self.name = name
        self.sname = sname
        self.lname = lname
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return self.lname + ' ' + self.name + ' ' + self.sname

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.sname}! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, cname, ctype, phones: dict, *args: Person):
        self.cname = cname
        self.ctype = ctype
        self.phones = phones
        self.persons = args

    def get_phone(self):
        if self.phones.get('contact'):
            return self.phones.get('contact')
        else:
            for p in self.persons:
                if p.get_work_phone():
                    return p.get_work_phone()

    def get_name(self):
        return self.cname

    def get_sms_text(self):
        return f'Для компании {self.cname} есть супер предложение!' \
               f' Примите участие в нашем беспроигрышном конкурсе для {self.ctype}'


def send_sms(*receivers):
    for receiver in receivers:
        if receiver.get_phone():
            print(f'Отправлено СМС на номер {receiver.get_phone()} с текстом {receiver.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту {receiver.get_name()}')


p1 = Person('Ivan', 'Ivanovich', 'Ivanov', {"private": 123, "work": 456})
p2 = Person('Igor', 'Petrovich', 'Petrov', {"private": 789})
p3 = Person('Igor', 'Petrovich', 'Sidorov', {"work": 789})
p4 = Person('John', 'Unknown', 'Doe', {})
c1 = Company('Bell', 'OOO', {"contact": 111}, p3, p4)
c2 = Company('Cell', 'AO', {"non-contact": 222}, p2, p3)
c3 = Company('Dell', 'Ltd.', {"non-contact": 333}, p2, p4)

pp1 = Person('Степан', "Петрович", "Джобсов", {"private": 555})
pp2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
pp3 = Person("Семен", "Робертович", "Возняцкий", {'work': 789})
pp4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
cc1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, pp1, pp3)
cc2 = Company("ПластОкно", "АО", {"non-contact": 222}, pp2)
cc3 = Company("Пингвинья ферма", "Ltd", {"non-contact": 333}, pp4)

send_sms(p1, p2, p3, p4, c1, c2, c3)
print()
send_sms(pp1, pp2, pp3, pp4, cc1, cc2, cc3)


