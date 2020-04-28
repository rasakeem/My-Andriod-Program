Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>>  FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TextView testvalue = findViewById(R.id.text_value);
                String stringValue = textValue.getText().tostring();
                int originalValue = Integer.parseInt(stringValue);
                int newValue = Newwork.doublethevalue(originalValue);
                textValue.setText(Integer.toString(newValue));

                Snackbar.make(view, "changeValue"+ orginalValue + "to" + newValue,Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }
