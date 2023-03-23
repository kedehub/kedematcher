import os

supported_languages = {
    '1C Enterprise': ['bsl', 'os'],
    'Apex': ['cls'],
    'Assembly': ['asm'],
    'Batchfile': ['bat', 'cmd', 'btm'],
    'C': ['c', 'h'],
    'C++': ['cpp', 'cxx', 'hpp', 'cc', 'hh', 'hxx'],
    'C#': ['cs'],
    'CSS': ['css'],
    'Clojure': ['clj'],
    'COBOL': ['cbl', 'cob', 'cpy'],
    'CoffeeScript': ['coffee'],
    'Crystal': ['cr'],
    'Dart': ['dart'],
    'Groovy': ['groovy', 'gvy', 'gy', 'gsh'],
    'HTML+Razor': ['cshtml'],
    'EJS': ['ejs'],
    'Elixir': ['ex', 'exs'],
    'Elm': ['elm'],
    'ERB': ['erb'],
    'Erlang': ['erl', 'hrl'],
    'F#': ['fs', 'fsi', 'fsx', 'fsscript'],
    'Fortran': ['f90', 'f95', 'f03', 'f08', 'for'],
    'Go': ['go'],
    'Haskell': ['hs', 'lhs'],
    'HCL': ['hcl', 'tf', 'tfvars'],
    'HTML': ['html', 'htm', 'xhtml'],
    'JSON': ['json'],
    'Java': ['java'],
    'JavaScript': ['js', 'jsx', 'mjs', 'cjs'],
    'Jupyter Notebook': ['ipynb'],
    'Kivy': ['kv'],
    'Kotlin': ['kt', 'kts'],
    'Less': ['less'], 
    'Lex': ['l'],
    'Liquid': ['liquid'],
    'Lua': ['lua'],
    'MATLAB': ['m'],
    'Nix': ['nix'],
    'OpenEdge ABL': ['p', 'ab', 'w', 'i', 'x'],
    'Perl': ['pl', 'pm', 't'],
    'PHP': ['php'],
    'PLSQL': ['pks', 'pkb'],
    'Protocol Buffer': ['proto'],
    'Puppet': ['pp'],
    'Python': ['py'],
    'QML': ['qml'],
    'R': ['r'],
    'Raku': ['p6','pl6','pm6','rk','raku','pod6','rakumod','rakudoc'],
    'Robot': ['robot'],
    'Ruby': ['rb'],
    'Rust': ['rs'],
    'Scala': ['scala'],
    'SASS': ['sass'],
    'SCSS': ['scss'],
    'Shell': ['sh'],
    'Smalltalk': ['st'],
    'Stylus': ['styl'],
    'Svelte': ['svelte'],
    'Swift': ['swift'],
    'TypeScript': ['ts', 'tsx'],
    'Vue': ['vue'],
    'Xtend': ['xtend'],
    'Xtext': ['xtext'],
    'Yacc': ['y'],
    'Objective-C': ['mm', 'm'],
    'Configuration': ['properties','yaml','xml','props', 'toml', 'yml'],
    'Tcl' : ['tcl', 'tbc', 'tk'],
    'M4' : ['m4'],
    'CMake' : ['cmake'],
    'Awk' : ['awk'],
    'PowerShell' : ['ps1'],
    'Markdown' : ['md'],
    'reStructuredText' : ['rst'],
    'LLVM' : ['ll', 'ir'],
    'CUDA' : ['cu', 'cuh'],
    'Starlark' : ['bzl'],
    'MLIR' : ['mlir'],
    'DIGITAL Command Language' : ['com'],
    'FreeMarker' : ['ftl'],
    'Hack' : ['hck', 'hack', 'hhi'],
    'OCaml' : ['ml', 'mli'],
    'AspectJ': ['aj'],
    'Solidity': ['sol'],
    'Fe': ['fe'],
    'Emacs Lisp': ['el'],
    'Isabelle': ['thy'],
    'Translation': ['po'],
    'TeX': ['tex'],
    'Rosetta DSL': ['ros'],
    'Text': ['txt'],
}

_ext_lang = {}

def _build_ext_lang_map():
    """
    For optimisation purposes, build ext -> language map. Supposed to run once and cache
    """
    if not _ext_lang:
        for lang, extensions in supported_languages.items():
            for ext in extensions:
                _ext_lang[ext] = lang

    return _ext_lang


def detect_language(file_path):
    parts = file_path.split(os.sep)
    file_name = parts[-1]

    if file_name == 'Dockerfile':
        return 'Dockerfile'
    if file_name == 'Makefile':
        return 'Makefile'

    ext = file_name.split('.')[-1].lower()

    if ext in _ext_lang:
        return _ext_lang[ext]

    return 'Other'


# This ensures the ext to lang map is build upon the module import
if not _ext_lang:
    _build_ext_lang_map()
