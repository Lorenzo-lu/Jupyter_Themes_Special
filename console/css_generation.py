import os;
import shutil;
def css_generation(PATH, theme, markdown_size, markdown_line_height,
                   code_size, code_line_height):
    file_path = os.getcwd();
    
    theme = 'default' if not theme else theme;
    markdown_size = 'none' if not markdown_size else markdown_size;
    markdown_line_height = 'none' if not markdown_line_height else markdown_line_height;
    code_size = 'none' if not code_size else code_size;
    code_line_height = 'none' if not code_line_height else code_line_height;
    

    os.chdir('themes');
    themename = theme + '.txt';
    if themename in os.listdir():        
        file = open(themename, 'r');
        css = file.read();
    else:
        css = '';

    css = css + 'div.inner_cell{\nfont-size: %s;\n\
        line-height: %s}\n\n'%(markdown_size, markdown_line_height);
    css = css + '.output pre, .CodeMirror-code{\nfont-size:%s;\n\
        line-height: %s}\n\n'%(code_size, code_line_height);

    os.chdir(PATH);
    if 'custom' in os.listdir():
        shutil.rmtree('custom');

    os.mkdir('custom');
    css_file = open('custom/custom.css', 'w+');
    css_file.write(css);

    os.chdir(file_path);
    if '__pycache__' in os.listdir():
        shutil.rmtree('__pycache__');
    print('Done!')





