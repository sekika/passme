import sys, os, re, getpass, warnings, copy
import hashlib, secrets
from configobj import ConfigObj
import clipboard
from .calc import genpass
from .html import genhtml

def main(argv=sys.argv[1:]):

    # Hard-coded configuration
    ConfFile = os.path.expanduser('~/.passme')
    Document = 'https://github.com/sekika/passme/blob/master/passme/doc/README.rst'
    hashes = ('sha384', 'sha512', 'sha3_384', 'sha3_512')
    chars = ('a','n','an','ans','ans95')

    # Default values of configuration in ConfFile
    ShowMasterPass = False
    ShowPass = True
    CopyPass = True
    VCS = ''
    SeedLen = 30
    DefaultHash = 'sha3_384'
    DefaultChar = 'an'
    DefaultLen = 14

    # Read configuration from ConfFile
    config = ConfigObj(os.path.expanduser(ConfFile))

    if 'SiteKeyFile' in config:
        SiteKeyFile = config["SiteKeyFile"]
    else:
        SiteKeyFile = input('Filename to save site keys: ')
        if os.path.exists(SiteKeyFile):
            print ('Sitekey file is specified. Initialization finished.')
        else:
            try:
                f = open(os.path.abspath(SiteKeyFile), 'w')
                f.write('# -*- coding: utf-8 -*-\n# Passme sitekey file\n\n')
                f.close()
                print ('Sitekey file is initialized. Initialization finished.')
            except:
                print ('Error: cannot create sitekey file: {0}'.format(SiteKeyFile))
                sys.exit()
        SiteKeyFile = os.path.abspath(SiteKeyFile)
        config['SiteKeyFile'] = SiteKeyFile
        config.write()
        sys.exit()
    if not os.path.exists(SiteKeyFile):
        try:
            f = open(SiteKeyFile, 'w')
            f.write('# -*- coding: utf-8 -*-\n# Passme sitekey file\n\n')
            f.close()
        except:
            print ('Error: cannot create sitekey file: {0}'.format(SiteKeyFile))
            print ('Check the filename in {0}'.format(ConfFile))
            sys.exit()

    if 'ShowMasterPass' in config:
        if  config['ShowMasterPass'] =='True': ShowMasterPass = True
    config['ShowMasterPass'] = ShowMasterPass

    if 'ShowPass' in config:
        if  config['ShowPass'] == 'False': ShowPass = False
    config['ShowPass'] = ShowPass

    if 'CopyPass' in config:
        if  config['CopyPass'] == 'False': CopyPass = False
    config['CopyPass'] = CopyPass

    if 'SeedLen' in config:
        if config['SeedLen'].isdigit(): SeedLen = config['SeedLen']
    config['SeedLen'] = SeedLen

    if 'VCS' in config:
        VCS = config['VCS']
    config['VCS'] = VCS

    config.write()

    if 'DefaultHash' in config:
        DefHash = config['DefaultHash']
        if DefHash in hashes: DefaultHash = DefHash

    if 'DefaultChar' in config:
        DefChar = config['DefaultChar']
        if DefChar in chars: DefaultChar = DefChar

    if 'DefaultLen' in config:
        if config['DefaultLen'].isdigit(): DefaultLen = config['DefaultLen']

    # Read commandline argument
    if (len(sys.argv)) == 1:
        print ('Usage:\npassme site [master]\npassme add\npassme list\npassme edit\npassme html\n\nFull document at\n{0}'.format(Document))
        sys.exit()
    else:
        site = sys.argv[1]

    # Open sitekey file
    sitekey = ConfigObj(SiteKeyFile, encoding='utf-8')

    # list command
    if site == 'list':
        print (sorted(sitekey.keys()))
        sys.exit()

    # edit command
    if site == 'edit':
        if 'OpenEditor' in config:
            OpenEditor = config['OpenEditor']
            os.system(OpenEditor + ' ' + SiteKeyFile)
        else:
            OpenEditor = input('Command to invoke text editor: ')
            if OpenEditor == '': sys.exit()
            config['OpenEditor'] = OpenEditor
            config.write()
            os.system(OpenEditor + ' ' + SiteKeyFile)
        sys.exit()

    # add command
    if site == 'add':
        while True:
            site = input('Site name: ')
            if site in ('add', 'list', 'edit', 'html', 'ALL'):
                print ('{0} is reserved.'.format(site)); site=''
            if site == '': sys.exit()
            if site in sitekey:
                print ('{0} is already defined.'.format(site))
                confirm = input('Are you sure to overwrite? If yes, type SURE: ')
                if not confirm == 'SURE': site = ''
            if site > '': break
        has = DefaultHash
        config['DefaultHash'] = DefaultHash
        while True:
            char = input('Character ({0}): '.format(DefaultChar))
            if char == '': char = DefaultChar
            if char in chars: break
        if char == 'ans95':
            print ('Warning: Javascript version does not work with ans95')
        config['DefaultChar'] = char
        while True:
            plen = 0
            p = input('Password length ({0}): '.format(DefaultLen))
            if p == '': plen = int(DefaultLen)
            if p.isdigit(): plen=int(p)
            if plen > 0: break
        config['DefaultLen'] = plen
        h = hashlib.sha3_512()
        h.update(secrets.token_bytes(128))
        for key in sitekey.keys():
            h.update(sitekey[key]['seed'].encode('utf-8'))
        seed = genpass(h.digest(), 'sha3_512', 'ans', int(SeedLen))
        comment = ''
        while True:
            c = input('Comment (no input to finish): ')
            comment = comment + c + '\n'
            if c == '':
                comment = comment.rstrip()
                break
        sitekey[site] = {}
        sitekey[site]['hash'] = has
        sitekey[site]['char'] = char
        sitekey[site]['len'] = plen
        sitekey[site]['seed'] = seed
        sitekey[site]['comment'] = comment
        print (comment)
        sitekey.write()
        config.write()
        print ('New sitekey for {0} was written in {1} as\nhash = {2}, char = {3}, len = {4}, seed = {5}\n{6}'.format(site, SiteKeyFile, has, char, plen, seed, comment))
        if VCS == 'git':
            print (os.path.basename(SiteKeyFile))
            os.system('cd '+os.path.abspath(os.path.dirname(SiteKeyFile))+'; git add '+os.path.basename(SiteKeyFile) + '; git commit -m "Changed by passme add command"; git push; git log -p -1')
        sys.exit()

    # html command
    if site == 'html':
        os.chdir(os.path.dirname(SiteKeyFile))
        print ('Working directory: {0}'.format(os.getcwd()))
        sites = []
        file = input('Output filename: ')
        try:
            f = open(file, 'w')
        except:
            print ('Error: cannot create file: {0}'.format(file))
            sys.exit()
        while True:
            site = input('Default site (ALL for all sites): ')
            if site == '': sys.exit()
            if site in sitekey:
                sites.append([site,sitekey[site]])
                break
            else:
                if site == 'ALL': break
                print ('{0} not found.'.format(site))
        if site == 'ALL':
            for site in sorted(sitekey.keys()):
                sites.append([site,sitekey[site]])
        else:
            while True:
                site = input('Another site (return to finish): ')
                if site == '': break
                if site in (sitekey.keys()):
                    sites.append([site,sitekey[site]])
                else:
                    print ('{0} not found.'.format(site))
        html = genhtml(sites)
        f.write(html)
        f.close
        sys.exit()

    # Site not defined
    if site == '': sys.exit()
    if site not in sitekey:
        print ('Site {0} is not defined.'.format(site))
        for s in sitekey:
            if 'comment' in sitekey[s]:
                if sitekey[s]['comment'].encode('utf-8').find(site.encode('utf-8')) > -1:
                    print ('[ Suggestion: {0} ]\n{1}'.format(s, sitekey[s]['comment']))
        sys.exit()
    
    # Read sitekey
    s = sitekey[site]
    for key in 'hash', 'char', 'len', 'seed':
        if key not in s:
            print ('Error in sitekey file: {0} not defined in {1}.'.format(key, site))
            sys.exit()
    if 'comment' in s:
        print (s['comment'])
    
    # Ask master password
    
    if (len(sys.argv)) > 2:
        master = sys.argv[2]
    else:
        if ShowMasterPass:
            master = input('Master password: ')
        else:
            master = getpass.getpass('Master password: ')
    
    seed = (master + s['seed']).encode('utf-8')
    
    # Generate password
    password = genpass(seed, s['hash'], s['char'], int(s['len']))
        
    # Show password
    if ShowPass: print (password)
    
    if CopyPass:
        clipboard.copy(password)
        print ('Password copied to clipboard.')
