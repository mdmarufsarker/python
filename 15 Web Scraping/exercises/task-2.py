# TASK: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.

import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

print(soup)

'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Quotes to Scrape</title>
<link href="/static/bootstrap.min.css" rel="stylesheet"/>
<link href="/static/main.css" rel="stylesheet"/>
</head>
<body>
<div class="container">
<div class="row header-box">
<div class="col-md-8">
<h1>
<a href="/" style="text-decoration: none">Quotes to Scrape</a>
</h1>
</div>
<div class="col-md-4">
<p>
<a href="/login">Login</a>
</p>
</div>
</div>
<div class="row">
<div class="col-md-8">
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
<span>by <small class="author" itemprop="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="change,deep-thoughts,thinking,world" itemprop="keywords"/>
<a class="tag" href="/tag/change/page/1/">change</a>
<a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
<a class="tag" href="/tag/thinking/page/1/">thinking</a>
<a class="tag" href="/tag/world/page/1/">world</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>
<span>by <small class="author" itemprop="author">J.K. Rowling</small>
<a href="/author/J-K-Rowling">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="abilities,choices" itemprop="keywords"/>
<a class="tag" href="/tag/abilities/page/1/">abilities</a>
<a class="tag" href="/tag/choices/page/1/">choices</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>
<span>by <small class="author" itemprop="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="inspirational,life,live,miracle,miracles" itemprop="keywords"/>
<a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
<a class="tag" href="/tag/life/page/1/">life</a>
<a class="tag" href="/tag/live/page/1/">live</a>
<a class="tag" href="/tag/miracle/page/1/">miracle</a>
<a class="tag" href="/tag/miracles/page/1/">miracles</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>
<span>by <small class="author" itemprop="author">Jane Austen</small>
<a href="/author/Jane-Austen">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="aliteracy,books,classic,humor" itemprop="keywords"/>
<a class="tag" href="/tag/aliteracy/page/1/">aliteracy</a>
<a class="tag" href="/tag/books/page/1/">books</a>
<a class="tag" href="/tag/classic/page/1/">classic</a>
<a class="tag" href="/tag/humor/page/1/">humor</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”</span>
<span>by <small class="author" itemprop="author">Marilyn Monroe</small>
<a href="/author/Marilyn-Monroe">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="be-yourself,inspirational" itemprop="keywords"/>
<a class="tag" href="/tag/be-yourself/page/1/">be-yourself</a>
<a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>
<span>by <small class="author" itemprop="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="adulthood,success,value" itemprop="keywords"/>
<a class="tag" href="/tag/adulthood/page/1/">adulthood</a>
<a class="tag" href="/tag/success/page/1/">success</a>
<a class="tag" href="/tag/value/page/1/">value</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>
<span>by <small class="author" itemprop="author">André Gide</small>
<a href="/author/Andre-Gide">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="life,love" itemprop="keywords"/>
<a class="tag" href="/tag/life/page/1/">life</a>
<a class="tag" href="/tag/love/page/1/">love</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>
<span>by <small class="author" itemprop="author">Thomas A. Edison</small>
<a href="/author/Thomas-A-Edison">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="edison,failure,inspirational,paraphrased" itemprop="keywords"/>
<a class="tag" href="/tag/edison/page/1/">edison</a>
<a class="tag" href="/tag/failure/page/1/">failure</a>
<a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
<a class="tag" href="/tag/paraphrased/page/1/">paraphrased</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>
<span>by <small class="author" itemprop="author">Eleanor Roosevelt</small>
<a href="/author/Eleanor-Roosevelt">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="misattributed-eleanor-roosevelt" itemprop="keywords"/>
<a class="tag" href="/tag/misattributed-eleanor-roosevelt/page/1/">misattributed-eleanor-roosevelt</a>
</div>
</div>
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
<span>by <small class="author" itemprop="author">Steve Martin</small>
<a href="/author/Steve-Martin">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="humor,obvious,simile" itemprop="keywords"/>
<a class="tag" href="/tag/humor/page/1/">humor</a>
<a class="tag" href="/tag/obvious/page/1/">obvious</a>
<a class="tag" href="/tag/simile/page/1/">simile</a>
</div>
</div>
<nav>
<ul class="pager">
<li class="next">
<a href="/page/2/">Next <span aria-hidden="true">→</span></a>
</li>
</ul>
</nav>
</div>
<div class="col-md-4 tags-box">
<h2>Top Ten tags</h2>
<span class="tag-item">
<a class="tag" href="/tag/love/" style="font-size: 28px">love</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/inspirational/" style="font-size: 26px">inspirational</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/life/" style="font-size: 26px">life</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/humor/" style="font-size: 24px">humor</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/books/" style="font-size: 22px">books</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/reading/" style="font-size: 14px">reading</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/friendship/" style="font-size: 10px">friendship</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/friends/" style="font-size: 8px">friends</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/truth/" style="font-size: 8px">truth</a>
</span>
<span class="tag-item">
<a class="tag" href="/tag/simile/" style="font-size: 6px">simile</a>
</span>
</div>
</div>
</div>
<footer class="footer">
<div class="container">
<p class="text-muted">
                Quotes by: <a href="https://www.goodreads.com/quotes">GoodReads.com</a>
</p>
<p class="copyright">
                Made with <span class="sh-red">❤</span> by <a href="https://scrapinghub.com">Scrapinghub</a>
</p>
</div>
</footer>
</body>
</html>
'''