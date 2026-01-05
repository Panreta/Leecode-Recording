
```markdown
From: insuranceCompany@ic.com
To: [[email]]
Subject: Insurance company – information about recent data breach
Dear [[first_name]] [[last_name]],
As you may have heard or read, last month we learned that criminals forced their way into our systems, 
and stole information about our customers. Late last week, as part of our ongoing investigation, 
we learned that the taken information includes names, mailing addresses, phone numbers or email addresses.
...
```
![[Pasted image 20251027093140.png]]



# 1. Want am I doing:
Input: 
$$f(templete,customer-info)=email,letter$$


Position + Customers
Position is Arguments, Customers are the words in CSV

1. Verify if the input is legal.
2. Generate the email and letter

input: 


eg:

```java
java Insurance.Main --csv-file data.csv --email --email-template email.txt --output-dir output/
```

parse to:

```java
args = ["--csv-file", "data.csv", "--email", "--email-template", "email.txt", "--output-dir", "output/"]
```

# 2.Verify:

[ArgumentParser](D:\MyUniversity\N.U\M1\P.D.P\hw.code\A3\Assignment3\src\main\java\Insurance\ArgumentParser.java)   
Generate the parse based on the structural data.


[ArgumentValidator](D:\MyUniversity\N.U\M1\P.D.P\hw.code\A3\Assignment3\src\main\java\Insurance\ArgumentValidator.java)：

1. validateRequiredArguments： CSV + Dir
2. validateEmailOptions,validateEmailOptions: Diversion, email or letter(seperate OCP)
3. validateOutputTypeRequested: should I generate email or letter


# 3. Generate the emails and letters
1. [CSVParser](file:///D:/MyUniversity/N.U/M1/P.D.P/hw.code/A3/Assignment3/src/main/java/Insurance/CSVParser.java): read header and use this to build , inline there is also a method to split.
2. [TemplateProcessor](D:\MyUniversity\N.U\M1\P.D.P\hw.code\A3\Assignment3\src\main\java\Insurance\TemplateProcessor.java):
3. [FileGenerator](D:\MyUniversity\N.U\M1\P.D.P\hw.code\A3\Assignment3\src\main\java\Insurance\FileGenerator.java):


TemplateProcessor:
```java
private static final Pattern PLACEHOLDER_PATTERN = Pattern.compile("\\[\\[(\\w+)\\]\\]");
```
match the pattern like \[\[words here]]   



```markdown
┌─────────────────────────────────────────────────────────────────┐
│                    Parse #1: Arguments                          │
├─────────────────────────────────────────────────────────────────┤
│ Input:  Command-line text                                       │
│         "--csv-file data.csv --email --email-template email.txt"│
│         ↓                                                        │
│ Process: ArgumentParser.parse()                                 │
│         ↓                                                        │
│ Output: ArgumentParser object                                   │
│         {                                                        │
│           csvFilePath: "data.csv",                              │
│           generateEmail: true,                                  │
│           emailTemplatePath: "email.txt"                        │
│         }                                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Parse #2: CSV Data                           │
├─────────────────────────────────────────────────────────────────┤
│ Input:  CSV file content (from disk)                            │
│         "first_name","last_name","email"                        │
│         "John","Doe","john@test.com"                            │
│         "Jane","Smith","jane@test.com"                          │
│         ↓                                                        │
│ Process: CSVParser.parseCSV()                                   │
│         ↓                                                        │
│ Output: List<Customer>                                          │
│         [                                                        │
│           Customer{first_name:"John", last_name:"Doe", ...},    │
│           Customer{first_name:"Jane", last_name:"Smith", ...}   │
│         ]                                                        │
└─────────────────────────────────────────────────────────────────┘
```


