########## Console ########## 


from css_generation import css_generation;

File = open("jupyter_path.txt", "r");
path = File.read()[:-1]; ## drop the /n in the file
File.close();
print("Your jupyter config dir is %s"%path);


theme = 'Tiger_theme';
#theme = 'default';
#theme = 'Cosmo_theme';
code_size = '11px';                 
code_line_height = '140%';
markdown_size = '13px';
markdown_line_height = '150%';

# generating the jupyter style:
# if you see 'Done!', refresh your jupyter
css_generation(path, theme, markdown_size, markdown_line_height,
     code_size, code_line_height);


###############################
# PATH -> the path name of your .jupyter folder
# theme -> you can find theme in the folder 'themes'
#          if want to use 'default', leave it as None
# 
# the following size paramaters: default value = None;
