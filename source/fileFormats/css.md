## Description

[Cascading Style Sheets]({{wikipedia}}/Cascading_Style_Sheets)
is a language for styling
[=html] documents.
It is widely used on the web.

[=html] files may contain CSS styles inside, or they may refer to other files for
their styling.

## Complications

The World-wide-web is one of the most dynamic corners of IT. Standards are
always on the move, and new patterns of organizing web content replace the best
practices of yesterday.

CSS has gone through several major versions.

The format is [=text], so CSS files are easy to open,
but the meaning of the styles is dependent on the version of the
CSS styling engine that has been used.

Moreover, in real-world web applications, CSS files are often
deliberately `uglified`, in order to decrease their file size.

## Recommendations

For archiving it must be made clear to which files the CSS files refer and which
version of CSS is being used. As browser-specific extensions may exist, the
target environment of the files must be known, unless only basic elements have
been used. If the CSS files contain links to other CSS files or external files,
these links must be working.

If the CSS files have been uglified, their non-uglified sources should be archived as well.

