最近接了个小单，遇到一个很头疼的问题，返回的状态码无限521，在网上查阅了各种资料后，终于解决了问题返回200。

首先咱们先贴上网址：点击打开链接

首先我们按照传统的方法

```
import requests
headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
req=requests.get('https://www.seebug.org/vuldb/ssvid-92666',headers=headers).status_code
print(req)

/usr/bin/python3.5 /home/pipidi/Spider/lianjia/lianjia/spiders/__init__.py
521

Process finished with exit code 0
```
可以说是毫无疑问 返回的是521

下面贴出两种解决办法：

（1）：直接复制`request` `header`

我们可以打开谷歌F12 找到其中的network 可以找到本网站地址的一个html 文件 直接复制所有他的头部

```
import requests
from copyheaders import headers_raw_to_dict
header=b'''''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh,en-US;q=0.9,en;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Cookie:__jsluid=9536c75cdfa3e7e8c38d59bcbf4fc98b; csrftoken=YzAMB2QogF2YmzpruqWI5vdsfeH9PSx5; Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1519809319,1519880921; __jsl_clearance=1519885472.708|0|IQ9%2FbeQ6cfNLaEZUk2QzXhNEtL8%3D; Hm_lpvt_6b15558d6e6f640af728f65c4a5bf687=1519885477
Host:www.seebug.org
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'''
req=requests.get('https://www.seebug.org/vuldb/ssvid-92666',headers=headers_raw_to_dict(header)).status_code
print(req)


200

Process finished with exit code 0
```
就可以返回200,但是在实际爬取的过程中，会发现他还是会时不时返回521，并且cookie 是饼干屑具有时效性，不可能一直保存，所以方法1也不能说是最优解，下面我们来介绍一下方法2



（2）：使用exejs执行js代码返回cookie

首先，我们先用带`User-Agent`的request去访问这个网站，还是令人沮丧，返回的是521

```
import requests
header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
req=requests.get('https://www.seebug.org/vuldb/ssvid-92666',headers=header).status_code
print(req)

521

Process finished with exit code 0
```

然后我们输出他的内容 使用`requests.get().text`方法

哇！？ 看看看这是啥？ 懂一点前端的同学估计都顿悟出来了 这！就是JS代码

查阅了很多大佬的博客，我发现 这是一种js加密cookie的手法

先访问第一次访问 返回521 并且给浏览器设置cookies 在第二次刷新的时候，你的浏览器就可以用设置上的cookie自动访问了

但是咱的爬虫不一样，无法加载js，就一直卡在第一次访问了

对此 我们的做法是让Python运行js代码，获取cookies 并且加到下次访问的头部

行！就这么做！

我们首先获取返回的源代码

```
def get_521_content():
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    req=requests.get('https://www.seebug.org/vuldb/ssvid-92666',headers=headers)
    cookies=req.cookies

    cookies='; '.join(['='.join(item) for item in cookies.items()])
    txt_521=req.text
    txt_521=''.join(re.findall('<script>(.*?)</script>',txt_521))
    return (txt_521,cookies)
```
我们需要返回的分别是两个 第一个是网页的源代码 第二个是后台设置的cookie

然后我们对拿来的js代码进行修改并且运行

我使用的Python 执行js的模块是execjs ，在这里我也不过多赘述

主要的修改是将eval 替换成return 让他有返回值给咱看到

```
def fixed_fun(function):
    func_return=function.replace('eval','return')
    content=execjs.compile(func_return)
    evaled_func=content.call('f')
```

```
var l=function(){while(window._phantom||window.__phantomas){};var cd,dc='__jsl_clearance=1519886795.502|0|';cd=[((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![]))-~~~[]-~-~{}-~~~[]-~-~{}+[]+[]),[4],(-~~~[]+[]+[])+(-~~~[]+[]+[]),(-~~~[]+[]+[]),(-~~~[]+[]+[])+[(-~[]|-~-~{})+(2<<-~[])],(-~~~[]+[]+[])+[4],(2+[[], ~~!{}][~~{}]),((-~-~{})*[(-~-~{}<<-~[])]+[]+[]),((+[])+[[], ~~!{}][~~{}]),(-~~~[]+[]+[])+((+[])+[[], ~~!{}][~~{}]),((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![]))+[[], ~~!{}][~~{}]),(-~~~[]+[]+[])+(-~![]+((-~![]<<-~![])<<-~[])+[]+[[]][~~[]]),[[-~-~{}]*((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![])))],(-~~~[]+[]+[])+[[-~-~{}]*((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![])))],(-~~~[]+[]+[])+(2+[[], ~~!{}][~~{}]),(-~~~[]+[]+[])+((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![]))+[[], ~~!{}][~~{}]),[(-~[]|-~-~{})+(2<<-~[])],(-~![]+((-~![]<<-~![])<<-~[])+[]+[[]][~~[]])];for(var i=0;i<cd.length;i++){cd[i]=[([-~[]-~[]-~[]-~[]][-~[]]+[]+[]).charAt(-~[-~~~[]-~(-~((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![]))))]),'HE',(2+[[], ~~!{}][~~{}])+[-~[]/~~[]+[]+[]][0].charAt(7)+(((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![])))/~~[]+[]).charAt(-~-~{})+[!{}+[[]][~~!{}]][0].charAt((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![])))+(-~~~[]+[]+[]),(2+[[], ~~!{}][~~{}]),'SG','D',[{}+[[]][~~!{}]][0].charAt(8),((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![]))+[[], ~~!{}][~~{}]),'T',(((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![])))/~~[]+[]).charAt(-~-~{})+[-~[]/~~[]+[]+[]][0].charAt(7)+[!{}+[[]][~~!{}]][0].charAt((-~[]+[(-~![]<<-~![])]>>(-~![]<<-~![])))+[-~[]/~~[]+[]+[]][0].charAt(7),'%',(-~![]+((-~![]<<-~![])<<-~[])+[]+[[]][~~[]])+((+[])+[[], ~~!{}][~~{}]),[-~[]/~~[]+[]+[]][0].charAt(7),'k%','x','FE','SEA',[!-[]+[]+[]][0].charAt(-~-~{})][cd[i]]};cd=cd.join('');dc+=cd;setTimeout('location.href=location.href.replace(/[\?|&]captcha-challenge/,\'\')',1500);document.cookie=(dc+';Expires=Thu, 01-Mar-18 07:46:35 GMT;Path=/;');};if((function(){try{return !!window.addEventListener;}catch(e){return false;}})()){document.addEventListener('DOMContentLoaded',l,false);}else{document.attachEvent('onreadystatechange',l);}
```
我们可以看到代码解密出来有变成了新的一串js代码

我们可以吧他放到html文件里面运行

我这里是直接放到exejs中运行的，对代码也进行了各种修改，最重要的是将`document.cookie=（）`函数替换成`return`这样就可以直接用`print`输出返回的内容了，对于其他的修改，大家只要那里报错删那里就行。

```

mode_func=evaled_func.replace('while(window._phantom||window.__phantomas){};','').\
        replace('document.cookie=','return').replace(';if((function(){try{return !!window.addEventListener;}','').\
        replace("catch(e){return false;}})()){document.addEventListener('DOMContentLoaded',l,false);}",'').\
        replace("else{document.attachEvent('onreadystatechange',l);}",'').replace(r"setTimeout('location.href=location.href.replace(/[\?|&]captcha-challenge/,\'\')',1500);",'')
    content = execjs.compile(mode_func)
    cookies=content.call('l')
    __jsl_clearance=cookies.split(';')[0]
    return __jsl_clearance
```

经过了一堆修改之后，

```
if __name__ == '__main__':
    func=get_521_content()
    content=func[0]
    cookie_id=func[1]
    print(cookie_id)
    cookie_js=fixed_fun(func[0])
    print(cookie_js)
```
我们会惊奇的发现，Python执行了js代码，并且返回了一段cookie，他就是我们想要的！之后我们需要做的事就比较轻松了，只需要把后台设置的`__jsluid `和js设置的`cookie` ` __jsl_clearance`一起加入我们的浏览器头就可以正常访问了

```
headers={
             'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
             'Cookie': cookie_id+';'+cookie_js}  #一定要和第一次访问的user-agent一模一样
    code=requests.get('https://www.seebug.org/vuldb/ssvid-92666',
                      headers=headers).text
    print(code)
```


