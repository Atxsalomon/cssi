Juan = {'name':'Juan',
        'age':17,
        'pets':'PerroGato',
        'haircolor':'dark brown',}

# Jesus = dict('Jesus')
# Jesus['beard'] = True
# Jesus['name'] = 'Jesus'
# Jesus['pets'] = False
# Jesus['Hair color'] = 'dark brown'

print Juan
#print Jesus

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True

    def eat(self, food):
        print ('eating noises {food}'.format(food=food))
    def lightningWhip(self, do_it_to_em):
        print ('*Raul doing the lightning whip* stand still {do_it_to_em}'.format(do_it_to_em=do_it_to_em))
Juan = Person(name='Juan',age=17)
print(Juan.name)
print('juan is hungry: {h}'.format(h=Juan.hungry))
#Juan.hungry = Fals
Juan.eat('BEEZ_CHURGERS')
Juan.lightningWhip('Wana see it again')
