# Import statements are executed in two steps: (1) find a module, and
# initialize it if necessary; (2) define a name or names in the local
# namespace (of the scope where the "import" statement occurs). The
# statement comes in two forms differing on whether it uses the "from"
# keyword. The first form (without "from") repeats these steps for each
# identifier in the list. The form with "from" performs step (1) once,
# and then performs step (2) repeatedly.
