import paired as paired

from listalign.fuzzyalign import fuzzyalign
from listalign.helpers import alignment_table
from listalign.suffixtreealign import suffix_align

lists = \
(['Justice', 'And', 'The', 'Politics', 'Of', 'Difference\n\nBrowse', 'and', 'Read', 'Justice', 'And', 'The', 'Politics',
 'Of', 'Difference\n\nSimple', 'way', 'to', 'get', 'the', 'amazing', 'book', 'from', 'experienced', 'author?', 'Why',
 'not?', 'The', 'way', 'is', 'very', 'simple', 'if', 'you', 'get', 'the\nbook', 'right', 'here.', 'You', 'need', 'only',
 'the', 'book', 'soft', 'files', 'right', 'here.', 'It', 'is', 'based', 'on', 'the', 'links', 'that', 'are',
 'published', 'in', 'this\nwebsite.', 'By', 'visiting', 'the', 'link,', 'you', 'can', 'gain', 'the', 'book',
 'directly.', 'And', 'here,', 'you', 'will', 'find', 'out', 'many', 'kinds', 'of', 'the', 'books\nwritten', 'by', 'the',
 'professional', 'writers', 'from', 'all', 'world', 'places.\n\nFor', 'this', 'reason,', 'you', 'can', 'take',
 'justice', 'and', 'the', 'politics', 'of', 'difference', 'as', 'one', 'of', 'your', 'reading', 'materials', 'today.',
 'Even', 'you\nstill', 'have', 'the', 'other', 'book', 'you', 'can', 'develop', 'your', 'willingness', 'to', 'really',
 'get', 'this', 'meaningful', 'book.', 'It', 'will', 'always', 'give\nadvantages', 'from', 'some', 'sides.', 'Reading',
 'this', 'kind', 'of', 'book', 'also', 'will', 'guide', 'you', 'to', 'have', 'more', 'experiences', 'that',
 'others\nhave', "not.\n\nIt's", 'not', 'surprisingly', 'when', 'entering', 'this', 'site', 'to', 'get', 'the', 'book.',
 'One', 'of', 'the', 'popular', 'books', 'now', 'is', 'the', 'justice', 'and', 'the\npolitics', 'of', 'difference.',
 'You', 'may', 'be', 'confused', 'because', 'you', "can't", 'find', 'the', 'book', 'in', 'the', 'book', 'store',
 'around', 'your', 'city.\nCommonly,', 'the', 'popular', 'book', 'will', 'be', 'sold', 'quickly.', 'And', 'when', 'you',
 'have', 'found', 'the', 'store', 'to', 'buy', 'the', 'book,', 'it', 'will', 'be\nso', 'hurt', 'when', 'you', 'run',
 'out', 'of', 'it.', 'This', 'is', 'why,', 'searching', 'for', 'this', 'popular', 'book', 'in', 'this', 'website',
 'will', 'give', 'you', 'benefit.\nYou', 'will', 'not', 'run', 'out', 'of', 'this', 'book.\n\nThis', 'concept', 'is',
 'because', 'we', 'offer', 'the', 'soft', 'file', 'of', 'the', 'book.', 'When', 'other', 'people', 'bring', 'the',
 'hard', 'book', 'everywhere,', 'you\ncan', 'only', 'hold', 'your', 'gadget.', 'Saving', 'the', 'soft', 'file', 'of',
 'justice', 'and', 'the', 'politics', 'of', 'difference', 'in', 'your', 'gadget', 'will', 'ease', 'you\nin', 'reading.',
 'When', 'you', 'are', 'being', 'at', 'home,', 'you', 'can', 'also', 'open', 'in', 'the', 'computer.', 'So,', 'saving',
 'the', 'book', 'soft', 'file', 'in', 'some\ndevices', 'are', 'available.', 'It', 'will', 'make', 'easier', 'of', 'you',
 'to', 'find', 'how', 'the', 'activity', 'is', 'going', 'to', 'be', 'very', 'simple', 'because', 'of', 'the\nmore',
 'advanced', 'technology.\n\njustice', 'and', 'the', 'politics', 'of', 'difference\n\nPopular', 'Books', 'Similar',
 'With', 'Justice', 'And', 'The', 'Politics', 'Of', 'Difference', 'Are\nListed', 'Below:\n\nPDF', 'File', ':',
 'Justice', 'And', 'The', 'Politics', 'Of', 'Difference', '\n\n', 'Page', ':', '1\n\n\x0c'],
[' Browse and Read Justice And The Politics Of Difference', ' Justice And The Politics Of Difference',
 ' Simple way to get the amazing book from experienced author? Why not? The way is very simple if you get the',
 ' book right here. You need only the book soft files right here. It is based on the links that are published in this',
 ' website. By visiting the link, you can gain the book directly. And here, you will find out many kinds of the books',
 ' written by the professional writers from all world places.',
 " It's not surprisingly when entering this site to get the book. One of the popular books now is the justice and the",
 " politics of difference. You may be confused because you can't find the book in the book store around your city.",
 ' Commonly, the popular book will be sold quickly. And when you have found the store to buy the book, it will be',
 ' so hurt when you run out of it. This is why, searching for this popular book in this website will give you benefit.',
 ' You will not run out of this book.',
 ' This concept is because we offer the soft file of the book. When other people bring the hard book everywhere, you',
 ' can only hold your gadget. Saving the soft file of justice and the politics of difference in your gadget will ease you',
 ' in reading. When you are being at home, you can also open in the computer. So, saving the book soft file in some',
 ' devices are available. It will make easier of you to find how the activity is going to be very simple because of the',
 ' more advanced technology.',
 ' For this reason, you can take justice and the politics of difference as one of your reading materials today. Even you',
 ' still have the other book you can develop your willingness to really get this meaningful book. It will always give',
 ' advantages from some sides. Reading this kind of book also will guide you to have more experiences that others',
 ' have not.', ' Popular Books Similar With Justice And The Politics Of Difference Are', ' Listed Below:', '      ',
 ' PDF File : Justice And The Politics Of Difference Page : 1'])

print(alignment_table(paired.align(*lists), *lists))
print(alignment_table(suffix_align(*lists), *lists))
print(alignment_table(  fuzzyalign(*lists), *lists))
