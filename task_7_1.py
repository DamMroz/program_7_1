import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


freq = 12
rate_apartment = 0.05
rate_bank_deposit=0.12
years = 5
pv_apartment = 120000
rate_apartment /= freq
rate_bank_deposit /= freq 
nper = years * freq


apartment_value=np.around(npf.fv(rate_apartment, years*freq, 0.0, -120000),2)
#Ile będzie wynosiła orientacyjna cena mieszkania za 5 lat?
print(f"Mieszkanie będzie warte {apartment_value} zł")


apartment_monthly_value=np.around(npf.fv(rate_apartment, 
                                  np.arange(1,nper+1,dtype=int), 0.0, -pv_apartment),2)


monthly_investment=0
investment_value=0


while investment_value < apartment_value:
    monthly_investment=monthly_investment+0.01
    investment_value=npf.fv(rate_bank_deposit, years*freq, -monthly_investment, 
                            -monthly_investment)-monthly_investment
    
    
monthly_investment=np.around(monthly_investment,2)
investment_monthly_value=npf.fv(rate_bank_deposit, np.arange(1,nper+1,dtype=int), 
                            -monthly_investment, -monthly_investment)-monthly_investment
#Ile musisz wpłacać do banku każdego miesiąca, aby przy 
#przedstawionej ofercie uzbierać na mieszkanie w ciągu 5 lat?
print(f"Lokata miesięczna powinna wynośić {monthly_investment} zł")


figure(dpi=300)
plt.plot(apartment_monthly_value,label='Mieszkanie')
plt.plot(investment_monthly_value,label='Lokata')
plt.legend()
plt.xlabel('Liczba miesięcy')
plt.ylabel('Wartość')
plt.savefig('value.png',bbox_inches='tight')