import pandas as pd
from calculator import Calculator

cal = Calculator(3,1)

results =[]

for i in range(1,11):
    cal.b=i
    results.append(
        {
            'Values':f"3*{i}",
            'Results':cal.do_product()
         
         }
    )

df = pd.DataFrame(results)

print(df)