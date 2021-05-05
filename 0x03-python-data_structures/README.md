<p align="center"><img src='https://img.icons8.com/nolan/452/python.png' alt='Banner' width=10%></p>

# 0x03. Python - Data Structures: Lists, Tuples

### List
<p>
Lists are used to group values, they are written in square brackets and data is separated by commas (,).

* Types:
* __list.append(x)__ 
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

* __list.extend(L)__
Extend the list by appending all the items in the given list. Equivalent to a[len(a):] = L.

* __list.insert(i, x)__
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)__
Remove the first item from the list whose value is x. It is an error if there is no such item.

* __list.pop([i])__
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

* __list.clear()__
Remove all items from the list. Equivalent to del a[:].

* __list.index(x)__
Return the index in the list of the first item whose value is x. It is an error if there is no such item.

* __list.count(x)__
Return the number of times x appears in the list.

* __list.sort()__
Sort the items of the list in place.

* __list.reverse()__
Reverse the elements of the list in place.

* __list.copy()__
Return a shallow copy of the list. Equivalent to a[:].
* 
<p>

In this repo, you will find the following topics:

* __0. Print a list of integers__
* __1. Secure access to an element in a list__
* __2. Replace element__
* __3. Print a list of integers... in reverse!__
* __4. Replace in a copy__
* __5. Can you C me now?__
* __6. Lists of lists = Matrix__
* __7. Tuples addition__
* __8. More returns!__
* __9. Find the max__
* __10. Only by 2__
* __11. Delete at__
* __12. Switch__

### Authors :black_nib:
* __Maria Fernanda Lopez__

#### Software Academy 👨‍💻

<p aling="center">
<a href="https://www.holbertonschool.com" target="_blank">
<img src="http://www.holbertonschool.com/holberton-logo.png" alt="Holberton School"  /></a>
</p>


<p>resource:
https://docs.python.org/3.4/tutorial/datastructures.html <p>