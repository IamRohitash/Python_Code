name,company,salary='Rohitash Yadav','Microsoft',45000.0
print('hello {} ,I think youn are job in {} company and your salary is {}'.format(name,company,salary))
print('hello {0} ,I think youn are job in {1} company and your salary is {2}'.format(name,company,salary))
print('hello {a} ,I think youn are job in {b} company and your salary is {c}'.format(a=name,b=company,c=salary))
print('hello {:s} ,I think youn are job in {:s} company and your salary is {:.2f}'.format(name,company,salary))
print('hello %s ,I think youn are job in %s company and your salary is %.2f'% (name,company,salary))