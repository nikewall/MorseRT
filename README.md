# MorseRT

Created during SwampHacks 2020 @ University of Florida (1/31-2/2)

by Niklas Wallace


## Purpose
Language is an important part of both individual and collective human history.
In U.S. history in particular, Morse Code has played a huge role in secure
communications since the creating of communicative technologies like the
telegram.

In modern times we don't have a day-to-day need for communication in Morse Code,
or other code languages, as we have developed other technology to obfuscate the language(s).

Regardless of adaptations and innovations which make daily life much easier,
I believe that it is important to keep some sort of connection with our origins
 -- in this case **secure and private communication** -- a belief which led to this project.

Also, it seemed like a fun challenge to do real-time, clocked key polling :P

## What it Does
**MorseRT** stands for "Morse in Real Time". Of course all Morse Code is
in real time, but this also converts Morse->ASCII with (hopefully) minimal latency
to the end user.

## Technical

* **Morse.py** is the driver. It uses the Python library *pynput* for
the keyboard input calculations, as well as the *time* library for clocking.

* **Choice of DS/A**
    * Data Structure: *Map*
        - *Why*: O(1) conversion from a Morse "string" to an ASCII character
    * Algorithm(s): *None*
        - *Possible improvement*: Create an algorithm (ML?) to auto-adjust
        "speeds" necessary to make dashes and dots, as well as what the minimum
        time is for a space to be registered.
