# User Input


## New Element



```html
<input type="color"/>
<input type="datetime"/>
<input type="datetime-local"/>

<!-- 手机上会不同 -->

<input type="email"/>
<input type="url"/>
<input type="month"/>
<input type="number"/>
<input type="range"/>
<input type="week"/>
<input type="time"/>
<input type="search"/>
```

## Native Validation
Never trust user input

```html
<input type="text" value="" required/>
<input type="text" value="1234" pattern="/^[A-Z]+$/"/>
<input type="text" value="1234" maxlength="3"/>
<input type="range" value="0" min="3" max="9"/>

<input type="range" min="5" max="20" step="5" value="8"/>
```