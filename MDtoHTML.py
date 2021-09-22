from markdown import markdown
import codecs
from mdx_math import MathExtension

css = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
<!-- 此处省略掉markdown的css样式，因为太长了 -->
</style>
'''


def transfer():
    name = 'info'
    in_file = f'./source/{name}.md'
    out_file = f'./source/{name}.html'
    with open(in_file, 'r', encoding='utf-8') as f:
        text = f.read()
    html = markdown(text, output_format='html', extensions=['extra', 'codehilite', 'toc',
                                                            'markdown.extensions.nl2br',
                                                            'mdx_math', MathExtension(enable_dollar_delimiter=True)])
    html = "<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' " \
           "async></script>" + html

    output_file = codecs.open(out_file, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_file.write(css+html)


if __name__ == "__main__":
    transfer()
