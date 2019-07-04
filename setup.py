import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='dokr',  

     version='0.1',

     scripts=['dokr.sh'] ,

     author="Sunny Dhoke",

     author_email="sunnydhoke22@gmail.com",

     description="A hello world",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/sunn-e/dokr",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )