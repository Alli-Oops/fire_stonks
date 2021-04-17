# Firestonks - Capstone Setup
## Skills Assessed
- Following directions and reading comprehension
- Reading tests
- Creating classes
  - Classes have attributes and instance methods
- Importing modules
- Working with attributes that are lists of instances
- Implementing instance methods that interact with other instances and objects
- Implementing inheritance
- Overriding methods from superclasses and Object

## Goal
You want to manage, organize and present your stonk analysis. You have a bunch of stonks you have bought or are thinking about buying. And you’ve done your research! It would be awesome if you could organize and match your favorite stonks with all the research you have already done and make predictions too!
On this platform, each person registers online as a user. Also, they should list their favorite stonk picks.
You envision an app where users can match stonk picks with various resources that they have found that make them think it’s a good investment. Each resource will provide justification for the stonk analysis - and the resource might be created by the user or cited.
For this capstone, given some features that the users want, create a set of classes, following the directions below. The directions will lead you to create many class definitions, their attributes and instance methods, and some other cool features. Users will be able to add their top stonk picks, make predictions, and connect their assessment to their research (aka due diligence)!

## One-Time Project Setup
Follow these directions once, a the beginning of your project:
1. Navigate to your projects folder named `capstone`

```bash
$ cd ~/Developer_C15/capstone
```

2. "Clone" (download a copy of this project) into your capstone folder. This command makes a new folder called `firestonks`, and then puts the project into this new folder.

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

3. Move your location into this project folder

```bash
$ cd firestonks
```

4. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

5. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

6. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:

- [ ] `cd` into your `capstones` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `firestonks` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependences with `pip`

## Project Development Workflow
1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

2. Find the test file that contains the test you want to run.

   - Check the `tests` folder, and find the test file you want to run
   - In that test file, read through each test case

3. Run the tests for your specific wave

```bash
# Must be in activated virtual environment
$ pytest tests/test_wave_01_updated.py
```

4. Focus on the top test failure. Read through the test failure, and understand why the failure is happening. Confirm your findings with a classmate.
5. Make a plan to fix the test failure.
6. Write code to fix the test failure.
7. Re-run the tests.
8. Repeat steps 5-7 until that test passes!
9. Repeats steps 4-8 until you have finished all tests in the file.
10. Begin using the test file of the next wave!
11. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

## Details About How to Run Tests
Run all tests that exist in this project with:

```bash
# Must be in activated virtual environment
$ pytest
```

If you want to run all tests that exist in one file, use:

```bash
# Must be in activated virtual environment
$ pytest tests/test_file_name.py
```

... where `test_file_name.py` is relpaced with the correct test file name.

If you want to see any `print` statements print to the console, add `-s` to the end of any `pytest` command:

```bash
# Must be in activated virtual environment
$ pytest -s
```

## Project Write-Up: How to Complete and Submit
The goal of this capstone setup is to refactor and create tests and code in various files in the `firestonks` directory so that all the tests pass and the end result will set up a capstone project to expand on in later units and as more skillsets are mastered.

To complete this project, use the above workflow and follow these steps:

1. Start with making the tests in `test_wave_01_updated.py` pass.
1. Review your code in the `firestonks` directory and see if there are ways you can make the code more readable.
1. Then, work on making the tests in `test_wave_02_updated.py` pass.
1. Review your code in the `firestonks` directory
1. Repeat on all test files until submission time.

At submission time, no matter where you are, submit the project via Learn.

## Project Directions
This project is designed to set up a capstone project - that one could puzzle together and connect with new skills and tools to expand into a dynamic website later on - how to implement this project without many directions. Being able to use tests to drive project completion is a skill that needs to be developed; programmers often take years to develop this skill competently.

When our test failures leave us confused and stuck, let's use the detailed project requirements below.

### Wave 1 - Updated
The first two tests in wave 1 imply:
  -There is a module (file) named 'user.py’ inside of the ’fire_stonks' package (folder)
  -Inside this module, there is a class named 'User'
  -Each 'User' will have an attribute named 'stonk_picks', which is an empty list by default
  -When we create an instance of 'User', we can optionally pass in a list with the keyword argument 'stonk_picks'
The remaining tests in wave 1 imply:
  -Every instance of 'User' has an instance method named add, which takes in one stonk
  -This method adds the stonk to the 'stonk_picks'
  -This method returns the stonk that was added
  -Similarly, every instance of 'User' has an instance method named remove, which takes in one stonk
  -This method removes the matching stonk from the 'stonk_picks'
  -This method returns the stonk that was removed
  -If there is no matching item in the 'stonk_picks', the method should return False

### Wave 2 - Updated
The first tests in wave 2 imply:
- There is a module (file) named ‘stonk.py’ inside of the 'fire_stonks' package (folder). Inside this module, there is a class named 'Stonk'
AND there is a module (file) module (file) named ’duediligence.py’. -Inside this module, there is a class named 'DueDiligence'

Test 2.1
-Each 'Stonk' will have an attribute named 'ticker', which is an empty string by default
-When we initialize an instance of 'Stonk', we can optionally pass in a string with the keyword argument 'ticker'

Test 2.2
-Each 'Stonk' will have an attribute named research, which is an empty list by default
-When we initialize an instance of 'Stonk', we can optionally pass in/ add an element to the keyword argument research which is a list
-Each 'Stonk' will have an attribute named research, which is an empty list by default

Test 2.3
-Each 'DueDiligence' will have an attribute named author, which is an empty string by default and indicates whether or not the instance is the 'User'’s original content - or another author/cited source.

Test 2.4
-The 'Stonk' class will have a method named get_by_author
-It takes one argument: a string, representing an author
-This method returns a list of 'DueDiligence' instances from the research list with that author

### Wave 3 - Updated
The first test in wave 3 implies:

Test 3.1
-When we stringify an instance of 'DueDiligence' using ‘str()’, it returns "This resource provides an analysis that helps justify a stonk pick"
-This implies 'DueDiligence' overrides its stringify method

The remaining tests in wave 3 imply:
-A primary instance of 'User' has an instance method named 'copy_stonk'
-It takes 2 arguments: another (influencer) instance of 'User' and a 'nice_stonk' in that influencer’s 'stonk_picks'

Tests 3.2, 3.3, 3.4,
-The 'copy_stonk' method will append a 'nice_stonk' in another 'User'’s (aka influencer’s) 'stonk_picks' to the primary 'User' instance’s 'stonk_picks'
and the method returns True
-If this 'User'.influencer’s 'stonk_picks' doesn't contain 'nice_stonk', the method returns False

### Wave 4 - Updated
Test 4.1*
The tests in wave 4 imply that instances of  the'User' class have an optional attribute ‘influence_count’ that has a default argument set to an integer of 0. This will track the number of times other 'User'’s copy a stonk from their 'stonk_picks'. 

Test 4.2*
The tests in wave 4 also imply that instances of 'Stonk' have an attribute 'copy_count' that has a default integer of 0. This will track the number of times other 'User'’s copy that particular 'Stonk' instance.

Tests 4.3* and 4.4* test that counters increase by 1 point when the ‘copy_stonk’ method is called.
Test 4.3
When the 'copy_stonk' method is called and returns True - the instance of the influencing ‘User's ‘copy_count’ increases by 1
Test 4.4
When the 'copy_stonk' method is called and returns True - the instance of the copied'Stonk's (‘nice_stonk') ‘influence_count’ increases by 1

Test 4.5 implies a helper function ‘add_dd' that handles situations where the primary 'User' copies a ‘nice_stonk’ that’s ticker matches a ‘stonk’ they already have in their ‘stonk_picks’. This function will add any unique ‘DueDiligence’ in the influencing ‘User’'s ‘nice_stonk’’s research list to the primary ‘User’’s matching-ticker stonk’s research list.

Test 4.5
When the 'copy_stonk' method is called and returns True - 
*if the primary 'User' who copies 'nice_stonk' (from another 'User') already has a stonk with the same 'ticker' in their 'stonk_picks' then - the function will add from (the influencer’s)  'nice_stonk's research list any elements of due_diligence if the due_diligence’s resource is not the same as any items belonging to the stonk with the same 'ticker' in the primary'User'’s ‘stonk_picks’. This will update the primary ‘User’'s stonk to include the unique research that the other ‘User’ attributed to the same ticker.

#### Using Inheritance

Now, we may notice that some of these classes hold the same types of state and have the same behavior. That makes this is a great opportunity to use inheritance! In the future phases of the project, go back and implement the `Citedsource`and `Usersource`, classes so that they inherit from the `DueDiligence` class. This should eliminate repetition in your code and greatly reduce the total number of lines code in your program!

Similarly - the `Stonk`class has a `Prediction` that can be refactored into it own class with subclasses for the various plays (i.e. `ShortPlay`, `LongPlay`, `ComplexPlay`). This will allow for future enhancements and specifications in terms of the whats/whens/whys/hows a user considers with each stonk prediction - including details about how they might play or implement their analysis.
##### Hint: Importing Prediction
You'll need to refer to `Prediction` in order to declare it as a parent. To reference the `Prediction` class into these modules, try this import line:
If you need to import the `Prediction` class into these modules, try this import line:

```python
from firestonks.prediction import Prediction
```

### DRYing up the code

The further reduce the amount of repeated code in your project, consider how and what functions might be able to make use of other functions you've already created. Is there a way that these methods could incorporate a call to another function or method into the body of these methods?

Try it out and see if the tests still pass! If you can't get them to pass with this refactor, you can always return to the most recent working commit before you submit the project!

## Optional Enhancements
Condsider making a class for `Prediction` that has the subclasses `ShortPlay`, `LongPlay`, and `ComplexPlay`

- The `Prediction` objects should all have:
  - A buy date and price
  - A sell date and price
    - An percentage/quantity to sell on the sell date
  - A return prediction
  - And - an optional list of `DueDiligence` objects that support this specific play
# fire_stonks
