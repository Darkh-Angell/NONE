def Expand(expand=''):
    Expand_amount = 10
    if expand == True:
        expand_option = input('Expansion packs:\n'
                            '1 - Expand +10\n'
                            '2 - Expand +20\n'
                            '3 - Expand +30\n'
                            '>>> ')
    
        while expand_option not in ['1','2','3']:
            raise ValueError ('Invalid Choice')
            expand_option = input('Expansion packs:\n'
                                '1 - Expand +10\n'
                                '2 - Expand +20\n'
                                '3 - Expand +30\n'
                                '>>> ')
        if expand_option == '1':
            Expand_amount += 10
        elif expand_option == '2':
            Expand_amount += 20
        elif expand_option == '3':
            Expand_amount += 30
  
    elif expand == False:
        Expand_amount = Expand_amount
  
    return Expand_amount     

class Inventory:
    def __init__(self, expansion):
        self.slots = []
        self.expansion = expansion
    def checked_inventory(self):
        while len(self.slots) > self.expansion-1:
            raise OverflowError('Number of items exceeds inventory amount ({}/{})\n'
                                'Delete {} items'.format(len(self.slots),self.expansion, (len(self.slots) - self.expansion)+1))

            break
        else:
            pass
    def location(self, item):
        self.checked_inventory()
        if type(item) == list:
            for items in item:
                if len(self.slots):
                    position = input('Where do you want to add {0}?\n'
                                'Press ENTER to add {0} to the end of your shopping list.\n'
                                '>>> '.format(items))
                else:
                    position = 0
                try:
                    position = abs(int(position))
                except ValueError:
                    position = None
                if position is not None:
                    self.slots.insert(position-1, items)
                else:
                    self.slots.append(items)
        else:
            if len(self.slots):
                position = input('Where do you want to add {0}?\n'
                            'Press ENTER to add {0} to the end of your shopping list.\n'
                            '>>> '.format(item))
            else:
                position = 0
        try:
            position = abs(int(position))
        except ValueError:
            position = None
        if position is not None:
            self.slots.insert(position-1, item)
        else:
            self.slots.append(item)

    def add(self, item):
        if type(item) == list:
          for items in item:
            self.checked_inventory()
            self.slots.append(items)
        else:
          self.checked_inventory()
          self.slots.append(item)
    
    def Items(self):
        n = 1
        for item in self.slots:
          print('{} - {}'.format(n, item))
          n+=1
    
    def __len__(self):
        return len(self.slots)
    
    def delete(self, item):
        if type(item) == list:
            for items in item:
                try:
                    while items in self.slots:
                        self.slots.remove(items)
                    else:
                        pass
                except ValueError:
                    raise ValueError('{} not in Inventory'.format(items))
                else:
                    pass
        else:
            try:
                while items in self.slots:
                    self.slots.remove(items)
            except ValueError:
                raise ValueError('{} not in Inventory'.format(items))
            else:
                pass
    
    def sort(self):
        self.checked_inventory()
        slots_str = []
        slots_int = []
        for items in self.slots:
            if type(items) == str:
                slots_str.append(items)
            else:
                slots_int.append(items)
        slots_str.sort()
        slots_int.sort()
        self.slots = slots_int + slots_str
        

