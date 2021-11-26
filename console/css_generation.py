import os;
import shutil;
def css_generation(PATH, theme_key, theme, markdown_size, markdown_line_height,
                   code_size, code_line_height):
    print('You are choosing theme:', theme_key)
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
        #file = open('custom.css', 'r', encoding="utf8");
        #css = file.read();
    except:
        os.chdir(PATH);
        print('No valid theme chosen.\nUse default jupyter theme');
        #return False;

    os.chdir('%s/themes/custom'%(code_path));
    if 'custom.css' in os.listdir():
        file = open('custom.css', 'r', encoding="utf8");
        css = file.read(); 
        file.close();
        os.remove('custom.css');
    else:
        css = ''; 

    ## add online fonts
    
    '''
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/fonts/KaTeX_Main-Regular.woff2') format('woff');font-weight:normal;font-style:normal}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/fonts/KaTeX_Main-Bold.woff2') format('woff');font-weight:bold;font-style:bold}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/fonts/KaTeX_Main-Italic.woff2') format('woff');font-weight:normal;font-style:italic}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/fonts/KaTeX_Main-BoldItalic.woff2') format('woff');font-weight:bold;font-style:italic}"
    '''

    css = css + '\n@font-face {font-family:LaTeX; src: url("https://myresources.yizhoulu.repl.co/fonts/mwa_cmr10.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family:LaTeX; src: url("https://myresources.yizhoulu.repl.co/fonts/mwa_cmls10.ttf");font-weight:normal;font-style:italic}'; 

    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://myresources.yizhoulu.repl.co/fonts/KaTeX_Main-Regular.woff2') format('woff');font-weight:normal;font-style:normal}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://myresources.yizhoulu.repl.co/fonts/KaTeX_Main-Bold.woff2') format('woff');font-weight:bold;font-style:bold}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://myresources.yizhoulu.repl.co/fonts/KaTeX_Main-Italic.woff2') format('woff');font-weight:normal;font-style:italic}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://myresources.yizhoulu.repl.co/fonts/KaTeX_Main-BoldItalic.woff2') format('woff');font-weight:bold;font-style:italic}"
    
    css = css + '\n@font-face {font-family: "txtt_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/newtxtt.pfb.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "IBMPlex_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/consolasMono-Regular.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/CONSOLA.TTF");font-weight:normal;font-style:normal}';  
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/CONSOLAB.TTF");font-weight:bold;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/consolai.ttf");font-weight:normal;font-style:italic}'; 
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/consolaz.ttf");font-weight:bold;font-style:italic}'; 

    css = css + '\n@font-face {font-family: "DejaVuSansMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/DejaVuSansMono.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "DejaVuSansMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/DejaVuSansMono-Bold.ttf");font-weight:bold;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "DejaVuSansMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/DejaVuSansMono-Oblique.ttf");font-weight:normal;font-style:italic}'; 
    css = css + '\n@font-face {font-family: "DejaVuSansMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/DejaVuSansMono-BoldOblique.ttf");font-weight:bold;font-style:italic}'; 

    css = css + '\n@font-face {font-family: "UbuntuMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/UbuntuMono-Regular.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "UbuntuMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/UbuntuMono-Bold.ttf");font-weight:bold;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "UbuntuMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/UbuntuMono-Italic.ttf");font-weight:normal;font-style:italic}'; 
    css = css + '\n@font-face {font-family: "UbuntuMono_code"; src: url("https://myresources.yizhoulu.repl.co/fonts/UbuntuMono-BoldItalic.ttf");font-weight:bold;font-style:italic}'; 

    #https://lorenzo-lu.github.io/
    '''
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://lorenzo-lu.github.io/misc/fonts/KaTeX_Main-Regular.tff');font-weight:normal;font-style:normal}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://lorenzo-lu.github.io/misc/fonts/KaTeX_Main-Bold.tff');font-weight:bold;font-style:normal}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://lorenzo-lu.github.io/misc/fonts/KaTeX_Main-Italic.tff');font-weight:normal;font-style:italic}"
    css = css + "\n@font-face{font-family:KaTeX_Main; src:url('https://lorenzo-lu.github.io/misc/fonts/KaTeX_Main-BoldItalic.tff');font-weight:bold;font-style:italic}"

    css = css + '\n@font-face {font-family: "txtt_code"; src: url("https://lorenzo-lu.github.io/misc/fonts/newtxtt.pfb.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "IBMPlex_code"; src: url("https://lorenzo-lu.github.io/misc/fonts/IBMPlexMono-Regular.ttf");font-weight:normal;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://lorenzo-lu.github.io/misc/fonts/CONSOLA.TTF");font-weight:normal;font-style:normal}';  
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://lorenzo-lu.github.io/misc/fonts/CONSOLAB.TTF");font-weight:bold;font-style:normal}'; 
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://lorenzo-lu.github.io/misc/fonts/consolai.ttf");font-weight:normal;font-style:italic}'; 
    css = css + '\n@font-face {font-family: "consolas_code"; src: url("https://lorenzo-lu.github.io/misc/fonts/consolaz.ttf");font-weight:bold;font-style:italic}'; 
    '''

    ## using KaTeX font
    markdown_font = "KaTeX_Main"; 
    #code_font = "consolas_code"
    code_font = 'UbuntuMono_code'; 
    
    css = css + "\n.jp-RenderedHTMLCommon{font-family: %s, sans-serif !important}"%markdown_font; ## use !important to override
    css = css + "\n.jp-RenderedHTMLCommon h1, .jp-RenderedHTMLCommon h2,\
     .jp-RenderedHTMLCommon h3, .jp-RenderedHTMLCommon h4, \
     .jp-RenderedHTMLCommon h5, .jp-RenderedHTMLCommon h6{font-weight: bold!important}"; ## use !important to override
    
    
    css = css + '\ndiv.inner_cell{\nfont-size: %s;\n\
        line-height: %s;\nfont-family:"%s",sans-serif;}\n\n'%(markdown_size, markdown_line_height, markdown_font); 
    css = css + '.output pre, .CodeMirror-code{\nfont-size:%s;\n\
        line-height: %s;\nfont-family:"%s", monospace;}\n\n'%(code_size, code_line_height, code_font);
    #css = css + 'div.prompt,.prompt{\nfont-size:%s;\n\
    #    }\n\n'%(code_size);

    markdown_code_size = markdown_size;
    markdown_code_color = 'blue';
    #markdown_code_family = 'consolas_code';
    markdown_code_family = code_font; 
    
    ## for the verbatim in markdown
    css = css + '\n.rendered_html pre, .rendered_html code {background-color:transparent;color:%s;font-size:%s ;\
font-family:"%s", monospace}'%(markdown_code_color,markdown_code_size, markdown_code_family); ## for the jupyter notebook
    css = css + '\n.jp-RenderedHTMLCommon :not(pre) > code,  .jp-RenderedHTMLCommon code{background-color:transparent!important;color:%s!important ;font-size:"%s"!important;\
font-family:%s,monospace!important}'%(markdown_code_color, markdown_code_size, markdown_code_family); ## for the outputed html
    css = css + '\n pre {font-family:%s, monospace!important}'%code_font; 
    
    file = open('custom.css', 'w+', encoding="utf8");
    file.write(css);
    file.close();
    ## keep the theme name: if you only want to change font size, you can get info what theme you are using, and the variable will be set as current one
    file = open('current_theme.txt', 'w+', encoding="utf8");
    file.write(theme_key);
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





