# Templated Increment

Suppose you have a block of code wherein you want to substitute every occurance of a marker
with an incrementing number and want to display the result of the concatenation.
That's where you would use templated increment.

## Example For Numeric Templated Increment

I generated a property in Visual Studio (type "Prop" and hit Tab twice) for the first note 
text field and want to have it replicated for the remaining note text fields (there are 10 
of them). I don't want to include Note1Text because it's already in my code so the code 
generation can start from Note2Text.

This is my template file (sample_tpl.txt)
```vbnet
    Private mNote%(n)sText As String
    Public Property Note%(n)sText() As String
        Get
            Return mNote%(n)sText
        End Get
        Set(ByVal value As String
            mNote%(n)sText = value
        End Set
    End Property
```
This is my command line
```
    python numericRunme.py sample_tpl.txt 10 2 > out1.vb
```

## Example for List Templated Increment

I have a coupple of XPath strings defined in a couple of variables. Having to type them all
over again to reference them is a repetitive task. The list templated increment will generate
the needed statements based on the list and a template.

This is my template file (sample_tpl2.txt)
```vbnet
    Dim %(tag)s_value As String = nav.SelectSingleNode(%(tag)s_xpath, nsmgr).Value
```
This is my list file (listvals2.txt)
```
    Name
    Age
    City
    Country
```
This is my command line
```
    python listRunme.py sample_tpl2.txt listvals2.txt > out2.vb
```
