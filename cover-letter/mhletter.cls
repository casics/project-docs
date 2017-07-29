%% Filename:     mhletter.cls                             -*- mode: latex -*-
%% Description:  LaTeX style file for simple letters
%% Author(s):    Michael Hucka <mhucka@caltech.edu>
%% Organization: California Institute of Technology
%% Date created: 2016-01-03

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mhletter}

% Class options.
% .............................................................................

\newif\if@nomark
\DeclareOption{nomark}{\global\let\if@nomark\iftrue}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessOptions
\LoadClass{article}

% Latex package dependencies.
% ...........................................................................

\RequirePackage[pdftex]{graphicx}
\RequirePackage[pdftex,rgb,dvipsnames,svgnames,hyperref,table]{xcolor}
\RequirePackage[letterpaper,centering,top=1in,total={6.5in,9in}]{geometry}
\RequirePackage{fourier}
\RequirePackage{microtype}
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{xspace}
\RequirePackage{soul}
\RequirePackage{url}
\RequirePackage[square,numbers,sort&compress]{natbib}
\RequirePackage{scrextend}
\RequirePackage{xhfill}
\RequirePackage{suffix}
\RequirePackage{enumitem}
\RequirePackage{calc}
\RequirePackage{varwidth}
\RequirePackage[american]{varioref}
\RequirePackage[T1]{fontenc}
\RequirePackage{draftwatermark}

\RequirePackage[pdftex,breaklinks=true,colorlinks=true, bookmarks=false,pdfhighlight=/O,urlcolor=darkblue,citecolor=darkred,linkcolor=darkblue]{hyperref}


% Color definitions.
% .............................................................................

\definecolor{extremelylightgray}{gray}{0.97}
\definecolor{veryverylightgray}{gray}{0.95}
\definecolor{verylightgray}{gray}{0.9}
\definecolor{lightgray}{gray}{0.8}
\definecolor{mediumgray}{gray}{0.5}
\definecolor{darkgray}{gray}{0.3}
\definecolor{almostblack}{gray}{0.23}
\definecolor{lightyellow}{rgb}{0.98,0.94,0.7}
\definecolor{verylightyellow}{rgb}{0.97,0.95,0.85}
\definecolor{darkblue}{rgb}{0.1,0.4,0.55}
\definecolor{mediumgreen}{rgb}{0.1,0.6,0.3}
\definecolor{darkred}{rgb}{0.6,0,0.1}

% Style adjustments.
% .............................................................................

% Adjust line spacing.

\renewcommand{\baselinestretch}{0.96}

% Paragraph and list style adjustments.

\setlength{\parindent}{0 pt}            % Unindented paragraphs, separated ...
\setlength{\parskip}{1.3 ex}            % ... by roughly one blank line.
\setlength{\partopsep}{-1ex plus 0.1ex minus -0.2ex}
\setlength{\itemsep}{-0.25ex plus 0.15ex}

% 'booktabs' package adjustments:

\setlength{\cmidrulewidth}{0.3 pt}
\setlength{\lightrulewidth}{0.3 pt}
\setlength{\heavyrulewidth}{0.9 pt}

% Fix placement of figures & tables.  This keeps latex from shoving big
% floats to the end of a document when they are somewhat big, which it will
% do even if you put [htb] as the argument.

\setcounter{topnumber}{2}               % max num of floats at top of page
\setcounter{bottomnumber}{2}            % max num of floats at bottom of page
\renewcommand\topfraction{1.0}          % fraction that a top float can cover
\renewcommand\bottomfraction{1.0}       % fraction a bottom float can cover
\renewcommand\textfraction{0.0}        % >5% of a non-float page must be text
\renewcommand\floatpagefraction{0.9}   % float page must be 95% full

% Spacing of floats.

\setlength{\intextsep}{10pt plus 4pt minus 0pt}

% Make floats that appear alone on a page appear at the top, rather than
% (as is the LaTeX default) appearing centered vertically on the page.

\setlength{\@fptop}{5pt}

% The following uses txtt for the typewriter font, instead of the default.

\renewcommand{\ttdefault}{txtt}
\makeatletter
\DeclareMathAlphabet{\mathtt}{T1}{txtt}{m}{n}
\SetMathAlphabet{\mathtt}{bold}{T1}{txtt}{b}{n}
\def\Txtt@scale{0.98}
\edef\Txtt@@scale{s*[\csname Txtt@scale\endcsname]}%
\DeclareFontFamily{T1}{txtt}{\hyphenchar \font\m@ne}
\DeclareFontShape{T1}{txtt}{m}{n}{	% regular
     <-> \Txtt@@scale txtt%
}{}
\DeclareFontShape{T1}{txtt}{b}{n}{	% bold
     <-> \Txtt@@scale txbtt%
}{}
\makeatother

% Watermark on every page.

\if@nomark\else
  \SetWatermarkText{\includegraphics{watermark.pdf}}
\fi


% Section divider helpers
% .............................................................................

\newcommand{\divider}[1]{\vspace{0.5em}\textbf{#1}~\xrfill[0pt]{0.5pt}[gray]}
\newcommand{\subdivider}[1]{\vspace{0.5em}\textbf{\textsl{#1}}}


% Miscellaneous
% .............................................................................

\newcommand{\eg}{e.g.,\xspace}
\newcommand{\idorg}{\href{http://identifiers.org}{\texttt{Identifiers.org}}\xspace}
