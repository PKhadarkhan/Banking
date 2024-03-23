import pickle
pickle_off=open("accounts.pkl","rb")
emp=pickle.load(pickle_off)
print(emp)
