# atomic-nodebox-test
Test for atomic webdevelopment ( Nodejs integration with NodeBox and Python )

###Description:
I wrote two python blocks to parse the html code and replace the values:
####Block A - Replace all characters ~ , and put values in the same order
values: Ferrari, car, red
template:
```
<span>
      <h1> ~ </h1>
     <p class="type"> ~ </p>
     <p class="color"> ~ </p>
</span>
```
Result:
```
<span>
      <h1> Ferrari </h1>
     <p class="type"> car </p>
     <p class="color"> red </p>
</span>
```
####Block B - Repeat a structure for each item
values; Batman, Superman, Spiderman
structure:
```
<li class="superhero"> ~ </li>
```

result:
```
<li class="superhero"> Batman </li>
<li class="superhero"> Superman </li>
<li class="superhero"> Spiderman </li>
```
There is also the posibility to nest both Blocks each other

###Node.js and NodeBox3:

Use Gulp tasks with BrowserSync to refresh the browser when files changes.
In Nodebox3, I save the result of all html codes in an index.html.
At this moment, gulp run the task to compile scss, an other tasks, and refresh the Browser

Browser <- Gulp <- files changes <.- NodeBox3 <- Content
