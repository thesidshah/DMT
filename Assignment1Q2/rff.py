import pandas as pd
'''
There's an entry where the values are: '86 86' because of which there are errors, need to remove it.
'''

df = pd.read_csv('kosarak.dat',
            header=None, sep='\s\s+|,', engine='python') 
user_click = {}
user_count = 1
attributes = set()
for line in df[0]:
  vals = set(map(int,line.split(" ")))
  user_click[user_count] = sorted(vals)
  user_count += 1
  attributes.update(vals)

with open("./arff_files/test_v1.arff", "w") as f:
  f.write('@RELATION user_clicks_for_pages\n')
  f.write('@ATTRIBUTE page_0 {0,1}\n')
  for page_id in attributes:
    f.write('@ATTRIBUTE page_%d {0,1}\n' % page_id)
  f.write('@DATA\n')
  for user in user_click:
    f.write('{')
    vals = ''.join("%d 1," % i for i in user_click[user])
    f.write(vals[:-1])
    f.write('}\n')

  f.close()