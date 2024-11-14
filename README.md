# note-reformatter

**Overview**

My primary motivation for creating this project was I wanted to stop nodding off when I was reading dense books. My idea was to convert e-books, PDFs, or any digitally scanned textbook into a crisp, readable interface where I could easily take notes. More specifically, I wanted a quicker and more painless version of the Cornell notetaking method (link: https://www.goodnotes.com/blog/cornell-notes).

Here, I wanted to split the text by paragraph, and then split each paragraph by sentence. This way, I could quickly scan the contents of the paragraph and then summarize the contents with a heading. At the end of the chapter, I would summarize everything.

This more or less gamified the notetaking process so I could stay focused and prevent getting exhausted by dense walls of text.

In the files provided, **_redacted_demo.pdf** should end up looking like **_demo_final_result.pdf**. You could then annotate it by summarizing each paragraph as shown in **_demo_final_result_annotated.pdf**.

However, PDFs are a notorious frustrating file format to work with, and something as simple as extracting text with all the line breaks and whitespace intact is usually a tremendous headache. As such, the code can sometimes spit out an unorganized mess.

You should avoid textbooks or anything with a lot of images and strangely placed texts, as it usually never gets the desired results.

___

**Process**

The best way to minimize issues is as follows:

1. Redact headers and footers (e.g. pages, chapter titles as headers, footnotes) as well as images. I paid for Adobe Acrobat, which made this process easy, but there might be some good free options out there. Either way, I provided a **redacted demo** as proof of concept.

2. Run **pdf_prep.py** and enter the path of the redacted PDF. Again, as proof of concept you can use **_redacted_demo.pdf**.

3. Take the output file of **pdf_prep.py** (i.e. the **original filename + "_final"**) and use an online converter to convert it into an epub, then into a txt file. I tried relentlessly to do this part as code, but it was just too difficult and unpredictable. For whatever reason, converting the PDF twice in this way fixes a persistent issue I had with line and page breaks.

4. Run **pdf_export.py** and enter the path of the converte txt document. It should result in a properly reformatted Microsoft Word Document ending in "**_final**".
