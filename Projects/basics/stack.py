def pust_element(NLIST):
    l = [ [a[0],a[1]] for a in NLIST if a[0] == 'India' and a[2] <= 35000]
    return l

a = pust_element([
    ['India', 'Delhi', 30000],
    ['India', 'Mumbai', 40000],
    ['USA', 'New York', 32000],
    ['India', 'Jaipur', 25000],
    ['India', 'Chennai', 35000],
    ['Japan', 'Tokyo', 10000],
    ['India', 'Kolkata', 36000],
    ['India', 'Hyderabad', 34000]
]
)
print(a)

