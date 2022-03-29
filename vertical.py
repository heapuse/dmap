from collections import defaultdict
from email.policy import default
import enum

data = [["bread", "jam", "nuts"], 
        ["bread", "coffee", "jam"],
        ["bread", "eggs", "jam"], 
        ["nuts", "coffee", "jam", "milk"],
        ["nuts", "coffee", "jam", "milk"]]

def intersection(list1, list2):
  inter = []
  for value in list1:
    if value in list2:
      inter.append(value)
  return inter
    

class Apriori_Vertical:
  def __init__(self, transactions, minimum_support, minimum_confidence):
    self.data = transactions
    self.minimum_support = minimum_support
    self.minimum_confidence = minimum_confidence
    self.freq_transaction = []
    self.transactions = []
    self.items = []

  def find_unique(self):
    du = defaultdict(list)
    unique_items = []
    item_transaction = []

    for index, transaction in enumerate(self.data):
      for item in transaction:
        du[item].append(index)
    
    for key, val in dict(du).items():
      
      unique_items.append([key])
      item_transaction.append(val)

    self.items = unique_items
    self.transactions = item_transaction
  
  def find_freq(self, itemset):
    cnt = 0
    for transaction in self.data:
      if len([i for i in itemset if i not in transaction]) == 0:
        cnt += 1

    return cnt

  def join(self, itemset, freq_transaction):
    n_itemset = []
    n_freq = []

    l = len(itemset[0])
    for idx, item in enumerate(itemset[:-1]):
      strt = item[0: l-1]
      for index, it in enumerate(itemset[idx+1:]):
        strt_ = it[0: l-1]
        if strt == strt_:
          n_itemset.append(item + [it[-1]])
          n_freq.append(intersection(freq_transaction[idx], freq_transaction[index]))
        else:
          break
    
    return n_itemset, n_freq

  def c_handler(self, itemset, freq_transactions):
    return self.join(itemset, freq_transactions)
    

  def l_handler(self, itemset, freq_transactions):
    l_items = []
    l_freq = []
    
    for idx, i in enumerate(itemset):
      if len(freq_transactions[idx]) >= self.minimum_support:
        l_items.append(i)
        l_freq.append(freq_transactions[idx])
    
    return l_items, l_freq
  
  def calc_confidence(self, items, freq):
    for itemset, freq_ in zip(items, freq):
      for it in itemset:
        its = [z for z in itemset if z != it]
        
        conf_its_it = len(freq_) / self.find_freq([it])
        conf_it_its = len(freq_) / self.find_freq(its)

        if(conf_it_its >= self.minimum_confidence): 
          print(f'C({its}/{it}) = {conf_it_its}')

        if(conf_its_it >= self.minimum_confidence): 
          print(f'C({it}/{its}) = {conf_its_it}')

  def run_algo(self):
    apr.find_unique()

    init_items, init_freq = self.items, self.transactions
    items, freq = self.l_handler(init_items, init_freq)
    while(True):
      if(len(items) == 0): break
      init_items, init_freq = items.copy(), freq.copy()
      #print(init_items, init_freq)
      items, freq = self.l_handler(*self.c_handler(init_items, init_freq))

    self.calc_confidence(init_items, init_freq)
    
    print(f'Frequent item sets: {init_items}, {init_freq}')
    
apr = Apriori_Vertical(data, 2, 1)
apr.run_algo()
