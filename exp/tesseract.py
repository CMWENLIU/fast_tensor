#import Image
#except ImportError:
import PIL
from PIL import Image
import pillowfight
#import pytesseract
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[17]
print("Will use lang '%s'" % (lang))

#------------------
input_img = PIL.Image.open("test.JPG")
output_img = pillowfight.ace(input_img)


txt = tool.image_to_string(
    #Image.open(output_img),
    output_img,
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
# txt is a Python string
print(txt)
word_boxes = tool.image_to_string(
    Image.open('test2.png'),
    lang="eng",
    builder=pyocr.builders.WordBoxBuilder()
)
# list of box objects. For each box object:
#   box.content is the word in the box
#   box.position is its position on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

line_and_word_boxes = tool.image_to_string(
    Image.open('test2.png'), lang="eng",
    builder=pyocr.builders.LineBoxBuilder()
)
# list of line objects. For each line object:
#   line.word_boxes is a list of word boxes (the individual words in the line)
#   line.content is the whole text of the line
#   line.position is the position of the whole line on the page (in pixels)
#
# Each word box object has an attribute 'confidence' giving the confidence
# score provided by the OCR tool. Confidence score depends entirely on
# the OCR tool. Only supported with Tesseract and Libtesseract (always 0
# with Cuneiform).
#
# Beware that some OCR tools (Tesseract for instance) may return boxes
# with an empty content.

# Digits - Only Tesseract (not 'libtesseract' yet !)
digits = tool.image_to_string(
    Image.open('test2.png'),
    lang=lang,
    builder=pyocr.tesseract.DigitBuilder()
)
# digits is a python strin


# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#print('is this correct?')
# Simple image to string
#print(pytesseract.image_to_string(Image.open('test.JPG')))
#print(pytesseract.image_to_string(Image.open('test2.png')))
# French text image to string
#print(pytesseract.image_to_string(Image.open('test.JPG'), lang='fra'))

# Get bounding box estimates
#print(pytesseract.image_to_boxes(Image.open('test.JPG')))

# Get verbose data including boxes, confidences, line and page numbers
#print(pytesseract.image_to_data(Image.open('test.JPG')))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open('test.JPG'))
