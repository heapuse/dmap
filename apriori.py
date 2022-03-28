from collections import defaultdict

data = [["bread", "jam", "nuts"], 
        ["bread", "coffee", "jam"],
        ["bread", "eggs", "jam"], 
        ["nuts", "coffee", "jam", "milk"],
        ["nuts", "coffee", "jam", "milk"]]

class Apriori:
  def __init__(self, transactions, minimum_support, minimum_confidence):
    self.minimum_support = minimum_support
    self.minimum_confidence = minimum_confidence
    self.transactions = transactions
    self.items = list()
    self.freq = list()
    self.calc_freq()

  def calc_freq(self):
    item_freq = defaultdict(lambda: 0)
    for transaction in self.transactions:
      for item in transaction:
        item_freq[item] += 1
    
    for key, value in item_freq.items():
      self.items.append([key])
      self.freq.append(value)

  def find_freq(self, itemset):
    cnt = 0
    for transaction in self.transactions:
      if len([i for i in itemset if i not in transaction]) == 0:
        cnt += 1

    return cnt

  def join(self, itemset):
    n_itemset = []
    l = len(itemset[0])
    for idx, item in enumerate(itemset[:-1]):
      strt = item[0: l-1]
      for it in itemset[idx+1:]:
        strt_ = it[0: l-1]
        if strt == strt_:
          n_itemset.append(item + [it[-1]])
        else:
          break
    
    return n_itemset

  def c_handler(self, itemset):
    c_items = self.join(itemset)
    c_freq = [self.find_freq(itset) for itset in c_items]

    return [c_items, c_freq]

  def l_handler(self, itemset, freq):
    l_items = [i for idx, i in enumerate(itemset) if freq[idx] >= self.minimum_support]
    l_freq = [i for i in freq if i >= self.minimum_support]

    return l_items, l_freq
  
  def calc_confidence(self, items, freq):
    for itemset, freq_ in zip(items, freq):
      for it in itemset:
        its = [z for z in itemset if z != it]
        
        conf_its_it = freq_ / self.find_freq([it])
        conf_it_its = freq_ / self.find_freq(its)

        if(conf_it_its >= self.minimum_confidence): 
          print(f'P({its}/{it}) = {conf_it_its}')

        if(conf_its_it >= self.minimum_confidence): 
          print(f'P({it}/{its}) = {conf_its_it}')

  def run_algo(self):
    init_items, init_freq = self.items, self.freq
  
    items, freq = self.l_handler(init_items, init_freq)

    while(True):
      if(len(items) == 0): break
      
      init_items, init_freq = items.copy(), freq.copy()
      items, freq = self.l_handler(*self.c_handler(items))

    self.calc_confidence(init_items, init_freq)
    

    
apr = Apriori(data, 2, 0)
apr.run_algo()

  
    
  
