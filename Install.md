# Installation Guide

## 1. Install python3
1. Open web browser, go to [Python page](https://www.python.org/)
2. Download Python3 newest version
3. Run and install

## 2. Install pip
Before do this step, you should check if your computer already had pip. If you download python 3 from
step one. Then you already installed pip
1. Open web browser, go to [Pip page](https://pip.pypa.io/en/stable/)
2. Download __*get-pip.py*__
3. Open terminal as __administrator__
4. Run __*python get-pip.py*__
5. Update pip by run __*python -m pip install -U pip*__ if you use windows or __*pip install -U pip*__ 
if you use mac or linux

## 3. Install pipenv (optional)
As a developer, your don't only need to develop a software project without conflicts with any other project, using a virtual environment. You have also need to sharing your software project to other users (e.g., developers) in such a way they can easily install it.

The code of our project generally depends on many third-party Python libraries. Any other developer interested in using your software project has to install these libraries too. But how to list these libraries with their specific version for your project? How to automatically install these libraries?

Pipenv solves all these problems:
1. creating an isolated environment for a software project;
2. installing a new third-party library with a specific version (while you are developing your software project);
3. keeping track of all the third-party libraries your project depends on;
4. installing all the dependencies for a software project (when another developer wants to use your project).

To install pipenv:
1. Open terminal as __administrator__
2. Run __*pip install pipenv*__

## 4. Install pygame
We have two ways to install pygame. You can find more information [here](https://www.pygame.org/news)
<br />
<br />If you want install as global directory:
1. Open terminal as __administrator__
2. Run __*pip install pygame*__ 

If you want install as workplace directory only:
1. Open terminal as __administrator__
2. Move to your workplace
3. Run __*pipenv shell --three*__ and wait for pipenv is installing
4. Run __*pipenv install pygame*__

## 5. Download and Import python files
1. Open terminal as __administrator__
2. Move to your workplace 
(if you  do not install pygame as global directory, do install pygame again after step 3)
3. Run __*git init*__ then run **_git clone 
http://gitlab-students.int.intek.edu.vn/mission/intek-mission-cardinal_numerals-playground/sm2_2019_dat_cuong.git_**
4. Create new python file. At first line type **_import cardinal_numeral_**
5. If you want cover number to vietnamese string, 
type **_cardinal_numeral.integer_to_vietnamese_numeral(number, region, active_tss)_**.
<br />
If you want cover number to english string, 
type **_cardinal_numeral.integer_to_english_numeral(number, active_tss)_**.

> Number is the number your want to cover, region is 'north' or 'south'.
>If you want your computer speak this number, set active_tss is True.
><br />Region is set default as 'north' and active_tss is set default as False

## 6. Use with GUI
To use this project with GUI, you need follow these steps:
1. Install [wxpython](https://wxpython.org/)
2. Open terminal as __administrator__
3. Move to your workplace where you clone this project
4. Run __*python3 GUIs.py*__

## 7. Use test case
1. Install [pytest](https://docs.pytest.org/en/latest/contents.html)
2. Open terminal as __administrator__
3. Move to your workplace where you clone this project
4. Run __*pytest -v MyTest.py*__

Update date 08/08/2019


