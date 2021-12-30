# Integral Image Tools

Integral Image tools is a Python library for calculating integral image and sum of pixels of a rectangle with given border points.

## Information

A summed-area table (or integral image) is a data structure and algorithm for quickly and efficiently generating the sum of values in a rectangular subset of a grid.  

A cell in the Integral image corresponds to a specific area in the original image. The value of that cell is the sum of all the values in that corresponding area in the original image.

Look at the example:  
![alt original image](https://psv4.userapi.com/c237231/u275559158/docs/d8/a15ea25cd4f7/0_ZaFmHzlhp3VKniaH.png?extra=MAODG-YMbWXVxwlrVRZDEb685Es9icrzsm3jNmpj_Yfk-1cin0B3hkKJKzJA2PpUg8L7bgf4RBFX7lViiUVI3eonscdCEHi8FuAPOFNSpCNm06o04taxOwhX8TJ9BVDK1r81Y01Y-COV-9ZZtpTQZJs9fnA)  
![alt integral image](https://psv4.userapi.com/c237231/u275559158/docs/d35/ebd76cb6ee81/1_vBy_3EqGmRbCuvsav4ffVg.png?extra=-qUgz6kQdfzxPzxFftIZ4z5OvpCE1Ag3uk4OYfoobjaTlHV8LBOt3Jn7KFMy8U_V5rm_YNC6Qt0xL9zGHYcN5wGcjKFIXGhP34a1vJ5IN3QdADAkSufTljSjpoYGN80hTSj4RCfXbiqle-qJoAGuT7XAzrY)  

This allows us to calculate the sum of any rectangle within the integral image with any given borders:  
![alt sum example](https://psv4.userapi.com/c235131/u275559158/docs/d27/33ef0ac98b51/3.png?extra=ientWyZGsCkF2IUA_X4EHe_SJbhE3gU07gC3Fnqu53Uybq2EByg55h_Jx_N6iJjA-rJsUc8DKCtdrS8fy6ANhK3BNiw8xrHbEAs9kKt6cwBzq5R_RAZGlie_6BNndcyAfGhfswemMlgybFkl7ddfpvLKPFs)  

More information:  
- [Wikipedia](https://en.wikipedia.org/wiki/Summed-area_table)  
- [Nice detailed visualization and more](https://levelup.gitconnected.com/the-integral-image-4df3df5dce35)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install integral_image_tools
```

## Usage

### Import

```python
from integral_image_tools import integral_image as ii
```

### Functions
```python
ii.integral_view(image: list[list[int]])
``` 
```python
ii.rect_sum(rect: list[list[int]], x1: int, y1: int, x2: int, y2: int)
```
#### Description

##### ii.integral_view
Calculates matrix of integral image for "image"

##### ii.rect_sum
Calculates sum of pixels of a rectangle within given borders

### Arguments

#### Description

##### image, rect
Matrices

##### x1, y1
Top left border coordinates

##### x2, y2
Bottom right border coordinates 

#### Requirements for arguments

##### image
- must be a matrix (list of lists of integers)
- its items must be integers in range 0..255   

##### rect
- must be a matrix (list of list of integers)

##### x1, y1, x2, y2
- must be positive integers
- cannot be out of boundaries of "rect"

### Examples

```python
ii.integral_view(
    [
        [244, 31, 31, 205],
        [101, 221, 226, 196],
        [56, 167, 89, 161],
        [101, 38, 151, 87]
    ]
)
# returns: 
# [
#     [244, 275, 306, 511],
#     [345, 597, 854, 1255],
#     [401, 820, 1166, 1728],
#     [502, 959, 1456, 2105]
# ]

ii.integral_view('TEST')
# raises ValueError

ii.rect_sum(
    [
        [244, 31, 31, 205],
        [101, 221, 226, 196],
        [56, 167, 89, 161],
        [101, 38, 151, 87]
    ],
    2, 3, 3, 3
)
# returns 238

ii.rect_sum('TEST', -1)
# raises ValueError
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)