# Iterative Prompt Development

Getting the right prompt that works for your task is crucial for the success of your model. In this section, we will discuss how to iteratively develop prompts for your task.

It is almost impossible to get the perfect prompt in the first try. You will have to iterate over multiple prompts to get the best one. Here is a step-by-step guide to iteratively develop prompts for your task:

1. **Be clear and Specific**: The first step is to be clear and specific about the task you want the model to perform. You should have a clear understanding of the task and the type of output you expect from the model.
2. **Analyse why result does not give the desired output**: If the model is not giving the desired output, try to understand why it is failing. Is it because the prompt is not clear, or the model is not capable of performing the task?
3. **Refine the idea and the prompt**: Based on the analysis, refine the idea and the prompt. Make sure the prompt is clear and specific.
4. **Repeat the process**: Keep repeating the process until you get the desired output.

Example 1.

## Generate a marketing product description from a product fact sheet

### Prompt 1:

````python
fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture,
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black,
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities:
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""

prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

Technical specifications: ```{fact_sheet_chair}```"""
response = get_completion(prompt)
print(response)
````

### Issue 1: The text is too long

- Limit the number of words/sentences/characters.

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

Use at most 50 words. // use at most 3 sentences.

Technical specifications: ```{fact_sheet_chair}```"""
response = get_completion(prompt)
print(response)

len(response.split())
````

### Issue 2. Text focuses on the wrong details

- Ask it to focus on the aspects that are relevant to the intended audience.

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```"""
response = get_completion(prompt)
print(response)
````

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```"""
response = get_completion(prompt)
print(response)
````

### Issue 3. Description needs a table of dimensions

- Ask it to extract information and organize it in a table.

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification.

After the description, include a table that gives the
product's dimensions. The table should have two columns.
In the first column include the name of the dimension.
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website.
Place the description in a <div> element.

Technical specifications: ```{fact_sheet_chair}```"""

response = get_completion(prompt)
print(response)
````

Prompt development is an iterative process. Keep refining the prompt until you get the desired output.

For beign a good prompt engineer, it about having a process and iterating over it.
