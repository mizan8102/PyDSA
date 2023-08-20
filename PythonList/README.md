<ul>
<li> <h3><b> Introduction to List </b> </h3> </li>

<p>The list is a data structuring method that allows storing the integers or the characters in an order indexed by starting from 0. List operations are the operations that can be performed on the data in the list data structure. A few of the basic list operations used in Python programming are extend(), insert(), append(), remove(), pop(), slice, reverse(), min() & max(), concatenate(), count(), multiply(), sort(), index(), clear(), etc.</p>

<li><h3> <b> Key Highlights</b></h3></li>

<ul>
<li>The Python List is one of the built-in data types of Python and the most flexible one. These are involved in the storage of the collection of data sets.</li>
<li>The elements of a list are in a defined order, and you can modify these elements. Either add, remove, or change the elements in the list.</li>
<li>It is easy to create the Python list; add some elements in square brackets, separating each element by comma and assigning it to a variable.</li>
<li>Python Lists allow you to perform various functions apart from simple operations like adding or deleting. You can remove any element irrespective of the position, reverse the order of the list, print the results in a specific sequence, and sort or even empty the elements in the list.</li>
</ul>

<li><h3><b>List Operations in Python</b></h3></li>
Some of the most widely used list operations in Python include the following:

<ol>
<li> <Strong> append(): </strong>
<p>The append() method adds elements at the end of the list. This method can only add a single element at a time. You can use the append() method inside a loop to add multiple elements.<p></li>

<li><Strong>extend()</Strong> <p>
The extend() method adds more than one element at the end of the list. Although it can add more than one element, unlike append(), it adds them at the end of the list like append().</p></li>

<li>
<Strong>insert()</Strong>

<p> 
The insert() method can add an element at a given position in the list. Thus, unlike append(), it can add elements at any position, but like append(), it can add only one element at a time. This method takes two arguments. The first argument specifies the position, and the second argument specifies the element to be inserted.
</p>
</li>

<li>
<Strong>
 remove()
</Strong>

<p>
The remove() method removes an element from the list. Only the first occurrence of the same element is removed in the case of multiple occurrences.
</p>

</li>

<li>
<Strong>
sort()
</Strong>

<p>
The sort method sorts the list in ascending order. You can only perform this operation on homogeneous lists, which means lists with similar elements.
</p>
<h5>
<b>Example code</b>
</h5>

```
yourList = [4, 2, 6, 5, 0, 1]
yourList.sort()
print(yourList)
```

</li>
<li>
<Strong>
pop()
</Strong>

<p>
The method pop() can remove an element from any position in the list. The parameter supplied to this method is the element index to be removed.
</p>
<h5><b>Example Code</b></h5>
<pre>
myList = [1, 2, 3, 'EduCBA', 'makes learning fun!']
myList.pop(3)
print(myList)
</pre>

</li>
<li>
<Strong>
len()
</Strong>

<p>
The len() method returns the length of the list, i.e., the number of elements in the list.
</p>

<h5><b>Example Code</b></h5></br>
<pre>
myList = [1, 2, 3, 'EduCBA', 'makes learning fun!']
print(len(myList))
</pre>
</li>
</ol>
</ul>
