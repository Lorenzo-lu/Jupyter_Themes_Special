import os;
import shutil;
def css_generation(PATH, theme, markdown_size, markdown_line_height,
                   code_size, code_line_height):

    # theme will be the path of theme from a dictionary in this version
    code_path = os.getcwd();
    theme = 'default' if not theme else theme;
    markdown_size = 'none' if not markdown_size else markdown_size;
    markdown_line_height = 'none' if not markdown_line_height else markdown_line_height;
    code_size = 'none' if not code_size else code_size;
    code_line_height = 'none' if not code_line_height else code_line_height;

    os.chdir('themes');
    if 'custom' in os.listdir():
        shutil.rmtree('custom');
    os.mkdir('custom');
    
    try:
        os.chdir(theme);
        for item in os.listdir():
            src = '%s/themes/%s/%s'%(code_path, theme, item);
            tgt = '%s/themes/custom/%s'%(code_path, item);            
            try:
                shutil.copytree(src, tgt);
            except:
                shutil.copy(src, tgt);
        #file = open('custom.css', 'r');
        #css = file.read();
    except:
        os.chdir(PATH);
        print('Wrong theme path');
        return False;

    os.chdir('%s/themes/custom'%(code_path));
    if 'custom.css' in os.listdir():
        file = open('custom.css', 'r');
        css = file.read(); 
        file.close();
        os.remove('custom.css');
    else:
        css = '';
    
    css = css + 'div.inner_cell{\nfont-size: %s;\n\
        line-height: %s}\n\n'%(markdown_size, markdown_line_height);
    css = css + '.output pre, .CodeMirror-code{\nfont-size:%s;\n\
        line-height: %s}\n\n'%(code_size, code_line_height);
    css = css + 'div.prompt,.prompt{\nfont-size:%s;\n\
        }\n\n'%(code_size);
    
    file = open('custom.css', 'w+');
    file.write(css);
    file.close();
    new_css_loc = os.getcwd();
    
    os.chdir(PATH);
    if 'custom' in os.listdir():
        shutil.rmtree('custom');

    shutil.move(new_css_loc, '%s/custom'%PATH);
    
    os.chdir(code_path);
    if '__pycache__' in os.listdir():
        shutil.rmtree('__pycache__');
    os.chdir(code_path + '/themes');
    if 'custom' in os.listdir():
        shutil.rmtree('custom');
    print('Done!')





