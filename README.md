# Bouncy numbers

## Problem statement

> Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.  
> Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.  
> We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.  
> Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.  
> Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.  
> *Find the least number for which the proportion of bouncy numbers is exactly 99%.*

## How to install

``` bash
# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# Installing dependencies
pip install -r requirements.txt
```

## How to use

``` bash
# Get help
python bouncy.py --help
python bouncy.py calculate --help
python bouncy.py checknumber --help

# Find the least number for a given proportion of bouncy numbers
python bouncy.py calculate # Default to 99
python bouncy.py calculate --proportion <proportion> # Replace <proportion>

# Check if a given number is bouncy
python bouncy.py checknumber --number <number> # Replace <number>
```

## Run tests

``` bash
pytest
```

## License

[MIT](https://github.com/GudarJs/bouncy-numbers/blob/master/LICENSE)
