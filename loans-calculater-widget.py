import ipywidgets as widgets
from IPython.display import display
def loans_calculater(): 
    loan=float(input('How much is the loan '))
    intrest=input('The intrest: ')
    intrest=float(intrest.replace('%',''))
    intrest=intrest/100
    n=12
    t=int(input('how many years:'))
    mp=(loan*(intrest/n))/(1-(1+(intrest/n))**(-n*t))
    display(f'{mp} JD in month')
widgets.interact(loans_calculater);
def g(l,i,t):
    i=i/100
    mp=(l*(i/12))/(1-((1+(i/12))**(-12*t)))
    display(f'{mp} JD per month')
widgets.interact(g,l=widgets.IntSlider(description='Loan(JD)',min=1500,max=50000,step=500,value=15000),i=widgets.FloatSlider(description='fixedIntrest % ',min=2.5,max=15,step=0.5,value=5),t=widgets.IntSlider(description='Duration(Y)',min=1,max=30,step=1,value=10));
w=widgets.interactive(g,l=widgets.IntSlider(description='Loan',min=1500,max=50000,step=500,value=15000),i=widgets.FloatSlider(description='fixedIntrest',min=0.025,max=0.12,step=0.025,value=0.075),t=widgets.IntSlider(description='ٌRepayment Period',min=1,max=30,step=1,value=10))
w.layout.margin='auto'
w