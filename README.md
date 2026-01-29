<h1>python-list-from-scratch</h1>

<p>
A custom implementation of Python’s built-in <code>list</code> using a
<b>dynamic array</b> created with <code>ctypes</code>.
This project is built to understand how Python lists work internally.
</p>

<hr>

<h2>📌 About the Project</h2>

<p>
Python lists are dynamic arrays internally. In this project, instead of using
Python’s built-in <code>list</code>, we create our own list class called
<b>MeraList</b> and manually handle memory allocation, resizing, and element
operations using <code>ctypes</code>.
</p>

<p>
This project is focused on learning <b>data structures</b>, <b>memory
management</b>, and <b>low-level behavior</b> of Python lists.
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>Dynamic array implementation using <code>ctypes</code></li>
  <li>Automatic resizing of array</li>
  <li>Index-based element access</li>
  <li>Custom string representation</li>
  <li>Length support using <code>len()</code></li>
</ul>

<hr>

<h2>🧠 Implemented Methods</h2>

<ul>
  <li><code>__init__()</code> – initialize the list</li>
  <li><code>__make_array()</code> – create low-level array using ctypes</li>
  <li><code>__len__()</code> – return number of elements</li>
  <li><code>append()</code> – add element at the end</li>
  <li><code>__resize()</code> – resize array when capacity is full</li>
  <li><code>__getitem__()</code> – access elements using index</li>
  <li><code>__delitem__()</code> – delete element by index</li>
  <li><code>pop()</code> – remove and return last element</li>
  <li><code>insert()</code> – insert element at a given index</li>
  <li><code>remove()</code> – remove first occurrence of an element</li>
  <li><code>find()</code> – find index of an element</li>
  <li><code>clear()</code> – remove all elements</li>
  <li><code>__str__()</code> – return string representation</li>
</ul>

<hr>

<h2>🛠️ Requirements</h2>

<ul>
  <li>Python 3.x</li>
</ul>

<p>
No external libraries are required. Only Python’s built-in <code>ctypes</code>
module is used.
</p>

<hr>

<h2>▶️ How to Run</h2>

<pre><code>
git clone https://github.com/krishnakantnagina/python-list-from-scratch.git
cd python-list-from-scratch
python merilist.py
</code></pre>

<hr>

<h2>🧪 Example Usage</h2>

<pre><code>
from merilist import MeraList

arr = MeraList()
arr.append(10)
arr.append(20)
arr.insert(1, 15)

print(arr)        # [10, 15, 20]
print(len(arr))   # 3

arr.pop()
arr.remove(10)
</code></pre>

<hr>

<h2>🎯 Learning Outcome</h2>

<ul>
  <li>Understanding dynamic arrays</li>
  <li>How Python manages list resizing</li>
  <li>Memory allocation using ctypes</li>
  <li>Implementing list behavior manually</li>
</ul>

<hr>

<h2>👤 Author</h2>

<p>
<b>Krishnakant Nagina</b><br>
Student & Python Developer
</p>

<hr>

<h2>📄 License</h2>

<p>
This project is open source and available under the MIT License.
</p>
