########## Console ########## 


from css_generation import css_generation;
import subprocess as sp;

# this is the path to your '.jupyter' folder (required)
#PATH = '/Users/yizhoulu/.jupyter';
PATH = sp.getoutput('jupyter --config');
print("Your jupyter config dir is %s"%PATH);

theme = 'Tiger_theme';
#theme = 'default';
code_size = '11px';                 
code_line_height = '140%';
markdown_size = '13px';
markdown_line_height = '150%';

# generating the jupyter style:
# if you see 'Done!', refresh your jupyter
css_generation(PATH, theme, markdown_size, markdown_line_height,
     code_size, code_line_height);


###############################
# PATH -> the path name of your .jupyter folder
# theme -> you can find theme in the folder 'themes'
#          if want to use 'default', leave it as None
# 
# the following size paramaters: default value = None;
