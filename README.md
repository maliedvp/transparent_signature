## usability

ensure that an image file that contains a photo of the signature is stored in the directory. The directory includes a test file `test_input.png` in the `res/` subfolder by default. If you wish to convert this file into a transparent png file that, run

  python transparent_signiture -i res/test_input.png -o res/test_output.png
    
The created file's name is `test_output.png`


## inclusion to an existing pdf using Latex


    \documentclass[12pt,a4paper]{article}
    \usepackage{pdfpages,eso-pic}

    \begin{document}
    \includepdf[pages={1-2}]{blank_pdf.pdf}

    \includepdf[pages=3, pagecommand={%
    \begin{picture}(0,0)
    \put(130,-300){\includegraphics[width=0.25\textwidth]{test_output.png}}
    \end{picture}
    }]{blank_pdf.pdf}
    \end{document}
    
The add_to_pdf.tex script in the `res/` folder includes these lines and serves as an example.