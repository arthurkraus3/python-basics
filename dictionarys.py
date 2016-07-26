>>> abc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> abc {}
  File "<stdin>", line 1
    abc {}
        ^
SyntaxError: invalid syntax
>>> tree = "it's a plant"
>>> tree
"it's a plant"
>>> abc['tree'] = "it's a plant"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> abc []
  File "<stdin>", line 1
    abc []
         ^
SyntaxError: invalid syntax
>>> abc[]
  File "<stdin>", line 1
    abc[]
        ^
SyntaxError: invalid syntax
>>> abc = {}
>>> abc
{}
>>> tree = "its a plant"
>>> abc['tree'] = "it's a tree"
>>> abc['new_key']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'new_key'
>>> abc['new_key']= "this is the value"
>>> abc
{'new_key': 'this is the value', 'tree': "it's a tree"}
>>> abc['new_key']
'this is the value'
>>> abc["tree"]
"it's a tree"
>>> dict = {"tom":"he is a person", "age":25, "location":"newport beach"}
>>> dict["tom"]
'he is a person'
>>> dict["age"]
25
>>> dict["age"]*100
2500
>>> 