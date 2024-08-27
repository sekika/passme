def genhtml(sites):

    ##############################################
    html = r'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Passme JS</title>

<style type="text/css">
    fieldset {
        margin: 0; padding: 0.75em; background: #efe; border: solid 1px #999; border-bottom-width: 0; line-height: 1.3em;
        border-top-left-radius: 0.5em; -moz-border-radius-topleft: 0.5em; -webkit-border-top-left-radius: 0.5em;
        border-top-right-radius: 0.5em; -moz-border-radius-topright: 0.5em; -webkit-border-top-right-radius: 0.5em;
    }
    fieldset.siteinfo {
        line-height: 2.5em;
    }
    fieldset label { display: block; float: left; margin-right: 0.75em; }
    fieldset div.Field { overflow: hidden; }
    fieldset div.Field input {
        width: 100%; background: none; border: none; outline: none; -webkit-appearance: none;
    }
    input.Result { width: 98%; background: #ada; }
    input.Copy { width: 100%; background: #ddd; font-size: 1em; padding: 0.5em; }
</style>

<script type="text/javascript" src="https://caligatio.github.io/jsSHA/sha.js"></script>

<script type="text/javascript">
function CopyText(arg){
    element =  document.getElementById(arg)
    element.focus();
    element.setSelectionRange(0, 9999);
    document.execCommand("copy");
    element.blur();
    document.getElementById("Result").value = "Copied";
    document.getElementById("master").value = "";
}
function calcHash() {
try {
    var master = document.getElementById("master");

<!-- ------------------------------------------------ Site information --------------------------- -->

'''

######################################################

    html = html + \
        ('site = "{0}" <!-- Default selection -->'.format(sites[0][0]))

    html = html + '''

    var sitekey = new Object({

'''
    for i in sites:
        site = i[0]
        key = [i[1]['hash'], i[1]['char'], int(i[1]['len']), i[1]['seed']]
        for c in i[1]['comment'].split('\n'):
            key.append(c)
        html = html + ('        "{0}" : {1},\n'.format(site, key))
    html = html.rstrip(',\n')

######################################################

    html = html + r'''
    });

<!-- -------------------------------------------------------------------------------------------- -->

    var seed = document.getElementsByName('seed');
    for (i = 0; i < seed.length; i++) {
        if (seed[i].checked) {
          site = seed[i].value;
        }
    }

    SiteInfo = "<fieldset class=\"siteinfo\">";
    for (var key in sitekey) {
        if (site == key) {
            checked = "checked=\"checked\" ";
        } else {
            checked = "";
        }
        SiteInfo = SiteInfo + "<input type=\"radio\" name=\"seed\" value=\"" + key + "\" " + checked + "onclick=\"calcHash()\">" + key;
    }
    SiteInfo = SiteInfo + "</fieldset>";

    site = sitekey[site];

    var hash = site[0];
    var char = site[1];
    var plen = site[2];
    var seed = site[3];

    if (site.length > 4) {
        SiteInfo = SiteInfo + "<ul>";
        for (var i = 4; i < site.length; i++) {
            var SiteInfo = SiteInfo + "<li>" + site[i].replace(/((http:|https:)\/\/[\x21-\x26\x28-\x7e]+)/gi, "<a href='$1'>$1</a>") + "</li>";
        }
        SiteInfo = SiteInfo + "</ul>"
    }

    hash = hash.replace("sha3_","SHA3-").replace("sha","SHA-"); <!-- convert from Python hashlib -->
    var Password = document.getElementById("Result");
    var SiteInfoOutput = document.getElementById("SiteInfo");

    var hashObj = new jsSHA(hash, "BYTES");
    hashObj.update(master.value + seed);

    base = hashObj.getHash("B64");

    switch (char) {
    case "base64":
        p = base;
        break;
    case "an":
        p = base.replace(/[+/=]/g,"");
        break;
    case "a":
        p = base.replace(/[0-9+/=]/g,"");
        break;
    case "n":
        p = hashObj.getHash("HEX").replace(/[a-f]/g,"");
        break;
    case "ans":
        symbol = "#[$-=?@]_!"
        p = base.replace(/=/g,"");
        a = p.charCodeAt(0) % symbol.length;
        symbol = symbol.slice(a,-1) + symbol.slice(0,a)
        for (var i = 0; i < symbol.length; i++) {
            p = p.split(p.charAt(0)).join(symbol.charAt(i)).slice(1,-1) + p.charAt(0);
        }
           break;
    default:
        p = "Error";
        break;
    }
    Password.value = p.slice(0,plen);
    if (SiteInfo > "") {SiteInfoOutput.innerHTML = SiteInfo;}
    document.getElementById("master").focus();
    } catch(e) {
        Password.value = e.message
    }
}
</script>
</head>
<body onload="calcHash()">
<h1>Passme JS</h1>

<form action="#" method="get">

<div id="SiteInfo"></div>

<fieldset id="PasswdField" onclick="document.getElementById('Passwd').focus();">
    <label id="PasswdLabel" for="master">Master</label>
    <div class="Field">
        <input type="text" name="master" id="master" onkeyup="calcHash()">
    </div>
</fieldset>
<div>
    <input class="Result" type="text" name="Result" id="Result">
</div>
<div>
    <input class="Copy" type="button" name="Copy" value="Copy" onClick="CopyText('Result');">
</div>
</form>

<p><a href="https://github.com/sekika/passme">Passme</a></p>
</body>
</html>
'''

######################################################

    return html
