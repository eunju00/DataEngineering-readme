#!/usr/bin/env python
# coding: utf-8

# In[6]:


hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

total_revenue = 0

for price in prices:
  total_price += price
  

average_price = total_price / len(prices)
print("Average price is " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

average_daily_revenue = total_revenue / 7
print("Average daily revenue is " + str(average_daily_revenue))

#print(range(0, (len(hairstyles) - 1)))
cuts_under_30 = [hairstyles[i] for i in range(0, (len(hairstyles) - 1)) if new_prices[i] < 30]

print(cuts_under_30)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




