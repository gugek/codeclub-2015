import datetime

time_string = "Wed, 02 Oct 2002 08:00:00 EST"

my_date = datetime.datetime(2015, 7, 9)
print(my_date)
print(type(my_date))

add_days = datetime.timedelta(hours=-1000)

new_date = my_date + add_days

print(new_date)

if new_date > my_date:
    print(True)
else:
    print(False)

a = [my_date, new_date, (my_date - datetime.timedelta(weeks=5))]
print(len(a))

print("Unsorted?")
for dt in a:
    print(dt)
print("Sorted?")
a.sort(reverse=True)  # sorting the list in place
for dt in a:
    print(dt)

def foo(day_cutoff=10):  # one parameter for day_cutoff with a default value
    today = datetime.datetime.today()
    cutoff = today - datetime.timedelta(days=day_cutoff)
    a = []
    for item in feed:
        if item.date > cutoff:
            item
            # put into keep
    # figure out how to sort a...

    # a should be descending date-time order sort

foo()
foo(20)