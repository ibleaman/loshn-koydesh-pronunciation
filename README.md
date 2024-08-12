# loshn-koydesh-pronunciation

A mapping of phonetic forms to orthographic forms (and vice versa) for Yiddish words from *loshn-koydesh* (Hebrew/Aramaic) -- also known as the "Semitic component" of Yiddish.

The lexicon comes from:

Niborski, Yitskhok. 1999. *Verterbukh fun loshn-koydesh-shtamike verter in yidish [Dictionnaire des mots d'origine hébraïque et araméenne en usage dans la langue yiddish/Dictionary of Hebrew- and Aramaic-origin words in Yiddish]*. Paris: Bibliothèque Medem.

The original pronunciation list (*fonetisher indeks / shlisl*) was compiled by Eliezer Niborski and published as a PDF here: https://editions.yiddish.paris/dictionnaire-des-mots-dorigine-hebraique/

This repository contains five files:
* The PDF linked above
* A version in RTF, provided by Eliezer Niborski
* A text file adapted from the RTF, containing a clean mapping of phonetic forms to standard orthographic forms (with many missing inflections added, typos fixed, etc.)
* A Python script to create a reversed mapping of orthographic forms to phonetic forms, based on above
* The output file from the Python script (in tab- and comma-separated format: `orthographic_form	phonetic_form1,phonetic_form2`)

Note: the files may inconsistently use pre-combined Unicode characters (e.g., װ versus וו or ױ versus וי, etc.)

## Overriding phonetic rules

If you are maintaining your own custom mapping files for `orthographic-to-phonetic.txt` and/or `phonetic-to-orthographic.txt`, you can override the defaults by setting the `LOSHN_KOYDESH_O2P_SRC` and/or `LOSHN_KOYDESH_P2O_SRC` environment variables to the file paths of your sources.
