########## Console ########## 


from css_generation import css_generation;
from pybash import pybash;
import subprocess as sp
import shutil
import os
import argparse
import json

def render_style(theme, code_size, code_line_height, markdown_size, markdown_line_height, reset_style):

    '''
    pybash('jupyter --config > jupyter_path.txt')

    jupyter_path_file = "jupyter_path.txt";
    File = open(jupyter_path_file, "r");
    path = File.read()[:-1]; ## drop the /n in the file
    File.close();
    os.remove(jupyter_path_file);
    '''
    path = sp.getoutput('jupyter --config');


    print("Your jupyter config dir is %s"%path);
    
    theme_path = {
        'default': 'null',
        'Tiger': 'Tiger_theme',
        'Cosmo': 'Cosmo_theme',
        'Bayern': 'Sports_team_themes/Soccer/Bayern Munchen',
        'Dortmund':'Sports_team_themes/Soccer/Dortmund',
        'Real_Madrid':'Sports_team_themes/Soccer/Real Madrid',
        'Barcelona':'Sports_team_themes/Soccer/Barcelona',
        'AC_Milan': 'Sports_team_themes/Soccer/AC Milan',
        'Inter_Milan': 'Sports_team_themes/Soccer/Inter Milan',
        'Chelsea': 'Sports_team_themes/Soccer/Chelsea',
        'Manchester_United': 'Sports_team_themes/Soccer/Manchester United'
        }; 
    
    
    '''
    theme = 'Tiger';
    #theme = 'default';
    #theme = 'Cosmo_theme';
    theme = 'Inter Milan';
    theme = 'Barcelona'
    code_size = '11px';                 
    code_line_height = '140%';
    markdown_size = '13px';
    markdown_line_height = '150%';
    '''

    # generating the jupyter style:
    # if you see 'Done!', refresh your jupyter
    
    if theme not in theme_path:
        theme = 'default';     

    ''' # remove this part; use json instead
    cur_dir = os.getcwd();  ## cd the .jupyter folder
    if theme=='keep':
        os.chdir(path);
        try:
            FILE = open('./custom/current_theme.txt','r', encoding="utf8");
            theme = FILE.read();
            FILE.close();
        except:
            theme = 'default';
            print('Set as default theme');
    os.chdir(cur_dir);
    '''
    theme_dir = theme_path[theme];
    
    css_generation(path, theme, theme_dir, markdown_size, markdown_line_height,
         code_size, code_line_height);
    
    if '__pycache__' in os.listdir():
        shutil.rmtree('__pycache__');

    ###############################
    # PATH -> the path name of your .jupyter folder
    # theme -> you can find theme in the folder 'themes'
    #          if want to use 'default', leave it as None
    # 
    # the following size paramaters: default value = None;
    
if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser(description='Render your jupyter style');
    parser.add_argument('-t','--theme', type=str, default='null', help='Choose a style');
    parser.add_argument('-cs','--code-size', type=str, default='null', help='choose the size of codes font');
    parser.add_argument('-clh','--code-line-height', type=str, default='null', help='choose the line height of each code line');
    parser.add_argument('-ms','--markdown-size', type=str, default='null', help='choose the size of markdown font');
    parser.add_argument('-mlh','--markdown-line-height', type=str, default='null', help='line height of each markdown line');
    parser.add_argument('-rs','--reset-style', type=str, default='False', help='line height of each markdown line'); 

    args_namespace = parser.parse_args(); 
    parameters = vars(args_namespace);    ## - will be _ underscore in dict
    cur_path = os.getcwd(); 
    path = sp.getoutput('jupyter --config');  # jupyter path

    os.chdir(path); ## go to .jupyter folder

    defaults = {
        'theme':'default',
        'code_size':'14px',
        'code_line_height':'140%',
        'markdown_size':'16px',
        'markdown_line_height':'140%',
        'reset': False
    }; 
    filename = 'parameters.json'; 

    if not os.path.exists(filename):        
        with open(filename, 'w+') as fp:
            json.dump(defaults, fp); 
  
    
    with open(filename, 'r') as fp:
        last_editted = json.load(fp); 
    
    if parameters['reset_style'].lower() == 'true':
        print('Resetting...')
        last_editted = defaults; 
    
    #print(parameters, last_editted)
    for key in parameters:
        if parameters[key] == 'null':
            parameters[key] = last_editted[key]; 
      
    os.remove(filename); 
    with open(filename, 'w+') as fp:
        json.dump(parameters, fp); 

    print('******Parameters******\n', parameters)

    os.chdir(cur_path);  ##  go back to current folder (custom)
    
    render_style(**parameters); 
    
    
    
    
    
    
    
