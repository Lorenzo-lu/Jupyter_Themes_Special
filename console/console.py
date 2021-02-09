########## Console ########## 


from css_generation import css_generation;

# this is the path to your '.jupyter' folder (required)
PATH = ''; 

theme = 'PH-theme';
code_size = '80%';                 
code_line_height = None;
markdown_size = None;
markdown_line_height = None;

# generating the jupyter style:
# if you see 'Done!', refresh your jupyter
css_generation(PATH, theme, markdown_size, markdown_line_height,
     code_size, code_line_height);


##############################
# PATH -> the path name of your .jupyter folder
# theme -> you can find theme in the folder 'themes'
#          don't include '.txt'; if want to use 'default', leave it as None
#
# the following size paramaters: default value = None;
