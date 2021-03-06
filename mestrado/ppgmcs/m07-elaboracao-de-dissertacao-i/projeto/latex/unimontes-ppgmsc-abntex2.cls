%%
%% Customizações do abnTeX2 (http://abnTeX2.googlecode.com) para a Universidade XXXX
%%
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%   http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2005/12/01 or later.
%%
%% This work has the LPPL maintenance status `maintained'.
%% 
%% The Current Maintainer of this work is SEU_NOME, SEU_EMAIL
%%
%% Further information about abnTeX2 are available on http://abntex2.googlecode.com/
%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{unimontes-ppgmsc-abntex2}[2015/04/01 v1.0 Modelo da Universidade Unimontes baseado em abnTeX2]

%
% Repassa todos os parametros a classe abntex2, 
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{abntex2}%
}
\ProcessOptions\relax
\LoadClass{abntex2}

% alterando a capa
\renewcommand{\imprimircapa}{%
  \begin{capa}%

\vspace*{-1cm}\hspace*{-1.5cm} {\mbox{\begin{minipage}{2cm}
\centerline{\includegraphics[scale=0.22]{estadominas.jpeg}}
\end{minipage}}} \hspace{-.6cm} 
\begin{minipage}{11.5cm}
\begin{center}
{\textbf{\large Universidade Estadual de Montes Claros}}\\
{\textsc{\small Pr\'{o}-reitoria de P\'{o}s-Gradua\c{c}\~{a}o}}\\
{\textsc{\small Programa de P\'{o}s-Gradua\c{c}\~{a}o em Modelagem Computacional e Sistemas}}\\
\end{center}
\end{minipage}{\mbox{\begin{minipage}{2cm}
\centerline{\includegraphics[scale=0.065]{unimontes.png}}
\end{minipage}}} 

\vspace{1cm}

\centerline{\includegraphics[scale=0.50]{ppgmcs.png}}

    \center
%    \ABNTEXchapterfont\Large {\abntex@ifnotempty{\imprimirinstituicao}{\imprimirinstituicao}}

	%{\ABNTEXchapterfont\large\imprimirorientador}
    
    \vspace*{1cm}
    
    
    {\ABNTEXchapterfont\large\imprimirautor}

    \vfill
    \begin{center}
    \ABNTEXchapterfont\bfseries\LARGE\imprimirtitulo
    \end{center}
    \vfill
    
    \large\imprimirlocal

    \large\imprimirdata
    
    \vspace*{1cm}
    %\clearpage
  \end{capa}
}

% Novo list of (listings) para QUADROS

\newcommand{\quadroname}{Quadro}
\newcommand{\listofquadrosname}{Lista de quadros}

\newfloat[chapter]{quadro}{loq}{\quadroname}
\newlistof{listofquadros}{loq}{\listofquadrosname}
\newlistentry{quadro}{loq}{0}

% configurações para atender às regras da ABNT
\setfloatadjustment{quadro}{\centering}
\counterwithout{quadro}{chapter}
\renewcommand{\cftquadroname}{\quadroname\space} 
\renewcommand*{\cftquadroaftersnum}{\hfill--\hfill}

% Configuração de posicionamento padrão:
\setfloatlocations{quadro}{hbtp}


% folha de rosto 

\makeatletter

\renewcommand{\folhaderostocontent}{
\begin{center}
%{\ABNTEXchapterfont\Large Universidade Estadual de Montes Claros -- UNIMONTES}
    
 %   \vspace*{1cm}
    
{\ABNTEXchapterfont\large\imprimirautor}

\vspace*{\fill}\vspace*{\fill}

\begin{center}
\ABNTEXchapterfont\bfseries\Large\imprimirtitulo
\end{center}

\vspace*{\fill}

\abntex@ifnotempty{\imprimirpreambulo}{%
  \hspace{.45\textwidth}
  \begin{minipage}{.5\textwidth}
  \SingleSpacing
  \imprimirpreambulo
  \end{minipage}%
  \vspace*{\fill}
}%

 \hspace{.45\textwidth}
 \begin{minipage}{.5\textwidth}
 	\SingleSpacing
{\imprimirorientadorRotulo~\imprimirorientador\par}
 \end{minipage}%
 
\abntex@ifnotempty{\imprimircoorientador}{%
	 \hspace{.45\textwidth}
 \begin{minipage}{.5\textwidth}
 	%\SingleSpacing	
  {\imprimircoorientadorRotulo~\imprimircoorientador}%
   \end{minipage}%
}%



\vspace*{\fill}

%{\abntex@ifnotempty{\imprimirinstituicao}{\imprimirinstituicao\vspace*{\fill}}}

{\large\imprimirlocal}

\par

{\large\imprimirdata}
\vspace*{1cm}
\end{center}
}

\makeatother
