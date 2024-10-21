# Form Attributes

HTML form attributes define the behaviors and properties of a form element.

## Example input form with attributes declared

```html
    <input    
        id="email" type="email" name="email" maxlength="32" required  
        class="email input_field input_field_email"  
        pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2, 4}$"  
        placeholder="Email address: you@address.com.au"  
    >  
```

```html
    <input 
        id="password" type="text" name="password" maxlength="64" required  
        class="password input__field input_field_password"  
        pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*_=+-]).{8,16}$"  
        placeholder="Enter password"  
    >  
```

## Pattern Attribute

```html
    <input pattern="">
```

The pattern attribute specifies a regular expression the form control's value should match. Read more about [form patterns here](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern).

## Placeholder  Attribute

```html
    <input placeholder="">
```

Places guiding text in the input field to help the user know what data is expected. This is a feature of a User Interface called 'type hints, ' which improves the user experience when completing the form.

## Maxlength Attributes

```html
    <input maxlength="">
```

Maxlength sets the length a characters a user can input, the attribute helps secure against long strings containing scripts being entered.
