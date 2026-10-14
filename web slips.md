# CDS-242-MNP – Lab on CDS-241-M Web Technology

S. Y. B. Sc. (Cyber and Digital Science) – Sem III  
Slip-wise questions with code

---

## Slip 1

**Q1.** Write a PHP program to store the details of 5 students (name, marks) in an associative array. Traverse the array and display the name of the student having maximum marks. (10 M)

```php
<?php
$students = ["Asha"=>78, "Ravi"=>91, "Neha"=>84, "Om"=>67, "Sara"=>88];
$topName = ""; $maxMarks = -1;
foreach ($students as $name => $marks) {
    if ($marks > $maxMarks) { $maxMarks = $marks; $topName = $name; }
}
echo "Top student: $topName<br>Marks: $maxMarks";
?>
```

**Q2.** Write HTML-CSS code to generate the book list / bill output (Item No, Item Name, Price in Rs. and Paise, Total Bill). Use Internal CSS. (15 M)

```html
<!DOCTYPE html>
<html><head><style>
body{font-family:Arial}
table{border-collapse:collapse;width:80%;margin:auto}
th,td{border:1px solid black;padding:10px;text-align:center}
h2{text-align:center}
</style></head><body>
<h2>List of Books</h2>
<table>
<tr><th rowspan="2">Item No</th><th rowspan="2">Item Name</th><th colspan="2">Price</th></tr>
<tr><th>Rs.</th><th>Paise</th></tr>
<tr><td>1</td><td>Programming in Python</td><td>500</td><td>50</td></tr>
<tr><td>2</td><td>Programming in Java</td><td>345</td><td>00</td></tr>
<tr><td colspan="2">Total Bill</td><td>845</td><td>50</td></tr>
</table>
</body></html>
```

---

## Slip 2

**Q1.** Write a PHP program to check whether a given number is prime or not. Use a function and a default parameter. (10 M)

```php
<?php
function isPrime($n = 2) {
    if ($n < 2) return false;
    for ($i = 2; $i * $i <= $n; $i++)
        if ($n % $i == 0) return false;
    return true;
}
$n = 29;
echo isPrime($n) ? "$n is prime" : "$n is not prime";
?>
```

**Q2.** Write a PHP program to read a file "Item.dat", which contains details of 5 different items such as Item code, Item Name, units sold and Rate. Display the Bill in tabular format. (15 M)

```php
<?php
// Item.dat format (one item per line): code|name|units|rate
// 101|Pen|5|10
// 102|Book|2|50
// 103|Pencil|10|5
// 104|Eraser|4|3
// 105|Notebook|3|40
$file = "Item.dat";
$total = 0;
if (!file_exists($file)) die("Item.dat not found");
echo "<table border='1' cellpadding='6'>";
echo "<tr><th>Code</th><th>Item</th><th>Units</th><th>Rate</th><th>Amount</th></tr>";
$lines = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
foreach ($lines as $line) {
    $v = explode("|", $line);
    if (count($v) != 4) continue;
    [$code, $name, $qty, $rate] = $v;
    $amount = (float)$qty * (float)$rate;
    $total += $amount;
    echo "<tr><td>$code</td><td>$name</td><td>$qty</td><td>$rate</td><td>$amount</td></tr>";
}
echo "<tr><th colspan='4'>Grand Total</th><th>$total</th></tr></table>";
?>
```

---

## Slip 3

**Q1.** Write a PHP program to check whether a given string is palindrome or not. (10 M)

```php
<?php
$s = "madam";
if (strtolower($s) === strtolower(strrev($s))) echo "$s is palindrome";
else echo "$s is not palindrome";
?>
```

**Q2.** Write JavaScript code using a function to generate a random number between 1 and 100. (15 M)

```html
<!DOCTYPE html>
<html><body>
<button onclick="showRandom()">Generate</button>
<p id="out"></p>
<script>
function randomNumber(){ return Math.floor(Math.random()*100)+1; }
function showRandom(){ document.getElementById("out").textContent = randomNumber(); }
</script>
</body></html>
```

---

## Slip 4

**Q1.** Write a PHP program to read the contents from a file line by line and display them on the web page. (10 M)

```php
<?php
$file = "sample.txt";
if (!file_exists($file)) die("File not found");
$fp = fopen($file, "r");
while (($line = fgets($fp)) !== false) echo htmlspecialchars($line) . "<br>";
fclose($fp);
?>
```

**Q2.** Write an HTML-CSS script to design the screen with a header ("This is a header."), a left box ("Look in the box at the right for some information."), a right box ("Here is some information.") and a footer ("This is a footer."). Use External CSS. (15 M)

```html
<!-- index.html -->
<!DOCTYPE html>
<html><head><link rel="stylesheet" href="style.css"></head>
<body>
<div class="box">
<div class="header"><h1>This is a header.</h1></div>
<div class="middle">
<div class="left">Look in the box at the right for some information.</div>
<div class="right">Here is some information.</div>
</div>
<div class="footer"><h1>This is a footer.</h1></div>
</div>
</body></html>
```

```css
/* style.css */
body{font-family:"Times New Roman",serif;margin:20px}
.box{width:700px;border:1px solid black}
.header,.footer{height:70px;padding:5px 10px;border-bottom:3px solid #999}
.footer{border-bottom:none;border-top:3px solid #999}
.middle{display:flex;height:170px}
.left{width:150px;padding:8px;font-size:14px;border-right:4px solid #999}
.right{flex:1;padding:8px;font-size:14px}
h1{margin:10px 0;font-size:28px}
```

---

## Slip 5

**Q1.** Write a PHP program to append the line "This is an appended line." to the sample.txt file without overwriting existing content. (10 M)

```php
<?php
$file = fopen("sample.txt", "a");
if (!$file) die("Unable to open file");
fwrite($file, "This is an appended line." . PHP_EOL);
fclose($file);
echo "Line appended successfully.";
?>
```

**Q2.** Write an HTML-CSS script to prepare the mark sheet of a first year student; it includes Seat No, Name, Subject names with marks, Course Name, Total Marks, Percentage etc. (Use Inline CSS) (15 M)

```html
<!DOCTYPE html>
<html><body>
<h2 style="text-align:center;color:navy">First Year Student Marksheet</h2>
<table style="border-collapse:collapse;width:80%;margin:auto" border="1" cellpadding="8">
<tr><th>Seat No</th><td>101</td><th>Name</th><td>Asha Patil</td></tr>
<tr><th colspan="2">Course Name</th><td colspan="2">B.Sc. Cyber and Digital Science</td></tr>
<tr><th>Subject</th><th>Max Marks</th><th>Marks Obtained</th><th>Result</th></tr>
<tr><td>Web Technology</td><td>100</td><td>85</td><td>Pass</td></tr>
<tr><td>Programming</td><td>100</td><td>80</td><td>Pass</td></tr>
<tr><td>Computer Science</td><td>100</td><td>90</td><td>Pass</td></tr>
<tr><th colspan="2">Total Marks</th><td colspan="2">255 / 300</td></tr>
<tr><th colspan="2">Percentage</th><td colspan="2">85%</td></tr>
</table>
</body></html>
```

---

## Slip 6

**Q1.** Write a PHP program to create two arrays of fruits and merge them into a single array. Display the merged result. (10 M)

```php
<?php
$a = ["Apple", "Mango", "Banana"];
$b = ["Orange", "Grapes", "Pineapple"];
$c = array_merge($a, $b);
foreach ($c as $fruit) echo $fruit . "<br>";
?>
```

**Q2.** Write a JavaScript program to reverse a given string using a function. Use alert() to display the output. (15 M)

```html
<script>
function reverseString(s){ return s.split("").reverse().join(""); }
let value = prompt("Enter a string:");
if (value !== null) alert("Reversed string: " + reverseString(value));
</script>
```

---

## Slip 7

**Q1.** Write a JavaScript program to display the multiplication table of a given number in tabular format. (10 M)

```html
<!DOCTYPE html>
<html><body>
<input id="num" type="number" value="5">
<button onclick="makeTable()">Show table</button>
<div id="result"></div>
<script>
function makeTable(){
    const n = Number(document.getElementById("num").value);
    let html = "<table border='1' cellpadding='5'><tr><th>Expression</th><th>Result</th></tr>";
    for (let i = 1; i <= 10; i++)
        html += `<tr><td>${n} x ${i}</td><td>${n*i}</td></tr>`;
    document.getElementById("result").innerHTML = html + "</table>";
}
</script>
</body></html>
```

**Q2.** Write a PHP program to create an associative array of students with names as keys and marks as values. Sort it by marks in descending order. (15 M)

```php
<?php
$students = ["Asha"=>78, "Ravi"=>91, "Neha"=>84, "Om"=>67, "Sara"=>88];
arsort($students);
foreach ($students as $name => $marks) echo "$name : $marks<br>";
?>
```

---

## Slip 8

**Q1.** Create an HTML-CSS page which will display names of your family members on separate lines in different sizes. State the size of each line in its text. (Use External CSS) (10 M)

```html
<!-- index.html -->
<!DOCTYPE html>
<html><head><link rel="stylesheet" href="family.css"></head>
<body>
<p class="one">Father (18px)</p>
<p class="two">Mother (22px)</p>
<p class="three">Brother (26px)</p>
<p class="four">Sister (30px)</p>
</body></html>
```

```css
/* family.css */
.one{font-size:18px}
.two{font-size:22px}
.three{font-size:26px}
.four{font-size:30px}
```

**Q2.** Write a PHP program to display the first N terms of the Fibonacci series. Use a variable function. (15 M)

```php
<?php
function fibonacci($n) {
    $a = 0; $b = 1;
    for ($i = 0; $i < $n; $i++) {
        echo $a . " ";
        [$a, $b] = [$b, $a + $b];
    }
}
$fn = "fibonacci";
$fn(10);
?>
```

---

## Slip 9

**Q1.** Write a PHP program to calculate the sum of digits of a number. Use a default parameter. (10 M)

```php
<?php
function digitSum($n = 12345) {
    $n = abs((int)$n); $sum = 0;
    while ($n > 0) { $sum += $n % 10; $n = intdiv($n, 10); }
    return $sum;
}
echo "Sum = " . digitSum(583);
?>
```

**Q2.** Write an HTML-CSS script to design an Email Registration form. Use Internal CSS. (15 M)

```html
<!DOCTYPE html>
<html><head><style>
body{font-family:Arial;background:#eef2f7}
.form{width:320px;margin:40px auto;background:white;padding:20px;border-radius:8px}
label,input{display:block;width:100%;margin:8px 0}
input{padding:8px;box-sizing:border-box}
button{background:#1769aa;color:white;padding:9px;border:0;width:100%}
</style></head><body>
<form class="form">
<h2>Email Registration</h2>
<label>Full Name</label><input type="text" required>
<label>Email</label><input type="email" required>
<label>Password</label><input type="password" required>
<label>Confirm Password</label><input type="password" required>
<button type="submit">Register</button>
</form>
</body></html>
```

---

## Slip 10

**Q1.** Write a JavaScript program to count the number of vowels in a given string. Display the result on the same web page. (10 M)

```html
<!DOCTYPE html>
<html><body>
<input id="s" type="text" placeholder="Enter string">
<button onclick="countVowels()">Count</button>
<p id="out"></p>
<script>
function countVowels(){
    const s = document.getElementById("s").value;
    const m = s.match(/[aeiou]/gi);
    document.getElementById("out").textContent = "Vowels: " + (m ? m.length : 0);
}
</script>
</body></html>
```

**Q2.** Write an HTML-CSS script to design a web page for the theory time table of first year B.Sc. CDS. (15 M)

```html
<!DOCTYPE html>
<html><head><style>
table{border-collapse:collapse;width:100%;font-family:Arial}
th,td{border:1px solid #333;padding:10px;text-align:center}
th{background:#d9eaf7}
</style></head><body>
<h2>B.Sc. CDS First Year - Theory Time Table</h2>
<table>
<tr><th>Day</th><th>9-10</th><th>10-11</th><th>11-12</th><th>12-1</th></tr>
<tr><th>Monday</th><td>Mathematics</td><td>Programming</td><td>Break</td><td>Web Technology</td></tr>
<tr><th>Tuesday</th><td>Statistics</td><td>Web Technology</td><td>Break</td><td>Programming</td></tr>
<tr><th>Wednesday</th><td>Programming</td><td>Mathematics</td><td>Break</td><td>Statistics</td></tr>
<tr><th>Thursday</th><td>Web Technology</td><td>Statistics</td><td>Break</td><td>Mathematics</td></tr>
<tr><th>Friday</th><td>Mathematics</td><td>Programming</td><td>Break</td><td>Statistics</td></tr>
</table>
</body></html>
```

---

## Slip 11

**Q1.** Write a PHP program to convert array elements into variables. (Use appropriate function) (10 M)

```php
<?php
$student = ["name"=>"Asha", "age"=>19, "course"=>"B.Sc. CDS"];
extract($student);
echo "$name<br>$age<br>$course";
?>
```

**Q2.** Write HTML-CSS code which generates the nested list output (Non flowering plants: Fern, Spore; Flowering plants: Lilly, Rose with Red Rose, Pink Rose) and displays each element of the list in different size, color and font. Use external CSS. (15 M)

```html
<!-- index.html -->
<!DOCTYPE html>
<html><head><link rel="stylesheet" href="list.css"></head>
<body>
<ul class="disc">
<li class="a">Non flowering plants
<ul class="circle">
<li class="b">Fern</li>
<li class="c">Spore</li>
</ul>
</li>
<li class="a">Flowering plants
<ul class="square">
<li class="d">Lilly</li>
<li class="e">Rose
<ol>
<li class="f">Red Rose</li>
<li class="g">Pink Rose</li>
</ol>
</li>
</ul>
</li>
</ul>
</body></html>
```

```css
/* list.css */
ul.disc{list-style-type:disc}
ul.circle{list-style-type:circle}
ul.square{list-style-type:square}
ol{list-style-type:decimal}
.a{font:20px Arial;color:blue}
.b{font:18px Georgia;color:green}
.c{font:16px Verdana;color:crimson}
.d{font:18px "Courier New";color:purple}
.e{font:20px Tahoma;color:darkorange}
.f{font:16px "Times New Roman";color:red}
.g{font:16px Verdana;color:deeppink}
```

---

## Slip 12

**Q1.** Write a PHP program to declare an integer array of 5 integers and perform the following operations: (1) calculate the sum of array elements, (2) calculate the product of array elements, (3) display only odd numbers from the array. (10 M)

```php
<?php
$a = [2, 3, 5, 6, 7];
$sum = array_sum($a);
$product = array_product($a);
echo "Sum = $sum<br>Product = $product<br>Odd numbers: ";
foreach ($a as $n) if ($n % 2 != 0) echo "$n ";
?>
```

**Q2.** Write JavaScript code to compare two strings and check if they are equal or not. (15 M)

```html
<script>
const a = prompt("Enter first string:");
const b = prompt("Enter second string:");
if (a === b) document.write("Strings are equal");
else document.write("Strings are not equal");
</script>
```

---

## Slip 13

**Q1.** Write a PHP program to sort an associative array of 5 student names in ascending and descending order. (10 M)

```php
<?php
$students = ["Neha"=>80, "Amit"=>75, "Zoya"=>90, "Kiran"=>68, "Ravi"=>85];
$asc = $students; $desc = $students;
ksort($asc); krsort($desc);
echo "Names ascending:<br>";
foreach ($asc as $n => $m) echo "$n - $m<br>";
echo "<br>Names descending:<br>";
foreach ($desc as $n => $m) echo "$n - $m<br>";
?>
```

**Q2.** Write a PHP program to accept a PAN number from a user and check the validity of the entered PAN number using a regular expression. (15 M)

```php
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $pan = strtoupper(trim($_POST["pan"] ?? ""));
    if (preg_match("/^[A-Z]{5}[0-9]{4}[A-Z]$/", $pan)) echo "Valid PAN format";
    else echo "Invalid PAN format";
}
?>
<form method="post">
PAN: <input name="pan" maxlength="10" required>
<button type="submit">Check</button>
</form>
```

---

## Slip 14

**Q1.** Write a PHP program to store names of 3 fruits in an associative array and print each name index wise. (10 M)

```php
<?php
$fruits = [0=>"Apple", 1=>"Mango", 2=>"Orange"];
foreach ($fruits as $index => $fruit) echo "$index : $fruit<br>";
?>
```

**Q2.** Write a PHP script for the following: design a form to accept two strings from the user. (a) Find whether the small string appears at the start of the large string. (b) Find the position of the small string in the large string. (15 M)

```php
<form method="post">
Large string: <input name="large" required><br>
Small string: <input name="small" required><br>
<button>Check</button>
</form>
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $large = $_POST["large"]; $small = $_POST["small"];
    $pos = strpos($large, $small);
    if ($pos === 0) echo "Small string appears at the start.<br>";
    else echo "Small string does not appear at the start.<br>";
    if ($pos === false) echo "Small string not found.";
    else echo "Position (0-based): " . $pos;
}
?>
```

---

## Slip 15

**Q1.** Write JavaScript code to check whether a given string is palindrome or not. Display the result on the same web page. (10 M)

```html
<!DOCTYPE html>
<html><body>
<input id="s" placeholder="Enter string">
<button onclick="check()">Check</button>
<p id="out"></p>
<script>
function check(){
    const s = document.getElementById("s").value.toLowerCase().replace(/[^a-z0-9]/g, "");
    const rev = s.split("").reverse().join("");
    document.getElementById("out").textContent = (s === rev) ? "Palindrome" : "Not palindrome";
}
</script>
</body></html>
```

**Q2.** Write a PHP program to store 10 numbers in an array and print only even numbers from that array. (Use appropriate function) (15 M)

```php
<?php
$numbers = [12, 7, 8, 19, 20, 31, 44, 53, 62, 75];
$even = array_filter($numbers, fn($n) => $n % 2 === 0);
echo "Even numbers: " . implode(", ", $even);
?>
```

---

## Slip 16

**Q1.** Write a PHP program to read one file and display the contents of the file with its size. (10 M)

```php
<?php
$file = "sample.txt";
if (!is_file($file)) die("File not found");
echo nl2br(htmlspecialchars(file_get_contents($file)));
echo "<br>File size: " . filesize($file) . " bytes";
?>
```

**Q2.** Write a PHP program to search an element in an associative array and display an appropriate message. (15 M)

```php
<?php
$marks = ["Asha"=>78, "Ravi"=>91, "Neha"=>84];
$key = "Ravi";
if (array_key_exists($key, $marks)) echo "$key found; marks = " . $marks[$key];
else echo "$key not found";
?>
```

---

## Slip 17

**Q1.** Write a JavaScript program to validate a pincode number. Use prompt() to take the data from the user. (10 M)

```html
<script>
const pin = prompt("Enter 6-digit Indian PIN code:");
if (pin !== null && /^[1-9][0-9]{5}$/.test(pin)) alert("Valid PIN code");
else alert("Invalid PIN code");
</script>
```

**Q2.** Write a PHP function that takes a file path as input and checks if the file exists. (15 M)

```php
<?php
function checkFile($path) {
    if (file_exists($path) && is_file($path)) return "File exists";
    return "File does not exist";
}
echo checkFile("sample.txt");
?>
```

---

## Slip 18

**Q1.** Write JavaScript code to check whether a number is an Armstrong number or not. Display the result on the same web page. (10 M)

```html
<!DOCTYPE html>
<html><body>
<input id="n" type="number">
<button onclick="checkArmstrong()">Check</button>
<p id="out"></p>
<script>
function checkArmstrong(){
    const n = Number(document.getElementById("n").value);
    const digits = String(Math.abs(n)).split("");
    const sum = digits.reduce((s, d) => s + Math.pow(Number(d), digits.length), 0);
    document.getElementById("out").textContent =
        (n >= 0 && sum === n) ? "Armstrong number" : "Not an Armstrong number";
}
</script>
</body></html>
```

**Q2.** Design an HTML form to accept a string and write a PHP script: (a) to find the length of the given string without using built-in functions, (b) a function to count the total number of vowels (a, e, i, o, u) in the string, (c) find the reverse of the given string (use built-in function). (15 M)

```php
<form method="post">
String: <input name="s" required>
<button>Submit</button>
</form>
<?php
function countVowels($s, $len) {
    $count = 0;
    for ($i = 0; $i < $len; $i++)
        if (stripos("aeiou", $s[$i]) !== false) $count++;
    return $count;
}
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $s = $_POST["s"];
    $len = 0;
    while (isset($s[$len])) $len++;
    echo "Length: $len<br>";
    echo "Vowels: " . countVowels($s, $len) . "<br>";
    echo "Reverse: " . htmlspecialchars(strrev($s));
}
?>
```

---

## Slip 19

**Q1.** Write a PHP script to check whether a given mobile number is valid or not. Use a regular expression. (10 M)

```php
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $mobile = $_POST["mobile"] ?? "";
    echo preg_match("/^[6-9][0-9]{9}$/", $mobile) ? "Valid mobile number" : "Invalid mobile number";
}
?>
<form method="post">
Mobile: <input name="mobile" maxlength="10" required>
<button>Check</button>
</form>
```

**Q2.** Write a JavaScript program to count how many times a particular element appears in an indexed array. (15 M)

```html
<script>
const arr = [2, 5, 2, 7, 2, 9, 5];
const target = Number(prompt("Enter element to count:"));
let count = 0;
for (const item of arr) if (item === target) count++;
document.write("Array: " + arr.join(", ") + "<br>" + target + " occurs " + count + " time(s).");
</script>
```

---

## Slip 20

**Q1.** Write a PHP program to display the contents from a file in reverse order. (10 M)

```php
<?php
$file = "sample.txt";
if (!is_file($file)) die("File not found");
$lines = file($file, FILE_IGNORE_NEW_LINES);
foreach (array_reverse($lines) as $line) echo htmlspecialchars($line) . "<br>";
?>
```

**Q2.** Write JavaScript code to check whether a given mobile number is valid or not. (15 M)

```html
<!DOCTYPE html>
<html><body>
<input id="mobile" maxlength="10" placeholder="10-digit mobile">
<button onclick="checkMobile()">Check</button>
<p id="out"></p>
<script>
function checkMobile(){
    const m = document.getElementById("mobile").value.trim();
    document.getElementById("out").textContent =
        /^[6-9][0-9]{9}$/.test(m) ? "Valid mobile number" : "Invalid mobile number";
}
</script>
</body></html>
```

---

## Slip 21

**Q1.** Write JavaScript code to count vowels in a string. Use alert() to display the output. (10 M)

```html
<script>
const s = prompt("Enter a string:") || "";
const m = s.match(/[aeiou]/gi);
alert("Number of vowels: " + (m ? m.length : 0));
</script>
```

**Q2.** Write a program to perform various file operations. Accept the filename from the user. (a) Display type of file. (b) Display the size of file. (c) Delete the file. (15 M)

```php
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $file = $_POST["filename"] ?? "";
    if (is_file($file)) {
        echo "File type: " . htmlspecialchars(mime_content_type($file) ?: "unknown") . "<br>";
        echo "File size: " . filesize($file) . " bytes<br>";
        if (isset($_POST["delete"])) {
            echo unlink($file) ? "File deleted." : "Unable to delete file.";
        }
    } else echo "File does not exist.";
}
?>
<form method="post">
Filename: <input name="filename" required>
<button name="show" value="1">Show details</button>
<button name="delete" value="1" onclick="return confirm('Delete this file?')">Delete file</button>
</form>
```

---

## Slip 22

**Q1.** Write a JavaScript program to count the digits in a number. Use the onMouseOver event. (10 M)

```html
<!DOCTYPE html>
<html><body>
<p id="msg" onmouseover="countDigits()">Move mouse over this text to count digits.</p>
<script>
function countDigits(){
    const value = prompt("Enter a number:");
    if (value !== null) {
        const count = (value.match(/[0-9]/g) || []).length;
        document.getElementById("msg").textContent = "Number of digits: " + count;
    }
}
</script>
</body></html>
```

**Q2.** Design an HTML form to accept a number and write a PHP script: (a) to display each digit of the number in words, (b) find the sum of all digits in that number. (15 M)

```php
<form method="post">
Number: <input name="num" pattern="[0-9]+" required>
<button>Submit</button>
</form>
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $num = $_POST["num"];
    $words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"];
    $sum = 0; $out = [];
    foreach (str_split($num) as $d) { $out[] = $words[(int)$d]; $sum += (int)$d; }
    echo "Digits in words: " . implode(" ", $out) . "<br>Sum of digits: $sum";
}
?>
```

---

## Slip 23

**Q1.** Write a PHP program to copy the content of one file into another file. (10 M)

```php
<?php
$source = "source.txt"; $destination = "destination.txt";
if (!is_file($source)) die("Source file not found");
if (copy($source, $destination)) echo "File copied successfully";
else echo "Copy failed";
?>
```

**Q2.** Write JavaScript code to check whether a given name is valid or not. (15 M)

```html
<!DOCTYPE html>
<html><body>
<input id="name" placeholder="Enter name">
<button onclick="checkName()">Validate</button>
<p id="out"></p>
<script>
function checkName(){
    const n = document.getElementById("name").value.trim();
    document.getElementById("out").textContent =
        /^[A-Za-z]+(?:[ '-][A-Za-z]+)*$/.test(n) ? "Valid name" : "Invalid name";
}
</script>
</body></html>
```

---

## Slip 24

**Q1.** Write an HTML-CSS program to create a feedback form with dropdowns, text area, checkbox, radio button, textbox and submit button. (10 M)

```html
<!DOCTYPE html>
<html><head><style>
body{font-family:Arial}
.form{max-width:420px;margin:20px auto;padding:20px;border:1px solid #aaa}
label{display:block;margin-top:10px}
input[type=text],select,textarea{width:100%;padding:7px;box-sizing:border-box}
button{margin-top:12px;padding:9px 18px;background:#1769aa;color:white;border:0}
</style></head><body>
<form class="form">
<h2>Feedback Form</h2>
<label>Name</label><input type="text" required>
<label>Category</label>
<select><option>Website</option><option>Course</option><option>Other</option></select>
<label>Rating</label>
<label><input type="radio" name="rating" value="good"> Good</label>
<label><input type="radio" name="rating" value="average"> Average</label>
<label><input type="radio" name="rating" value="poor"> Poor</label>
<label>Comments</label><textarea rows="4"></textarea>
<label><input type="checkbox"> I agree to submit this feedback</label>
<button type="submit">Submit</button>
</form>
</body></html>
```

**Q2.** Write a PHP program to check whether a given name is valid or not. Use a regular expression. (15 M)

```php
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"] ?? "");
    echo preg_match("/^[A-Za-z]+(?:[ '-][A-Za-z]+)*$/", $name) ? "Valid name" : "Invalid name";
}
?>
<form method="post">
Name: <input name="name" required>
<button>Check</button>
</form>
```

---

## Slip 25

**Q1.** Write a PHP program that deletes a specific file from the server. (10 M)

```php
<?php
$file = "sample.txt";
if (is_file($file)) {
    echo unlink($file) ? "File deleted successfully" : "Unable to delete file";
} else echo "File does not exist";
?>
```

**Q2.** Write a PHP program to accept an email-id from the user and check the validity of the entered email-id using a regular expression. (15 M)

```php
<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = trim($_POST["email"] ?? "");
    echo preg_match("/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/", $email)
        ? "Valid email format" : "Invalid email format";
}
?>
<form method="post">
Email: <input type="email" name="email" required>
<button type="submit">Check</button>
</form>
```