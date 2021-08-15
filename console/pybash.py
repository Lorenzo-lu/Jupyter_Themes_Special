import os
import subprocess as sp

def pybash(command):
    header = '*'*10+'   py bash runner   '+'*'*10;
    footer = '*'*len(header);
    spacer = '~'
    print('%s\nbash input:\n%s\n%s \n%s'\
          %(header, spacer, command, footer));
    script_name = 'command.yz_log';
    if os.path.exists(script_name):
        script_name += '_';
    with open(script_name, 'w+') as FILE:
        FILE.write(command);
    print('bash output:\n%s'%spacer);
    try:
        print(sp.getoutput('bash %s'%(script_name)));
    except:
        print('%s\n'%footer);
        os.remove(script_name);
        raise;
    print('%s\n'%footer);
    os.remove(script_name);