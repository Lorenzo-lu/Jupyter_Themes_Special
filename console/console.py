########## Console ########## 


from css_generation import css_generation;
from pybash import pybash;
import subprocess as sp
import shutil
import os
import argparse

def render_style(theme, code_size, code_line_height, markdown_size, markdown_line_height):
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
    
    cur_dir = os.getcwd();
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
    css_generation(path, theme, theme_path[theme], markdown_size, markdown_line_height,
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
    parser.add_argument('-t','--theme', type=str, default='keep', help='Choose a style');
    parser.add_argument('-cs','--code-size', type=str, default='11px', help='choose the size of codes font');
    parser.add_argument('-clh','--code-line-height', type=str, default='140%', help='choose the line height of each code line');
    parser.add_argument('-ms','--markdown-size', type=str, default='13px', help='choose the size of markdown font');
    parser.add_argument('-mlh','--markdown-line-height', type=str, default='150%', help='line height of each markdown line');
    
    
    args_namespace = parser.parse_args();
    render_style(**vars(args_namespace))
    
    
    
    
    
    
    
